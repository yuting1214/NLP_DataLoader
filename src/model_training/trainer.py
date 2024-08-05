import torch
from torch.nn import CrossEntropyLoss 
from tqdm.notebook import tqdm
from accelerate import Accelerator
from transformers import get_scheduler
import os

def train_model(model, dataloaders, optimizer, path, num_epochs=3):
    def ce_loss(inputs, logits):
        # Shift so that tokens < n predict n
        shift_labels = inputs[..., 1:].contiguous()
        shift_logits = logits[..., :-1, :].contiguous()
        # Flatten the tensors to fit CrossEntropyLoss expectations
        loss_fct = CrossEntropyLoss() 
        loss = loss_fct(shift_logits.view(-1, shift_logits.size(-1)), shift_labels.view(-1))
        return loss  

    # Initialize loss and perplexity lists
    step_loss_train = []
    epoch_loss_train = []
    step_loss_val = []
    epoch_loss_val = []
    epoch_perplexity_val = []

    # Prepare the model and dataloaders with Accelerator
    accelerator = Accelerator()
    model, optimizer, train_dataloader, eval_dataloader = accelerator.prepare(
        model, optimizer, dataloaders['train'], dataloaders['val']
    )

    # Calculate the number of update steps per epoch and total training steps
    num_update_steps_per_epoch = len(train_dataloader) // 8  # Consider the gradient accumulation steps
    num_training_steps = num_epochs * num_update_steps_per_epoch

    # Define gradient accumulation steps
    gradient_accumulation_steps = 8

    # Setup the learning rate scheduler
    lr_scheduler = get_scheduler(
        name="linear",
        optimizer=optimizer,
        num_warmup_steps=1_000,
        num_training_steps=num_training_steps,
    )
    completed_steps = 0

    # Start the training loop
    for epoch in range(num_epochs):
        print(f'Epoch {epoch + 1}/{num_epochs}')
        print('-' * 10)

        # Loop over each phase: training and validation
        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()
                running_loss = 0.0  # Reset running loss for each phase
                for step, batch in tqdm(enumerate(train_dataloader, start=1), total=num_training_steps):
                    # Compute logits and loss
                    logits = model(batch["input_ids"]).logits
                    loss = ce_loss(batch["input_ids"], logits)
                    # Scale the loss for gradient accumulation
                    loss = loss / gradient_accumulation_steps
                    # Perform the backward pass and update parameters
                    accelerator.backward(loss)
                    if step % gradient_accumulation_steps == 0:
                        accelerator.clip_grad_norm_(model.parameters(), 1.0)
                        optimizer.step()
                        lr_scheduler.step()
                        optimizer.zero_grad()
                        completed_steps += 1

                    # Log the step loss and accumulate running loss
                    step_loss_train.append(loss.item())
                    running_loss += loss.item() * gradient_accumulation_steps  # Scale up the running loss

                    # Log training information
                    if step % 10 == 0:
                        print(
                            f"Step {completed_steps}, Loss: {loss.item() * gradient_accumulation_steps}, "
                            f"LR: {lr_scheduler.get_last_lr()[0]}"
                        )

                # Calculate and log epoch loss for training
                epoch_loss_train.append(running_loss / num_update_steps_per_epoch)

            else:
                model.eval()
                running_loss = 0.0  # Reset running loss for each phase
                losses = []  # Reset losses list for validation phase
                eval_progress_bar = tqdm(eval_dataloader, desc="Validation", leave=False)  # Initialize tqdm progress bar for validation
                for step, batch in enumerate(eval_progress_bar):
                    with torch.no_grad():
                        logits = model(batch["input_ids"]).logits
                        loss = ce_loss(batch["input_ids"], logits)
                        losses.append(loss)  # Record the loss for each step
                        step_loss_val.append(loss.item())  # Append the loss of each step for validation

                # Calculate and log epoch loss and perplexity for validation
                epoch_loss_in_val = torch.stack(losses).mean().item()
                epoch_loss_val.append(epoch_loss_in_val)
                try:
                    perplexity = torch.exp(torch.tensor(epoch_loss_in_val)).item()
                except OverflowError:
                    perplexity = float("inf")
                epoch_perplexity_val.append(perplexity)
                print(f'Validation Loss: {epoch_loss_in_val}, Perplexity: {perplexity}')


        # Save the model after each epoch
        accelerator.wait_for_everyone()
        unwrapped_model = accelerator.unwrap_model(model)
        if not os.path.exists(path):
            os.makedirs(path)
        unwrapped_model.save_pretrained(os.path.join(path, f'checkpoint-{epoch}'), save_function=accelerator.save)

    return {
        "epoch_loss_train": epoch_loss_train,
        "step_loss_train": step_loss_train,
        "epoch_loss_val": epoch_loss_val,
        "step_loss_val": step_loss_val,
        "epoch_perplexity_val": epoch_perplexity_val
    }
