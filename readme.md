## Task: Reformat a public dataset.

### Objective

To enhance the suitability of public datasets for LLM (Large Language Model) training and fine-tuning, datasets need to be presented in a consistent, structured format. Your responsibility is to conceive and implement a data format, then modify a given public dataset to adhere to this new structure.

### Detailed Instructions:

1. **Dataset Selection**: 

   - You may start with the [Emotional-Support-Conversation dataset](https://raw.githubusercontent.com/thu-coai/Emotional-Support-Conversation/main/ESConv.json) for this task. But you are encouraged to use other public datasets as long as specific reasons are given.

   - This dataset doesn't inherently have "labels". Your task includes crafting at least one appropriate label key and annotating the data accordingly.
   
   - When designing labels, ensure they align with the principles of making the LLM harmless, helpful, and honest.

2. **Dataset Attributes**:
   - Your reformatted dataset should includes at least two attributes: `raw_data` and `processed_data`.

     - `raw_data`: A string, which directly saves the raw text data loaded from the original dataset
     
     - `processed_data`: A list where each item signifies a feature-label pair that's been processed for a specific task. For clarity, refer to the examples provided in the block below.

3. **Flexibility in Design**:

   - **Data Structure**: Your design should be accommodating. This means:
   
     - Simplifying the addition of new processed data.

     - Expanding the label classes without hassle (i.e., introducing new label keys).

     - Incorporating label values from various annotators (i.e., multiple label values from different annotators for the same label key).
     
   - **Code Flexibility**: Ensure your code is modular, making it straightforward to apply the same formatting to other public datasets.


4. **Design Autonomy**: 

   - While the example below offers guidance, don't feel restricted by it. If you believe a different structure is more suitable, present your unique design. However, ensure that it incorporates the essential attributes: `raw_data` and `processed_data`.
   
5. **Deliverables**:

   - An outline of your designed data format/structure.

   - The code used to convert the public dataset to your design.

   - Print the time cost for saving and loading your designed dataset, specifically,

     - Time cost for saving the whole dataset

     - Time cost for loading the whole dataset
     
     - Time cost for loading randomly selected 1k instances from the dataset.
   

   - Model Inference

     - Select a Language Model: Choose a language model of your preference. For instance, you can use a pretrained model available from HuggingFace transformers.

     - Generate Embeddings:  Utilize the selected model to generate embeddings for your processed data. You only need to obtain embeddings for a sample of 100 instances.

     - Find the Closest Pair: Identify the pair of instances with the closest embeddings.

     - Display the Instances: Print or display the instances for review.

   - **Model Training (Bonus)**

      - Select a Language Model: Choose a language model of your preference. For instance, you can use a pretrained model available from HuggingFace transformers.

      - Fine-tune the Model: Finetune the pretrained model using your processed data with a training-to-test data split ratio of 7:3. 

         - You can use a subset of your processed data if the computing resource is limited.
         
         - The task for fine-tuning could be classification, generation, or embedding improvement. 

      - Display Training Log: print the training log, which should includes essential information including the training loss and test loss.



**Please finish this task in one week. You can return .py or .ipynb files.**