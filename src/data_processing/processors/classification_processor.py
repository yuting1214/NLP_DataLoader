from typing import List, Dict, Union, Tuple, Callable

# Define a common type for the processing functions.
ProcessingFunction = Callable[[Dict], Union[str, List[str]]]

def get_supporter_responses(data: dict) -> List[str]:
    responses = []
    
    for turn in data['dialog']:
        if turn['speaker'] == 'supporter' and 'strategy' in turn['annotation']:
            responses.append(turn['content'])
    
    return responses

def get_dialogue(data: dict) -> str:
    dialogue = " ".join([turn['content'].replace('\n', ' ') for turn in data['dialog']])

    return dialogue

def get_subconversation(data: dict) -> List[str]:
    sub_conversations = []
    current_sub_conversation = []

    for turn in data['dialog']:
        current_sub_conversation.append(turn['content'])
        
        if 'feedback' in turn['annotation']:
            sub_conversations.append(" ".join(current_sub_conversation))
            current_sub_conversation = []
    return sub_conversations