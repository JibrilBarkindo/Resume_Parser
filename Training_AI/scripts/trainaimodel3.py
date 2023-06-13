import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json
import os

nlp = spacy.blank("en")  # load a new spacy model
db = DocBin()  # create a DocBin object

folderpath = "C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Resume_Parser\Training_AI\JSON_CV_files"
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

      
      

db.to_disk("./training_data3.spacy")  # save the docbin object

evalfolderpath = "C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Resume_Parser\Training_AI\Json_Eval_files"
eval_data_files = os.listdir(evalfolderpath)

for eval_file in eval_data_files:
    eval_file_path = os.path.join(evalfolderpath, eval_file)
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

db.to_disk("./eval_data3.spacy")
