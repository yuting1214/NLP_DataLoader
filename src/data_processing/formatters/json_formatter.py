from typing import List, Dict, Union, TypedDict, Optional

class ProcessedDataEntry(TypedDict):
    annotator_id: str
    feature: Union[str, List[str]]
    labels: Optional[Dict[str, Union[str, List[str]]]]

class FormattedDataEntry(TypedDict):
    raw_data: str
    processed_data: List[ProcessedDataEntry]

def format_fn(annotator_id: str,
              raw_entry: str,
              labels: Optional[Dict[str, Union[str, List[str]]]],
              processed_text_data: List[str]) -> FormattedDataEntry:
    """
    Format the processed data entry with annotations into the desired output structure.

    :param annotator_id: A unique identifier for the annotator.
    :param raw_entry: The original data entry from the raw data.
    :param labels: A dictionary of labels assigned by the annotator function.
    :param processed_text_data: The processed text data as a list of strings.
    :return: A dictionary in the desired output format.
    """
 
    # Prepare the processed data structure
    if labels != None:
        processed_data = {
            "annotator_id": annotator_id,
            "feature": processed_text_data,
            "labels": labels
        }
    else:
        processed_data = {
            "annotator_id": annotator_id,
            "feature": processed_text_data,
        }     

    # Prepare the final structure
    formatted_entry = {
        "raw_data": raw_entry,
        "processed_data": [processed_data]  # Wrapping the processed data in a list
    }

    return formatted_entry
