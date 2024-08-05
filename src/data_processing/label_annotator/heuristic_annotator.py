from typing import List, Dict, Union, Tuple, Callable

# Define a common type for the annotation functions.
AnnotationFunction = Callable[[Dict], Tuple[str, Dict[str, Union[str, List[str]]]]]

def extract_supporter_strategy(data: Dict) -> Tuple[str, Dict[str, Union[str, List[str]]]]:
    annotator_id = 'heuristic_supporter_strategy'
    label_key = 'strategy'
    strategies = []

    for turn in data['dialog']:
        if turn['speaker'] == 'supporter' and 'strategy' in turn['annotation']:
            strategies.append(turn['annotation']['strategy'])

    return (annotator_id, {label_key: strategies})

def extract_user_emotion(data: Dict) -> Tuple[str, Dict[str, Union[str, List[str]]]]:
    annotator_id = 'heuristic_user_emotion'
    label_key = 'emotion_type'
    emotion = data['emotion_type']

    return annotator_id, {label_key: emotion}

def extract_conversation_situation(data: Dict) -> Tuple[str, Dict[str, Union[str, List[str]]]]:
    annotator_id = 'heuristic_situation'
    label_key = 'situation'
    situation = data['situation']

    return annotator_id, {label_key: situation}

def extract_subconversation_feedback(data: Dict) -> Tuple[str, Dict[str, Union[str, List[str]]]]:
    annotator_id = 'heuristic_subconversation_feedback'
    label_key = 'feedback'
    feedbacks = []
    for turn in data['dialog']:
        if 'feedback' in turn['annotation']:
            feedbacks.append(int(turn['annotation']['feedback']))

    return (annotator_id, {label_key: feedbacks})

def annotate_dialog(data: Dict) -> Tuple[str, Dict[str, None]]:
    annotator_id = 'heuristic_subconversation_feedback'
    return (annotator_id, None)