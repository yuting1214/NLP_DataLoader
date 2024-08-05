import random
from datasets import DatasetDict, Dataset

def split_data(input_data, train_ratio=0.7, shuffle=True):
    if shuffle:
        # Shuffle the input data randomly
        random.shuffle(input_data)
    
    target_input = [item['processed_data'][0]['feature'] for item in input_data]
    # Calculate the split index
    split_index = int(len(target_input) * train_ratio)
    
    # Split the data into training and evaluation sets
    train_data = target_input[:split_index]
    eval_data = target_input[split_index:]
    
    # Create dictionaries with "feature" key and the split lists as values
    train_set = Dataset.from_dict({"feature": train_data})
    eval_set = Dataset.from_dict({"feature": eval_data})
    
    return train_set, eval_set

def tokenize(element, tokenizer):
    context_length = 128

    outputs = tokenizer(
        element["feature"],
        truncation=True,
        max_length=context_length,
        return_overflowing_tokens=True,
        return_length=True,
    )
    input_batch = []
    for length, input_ids in zip(outputs["length"], outputs["input_ids"]):
        if length == context_length:
            input_batch.append(input_ids)
    return {"input_ids": input_batch}

def sample_data(input_data, sample_size=100, shuffle=True):
    if shuffle:
        # Shuffle the input data randomly
        random.shuffle(input_data)
    
    target_input = [item['processed_data'][0]['feature'] for item in input_data]
    
    return target_input[:sample_size]