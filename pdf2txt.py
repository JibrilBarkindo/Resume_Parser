from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
import spacy


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as fh:
        # create a file handle for saving the text
        txt_file_path = pdf_path.replace('.pdf', '.txt')
        txt_file = open(txt_file_path, 'w', encoding='utf-8')
        
        # iterate over all pages of PDF document
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            # creating a resource manager
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
            txt_file.write(text)  # write the text to the file

            # close open handles
            converter.close()
            fake_file_handle.close()
        
        txt_file.close()  # close the TXT file handle

# calling the function and extracting text
pdf_path = "C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\data\data\FINANCE\\10.pdf"
extract_text_from_pdf(pdf_path)
print("Text extracted and saved to a TXT file.")
