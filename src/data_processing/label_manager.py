# data_processing/label_manager.py

class LabelManager:
    def __init__(self):
        self.labels = {}

    def add_labels(self, key: str, values: list):
        """Add or update labels for a given key."""
        if key in self.labels:
            self.labels[key].extend(values)
        else:
            self.labels[key] = values

    def get_labels(self, key: str) -> list:
        """Retrieve labels for a given key."""
        return self.labels.get(key, [])

    def add_annotator_labels(self, key: str, annotator: str, values: list):
        """Add or update labels from a specific annotator for a given key."""
        if key not in self.labels:
            self.labels[key] = {}
        
        if annotator in self.labels[key]:
            self.labels[key][annotator].extend(values)
        else:
            self.labels[key][annotator] = values

    def get_annotator_labels(self, key: str, annotator: str) -> list:
        """Retrieve labels from a specific annotator for a given key."""
        return self.labels.get(key, {}).get(annotator, [])
