import spacy
import os

# Load the pre-trained model
english_nlp = spacy.load("C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Resume_Parser\Training_AI\JSON Files\Training_JSON\\Name_email_referencesv3\\model-best")

# Folder path containing the files
folderpath = "C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\\txt files\_txt files_formatted"

# Get the list of file names in the folder
file_names = os.listdir(folderpath) 

# Iterate over each file in the folder
for file_name in file_names:
    # Construct the full file path
    file_path = os.path.join(folderpath, file_name)

    # Open the file and read its contents
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Process the text with the pre-trained model
    spacy_parser = english_nlp(text)

    # Iterate over the entities and print the results
    for entity in spacy_parser.ents:
        print(f'Found: {entity.text} of type: {entity.label_}')
