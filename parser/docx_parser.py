import docx

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join(para.text for para in doc.paragraphs)
