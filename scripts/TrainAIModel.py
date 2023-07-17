import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json
import os

# Load a new blank spacy model
nlp = spacy.load("C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\AIModelShowcase\\SpecificModel\\model-name_email_refv2")
# Create a DocBin object for storing Doc objects
db = DocBin()

# Folder path containing the training JSON files
folderpath = "C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Resume_Parser\Training_AI\JSON Files\Training_JSON\\Name_email_referencesv3"
# Get a list of file names in the folder
file_names = os.listdir(folderpath)

# Process each training data file
for file_name in file_names:
    file_path = os.path.join(folderpath, file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            TRAIN_DATA = json.load(f)
    except UnicodeDecodeError:
        print(f"Skipping file: {file_name}. Invalid start byte error.")
        continue
       
    # Iterate over the text and annotations in the training data
    for text, annot in tqdm(TRAIN_DATA['annotations']):
        # Create a Doc object from the text
        doc = nlp.make_doc(text)
        ents = []
        # Extract named entities from the annotations and add them to the Doc object
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents
        # Add the Doc object to the DocBin
        db.add(doc)

# Save the training data in readable spacy binary format
db.to_disk("./Train_specific_model.spacy")

# Folder path containing the evaluation JSON files
evalfolderpath = "C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Resume_Parser\Training_AI\JSON Files\Eval_JSON\\Name_email_references"
# Get a list of file names in the folder
eval_data_files = os.listdir(evalfolderpath)

# Process each evaluation data file
for eval_file in eval_data_files:
    eval_file_path = os.path.join(evalfolderpath, eval_file)
    try:
        with open(eval_file_path, 'r', encoding='utf-8') as f:
            eval_data = json.load(f)
            if not eval_data:  # Skip empty files
                print(f"Skipping empty file: {eval_file}")
                continue
    except (UnicodeDecodeError, json.JSONDecodeError):
        print(f"Skipping badly formatted file: {eval_file}")
        continue
    # Iterate over the text and annotations in the evaluation data
    for text, annot in tqdm(eval_data['annotations']):
        # Create a Doc object from the text
        doc = nlp.make_doc(text)
        ents = []
        # Extract named entities from the annotations and add them to the Doc object
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents
        # Add the Doc object to the DocBin
        db.add(doc)

# Save the evaluation data as a serialized file
db.to_disk("./eval_specific_model.spacy")