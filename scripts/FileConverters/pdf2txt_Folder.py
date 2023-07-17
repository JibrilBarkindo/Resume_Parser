from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
import os
import glob

def convert_folder_to_txt(folder_path):
    # Get a list of PDF files in the folder
    pdf_files = glob.glob(os.path.join(folder_path, '*.pdf'))

    # Iterate over each PDF file
    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as fh:
            # Create a file handle for saving the text
            txt_file_path = pdf_file.replace('.pdf', '.txt')
            txt_file = open(txt_file_path, 'w', encoding='utf-8')

            # Iterate over all pages of PDF document
            for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                # Create a resource manager
                resource_manager = PDFResourceManager()

                # Create a file handle
                fake_file_handle = io.StringIO()

                # Create a text converter object
                converter = TextConverter(
                    resource_manager,
                    fake_file_handle,
                    codec='utf-8',
                    laparams=LAParams()
                )

                # Create a page interpreter
                page_interpreter = PDFPageInterpreter(
                    resource_manager,
                    converter
                )

                # Process current page
                page_interpreter.process_page(page)

                # Extract text
                text = fake_file_handle.getvalue()
                txt_file.write(text)  # Write the text to the file

                # Close open handles
                converter.close()
                fake_file_handle.close()

            txt_file.close()  # Close the TXT file handle

    print("Conversion complete. PDFs in the folder have been converted to TXT format.")

# Calling the function and converting the folder to TXT
folder_path = "C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Test CV'S\Kaggle_data\ENGINEERING"
convert_folder_to_txt(folder_path)
print("pdf folder successfully converted")