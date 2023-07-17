import spacy
from docx import Document



def extract_text_from_doc(doc_path):
    document = Document(doc_path)
    text = [paragraph.text for paragraph in document.paragraphs]
    return ' '.join(text)

def save_file_as_text(doc_path, text_path):
    text = extract_text_from_doc(doc_path)
    with open(text_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

def extract_named_entities(text):
    english_nlp = spacy.load("C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Resume_Parser\Training_AI\JSON Files\Training_JSON\\Name_email_referencesv2\model-name_email_refv2")
    spacy_parser = english_nlp(text)

    named_entities = []
    for entity in spacy_parser.ents:
        named_entities.append((entity.text, entity.label_))
    
    return named_entities

doc_path = "C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Test CV'S\CVs danCoady\James Smith.docx"
text_path = "C:\\Users\\JibrilBanu\\Documents\\GitHub\\CV_Parser\\txt files\\testingFile.txt"

# Convert DOCX to TXT
save_file_as_text(doc_path, text_path)

# Extract named entities from the text
with open(text_path, 'r', encoding='utf-8') as file:
    text_content = file.read()

named_entities = extract_named_entities(text_content)

# Print the named entities
for entity, label in named_entities:
    print(f'Found: {entity} of type: {label}')
