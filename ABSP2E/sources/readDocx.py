import docx


def getText(file_name):
    doc = docx.Document(file_name)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)
