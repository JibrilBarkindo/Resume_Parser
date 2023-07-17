from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
import os

def convert_pdf_to_txt(pdf_file_path):
    with open(pdf_file_path, 'rb') as fh:
        # Create a file handle for saving the text
        txt_file_path = pdf_file_path.replace('.pdf', '.txt')
        txt_file = open(txt_file_path, 'w', encoding='utf-8')

        # Iterate over all pages of the PDF document
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

    print("Conversion complete. The PDF file has been converted to TXT format.")

# Specify the path of the PDF file
pdf_file_path = "C:\\Users\JibrilBanu\Downloads\Halimah Banu CV APRIL 2023.pdf"

# Convert the PDF file to TXT
convert_pdf_to_txt(pdf_file_path)
print("PDF file successfully converted to TXT.")