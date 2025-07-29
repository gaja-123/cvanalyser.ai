from pypdf import PdfReader

def extract_text_from_pdf(pdf_doc):
    pdf= PdfReader(pdf_doc) # read index,page details
    
    raw_text = ""
    for index,page in enumerate(pdf.pages):
        raw_text += page.extract_text() # extract text from each page
    return raw_text
    