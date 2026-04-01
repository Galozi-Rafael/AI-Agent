import os
from config import DOCS_FOLDER

def list_documents():
    
    if not os.path.exists(DOCS_FOLDER):
        return []
    
    files = []

    for file_name in os.listdir(DOCS_FOLDER):
        if file_name.endswith('.txt'):
            files.append(file_name)
    
    return files

def read_document(file_name):
    file_path = os.path.join(DOCS_FOLDER, file_name)
    
    if not os.path.exists(file_path):
        return None
    
    with open(file_path, "r", encoding='utf-8') as file:
        return file.read()