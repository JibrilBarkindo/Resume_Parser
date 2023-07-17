import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams  # Add this import statement
import spacy

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as fh:
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle, codec='utf-8', laparams=LAParams())
        page_interpreter = PDFPageInterpreter(resource_manager, converter)
        
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
            
            text = fake_file_handle.getvalue()
            yield text
        
        converter.close()
        fake_file_handle.close()

english_nlp = spacy.load("C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Resume_Parser\Training_AI\JSON Files\Eval_JSON\\Name_email_references\model-name_email_reference")

pdf_path = "C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Test CV'S\other data\Matthew Evans.pdf"

# Extract text from the PDF
for page in extract_text_from_pdf(pdf_path):
    text = ' ' + page

# Process the text with spaCy
spacy_parser = english_nlp(text)

# Print the entities found
for entity in spacy_parser.ents:
    print(f'Found: {entity.text} of type: {entity.label_}')
