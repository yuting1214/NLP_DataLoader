import json
from typing import List, Any

def read_fn(file_path: str) -> List[Any]:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
