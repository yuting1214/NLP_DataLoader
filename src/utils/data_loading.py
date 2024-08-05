import json
import random
from typing import List, Any

def load_processed_data(file_path: str) -> Any:
    """
    Load the processed data from a JSON file.

    :param file_path: Path to the file to be read.
    :return: The content of the file, typically a list or a dictionary.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def load_random_sample(file_path: str, sample_size: int = 1000) -> List[Any]:
    """
    Load a random sample of instances from a JSON file.

    :param file_path: Path to the JSON file containing the dataset.
    :param sample_size: The number of instances to randomly sample from the dataset.
    :return: A list containing the randomly sampled instances.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # If the file contains a list of instances
    if isinstance(data, list):
        if sample_size > len(data):
            raise ValueError("Sample size cannot be greater than the total number of instances in the dataset.")
        random_sample = random.sample(data, sample_size)
    else:
        raise TypeError("The dataset should be a list of instances.")

    return random_sample