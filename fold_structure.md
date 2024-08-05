project-root/
│
├── data/
│   ├── raw/
│   │   └── ESConv.json
│   │
│   └── formatted/
│       └── ESConv_processed.json
│
├── src/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── download_data.py
│   │   └── time_utils.py
│   │
│   ├── data_processing/
│   │   ├── __init__.py
│   │   ├── readers/
│   │   │   ├── __init__.py
│   │   │   ├── json_reader.py
│   │   │   ├── csv_reader.py (TBD)
│   │   │   └── xml_reader.py (TBD)
│   │   │
│   │   ├── label_annotator/
│   │   │   ├── __init__.py
│   │   │   ├── heuristic_annotator.py
│   │   │   ├── human_labor.py (TBD)
│   │   │   └── ml_method.py (TBD)
│   │   │
│   │   ├── processors/
│   │   │   ├── __init__.py
│   │   │   ├── language_model_processor.py
│   │   │   └── classification_processor.py
│   │   │
│   │   ├── formatters/
│   │   │   ├── __init__.py
│   │   │   ├── json_formatter.py
│   │   │   ├── csv_formatter.py (TBD)
│   │   │   └── xml_formatter.py (TBD)
│   │   │
│   │   ├── label_manager.py (TBD)
│   │   └── data_processing_pipeline.py
│   │
│   ├── model_training/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   └── trainer.py
│   │
│   └── model_inference/
│       ├── __init__.py
│       └── closest_pair_finder.py
│
├── paper/ # reference paper for [Emotional-Support-Conversation dataset]
│
├── model/ # Store pretrained and self-trained models
|
├── docta_tech_assessment_MLE.ipynb # Takehome problem
|
└── demo.ipynb # Demonstration for the usage of the project
