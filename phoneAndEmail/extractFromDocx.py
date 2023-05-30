'''import docx2txt
import spacy

personsName = []

def extract_text_from_doc(doc_path):
    temp = docx2txt.process(doc_path)
    text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
    #print(text)
    return ' '.join(text)

doc_path = "C:\\Users\\MichalAleksanderek\\Documents\\Month0423\\pythonTesting\\cvDoc.docx"
text = extract_text_from_doc(doc_path)

english_nlp = spacy.load('en_core_web_sm')
spacy_parser = english_nlp(text)

for entity in spacy_parser.ents:
    #print(f'Found: {entity.text} of type: {entity.label_}')
    if entity.label_ == "PERSON":
        personsName.append(entity.text)

print(personsName)
'''

import io
import re
import phonenumbers
import spacy
import boto3
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.high_level import extract_text
import docx2txt













# Regex for emails and saves emails to text file
def extract_email(cv_text):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_regex, cv_text)
    emailFile = open("C:\\Users\\MichalAleksanderek\\Documents\\Month0423\\pythonTesting\\emailsExtracted.txt", "w")
    for email in emails:
        emailFile.write("%s\n" % email)
    #emailFile.close()
    return emails

# Regex for phone numbers
def extract_phone_number(cv_text):
    numbers = phonenumbers.PhoneNumberMatcher(cv_text, "IN")
    phoneFile = open("C:\\Users\\MichalAleksanderek\\Documents\\Month0423\\pythonTesting\\phoneNumbersExtracted.txt", "w")
    for number in numbers:
        phone_number_str = str(number.number)
        print(phone_number_str)
        phoneFile.write(phone_number_str + "\n")
    #phoneFile.close()
    return numbers






# Print all of the pdf data into a txt file
def pdf_to_txt(input_path, output_path):
    text = extract_text(input_path)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)
input_file = "C:\\Users\\MichalAleksanderek\\Documents\\Month0423\\pythonTesting\\data\\data\\ACCOUNTANT\\01789.pdf"
output_file = "C:\\Users\\MichalAleksanderek\\Documents\\Month0423\\pythonTesting\\pdfData.txt"
pdf_to_txt(input_file, output_file)

# Extract text from DOCX file
def docx_to_txt(input_path, output_path):
    text = docx2txt.process(input_path)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)
input_file = "C:\\Users\\MichalAleksanderek\\Documents\\Month0423\\pythonTesting\\Test CVs\\Abigail Welling.docx"
output_file = "C:\\Users\\MichalAleksanderek\\Documents\\Month0423\\pythonTesting\\docxData.txt"
docx_to_txt(input_file, output_file)

# Extract text from PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as fh:
        # iterate over all pages of PDF document
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            # creating a resoure manager
            resource_manager = PDFResourceManager()
            
            # create a file handle
            fake_file_handle = io.StringIO()
            
            # creating a text converter object
            converter = TextConverter(
                                resource_manager, 
                                fake_file_handle, 
                                codec='utf-8', 
                                laparams=LAParams()
                        )

            # creating a page interpreter
            page_interpreter = PDFPageInterpreter(
                                resource_manager, 
                                converter
                            )

            # process current page
            page_interpreter.process_page(page)
            
            # extract text
            text = fake_file_handle.getvalue()
            yield text

            # close open handles
            converter.close()
            fake_file_handle.close()

english_nlp = spacy.load('en_core_web_lg')

# calling above function and extracting text
#for page in extract_text_from_pdf("C:\\Users\\MichalAleksanderek\\Documents\\Month0423\\pythonTesting\\data\\data\\ACCOUNTANT\\01789.pdf"):
    #text = ' ' + page

# Process PDF file
def process_pdf_file(file_path):
    output_file = "C:\\Users\\MichalAleksanderek\\Documents\\Month0423\\pythonTesting\\pdfData.txt"
    pdf_to_txt(file_path, output_file)
    with open(output_file, 'r') as file:
        cv_text = file.read()

        emails = extract_email(cv_text)
        phone_numbers = extract_phone_number(cv_text)

        print("Emails:", emails)
        print("Phone Numbers:", phone_numbers)

        return cv_text

# Process DOCX file
def process_docx_file(file_path):
    output_file = "C:\\Users\\MichalAleksanderek\\Documents\\Month0423\\pythonTesting\\docxData.txt"
    docx_to_txt(file_path, output_file)
    with open(output_file, 'r') as file:
        cv_text = file.read()

        emails = extract_email(cv_text)
        phone_numbers = extract_phone_number(cv_text)

        print("Emails:", emails)
        print("Phone Numbers:", phone_numbers)

        return cv_text

docType = "Pdf"

#Print out phone numbers and emails
if docType == "Docx":
    with open("C:\\Users\\MichalAleksanderek\\Documents\\Month0423\\pythonTesting\\docxData.txt", 'r') as file:
        cv_text = file.read()

        emails = extract_email(cv_text)
        phone_numbers = extract_phone_number(cv_text)

        print("Emails:", emails)
        print("Phone Numbers:", phone_numbers)

elif docType == "Pdf":
    with open("C:\\Users\\MichalAleksanderek\\Documents\\Month0423\\pythonTesting\\pdfData.txt", 'r') as file:
        cv_text = file.read()

        emails = extract_email(cv_text)
        phone_numbers = extract_phone_number(cv_text)

        print("Emails:", emails)
        print("Phone Numbers:", phone_numbers)