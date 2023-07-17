import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json
import os

nlp = spacy.load("C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Resume_Parser\Training_AI\JSON Files\model-best")  # load a new spacy model
db = DocBin()  # create a DocBin object


folderpath = "C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Resume_Parser\Training_AI\JSON Files\Training_JSON\Phone_And_Email"
file_names = os.listdir(folderpath)  # get a list of file names in the folder

for file_name in file_names:
    file_path = os.path.join(folderpath, file_name)
    with open(file_path, 'r',encoding='utf-8') as f:
        TRAIN_DATA = json.load(f)
       
   
    for text, annot in tqdm(TRAIN_DATA['annotations']):
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)

      
new_data = "C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Resume_Parser\Training_AI\JSON Files\Training_JSON\Contact_Info_and_Name"
file_names2 = os.listdir(new_data)

for file_name in file_names2:
    file_path = os.path.join(new_data, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        TRAIN_DATA = json.load(f)

    for text, annot in tqdm(TRAIN_DATA['annotations']):
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)


db.to_disk("./merged_training_data.spacy")  # save the docbin object

existing_eval_data = "C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Resume_Parser\Training_AI\JSON Files\Eval_JSON\contact_info_and_Name"
eval_data_files = os.listdir(existing_eval_data)

for eval_file in eval_data_files:
    eval_file_path = os.path.join(existing_eval_data, eval_file)
    with open(eval_file_path, 'r',encoding='utf-8') as f:
        eval_data = json.load(f)

    for text, annot in tqdm(eval_data['annotations']):
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)


new_eval_data = "C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Resume_Parser\Training_AI\JSON Files\Eval_JSON\phone_and _email"
eval_data_files = os.listdir(new_eval_data)

for eval_file in eval_data_files:
    eval_file_path = os.path.join(new_eval_data, eval_file)
    with open(eval_file_path, 'r',encoding='utf-8') as f:
        eval_data = json.load(f)

    for text, annot in tqdm(eval_data['annotations']):
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents



db.to_disk("./merged_eval_data.spacy")

#get config file using:   python -m spacy init config config.cfg --lang en --pipeline ner --optimize accuracy

#Train model in cli using: python -m spacy train config.cfg --output ./ --paths.train ./training_data3.spacy --paths.dev ./eval_data3.spacy 
