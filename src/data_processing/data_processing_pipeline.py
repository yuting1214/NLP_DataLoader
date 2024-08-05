import json
import multiprocessing as mp
from typing import Callable, List, Dict, Any, Tuple
from tqdm import tqdm

class DataEntry:
    def __init__(self, raw_data: str, processed_data: List[Dict[str, Any]]):
        self.raw_data = raw_data
        self.processed_data = processed_data

class DataProcessingPipeline:
    def __init__(self, read_fn: Callable):
        self.read_fn = read_fn
        self.entries = []

    def process_data(self, annotate_fn_list: List[Callable], process_fn: Callable, format_fn: Callable):
        # Step 1: Read Data
        raw_data_list = self.read_fn()

        # Loop through each entry in the raw data
        for raw_entry in raw_data_list:
            # Initialize the list to hold formatted data from different annotators
            formatted_entries = []

            # Step 2: Annotate and Process Data
            for annotate_fn in annotate_fn_list:
                annotator_id, labels = annotate_fn(raw_entry)
                # Step 3: Process annotated data
                processed_text_data = process_fn(raw_entry)

                # Step 4: Format the processed data into the desired structure for each annotator
                formatted_entry = format_fn(annotator_id, raw_entry, labels, processed_text_data)
                formatted_entries.append(formatted_entry['processed_data'][0])  # Extract the single processed data entry

            # Aggregate all formatted data entries for this raw entry
            aggregated_entry = {
                "raw_data": raw_entry,
                "processed_data": formatted_entries
            }

            self.entries.append(aggregated_entry)

        return self

    def __getitem__(self, index):
        return self.entries[index]

    def __len__(self):
        return len(self.entries)

    def save(self, filepath: str):
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.entries, f, indent=4)