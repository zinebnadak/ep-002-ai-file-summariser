# This is another function i made: 
# load_file takes a file_path variable as input
# checks if it exists
# detects the file type 
# extracts the text from document then returns all text as a string. 

from pathlib import Path                                                    # pathlib module handles filepaths as objects rather than strings like os does. We import Path object

def load_file(file_path: str) -> str:                                  
    path = Path(file_path)                           
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    suffix = path.suffix.lower()

    if suffix in (".txt", ".md"):
        return path.read_text(encoding = "utf-8")                           #always specify UTF-8 when reading text files  so that the code works the same on every computer. Default on Mac is UTF-8 anyway

    if suffix == ".pdf":
        from pypdf import PdfReader
        reader = PdfReader(str(path))
        pages = [page.extract_text() or "" for page in reader.pages]        #go through every page, pull out the text, or "" is used instead of crashing
        return "\n\n".join(pages)                                           #join all pages with a blank line between each

    if suffix == ".docx":
        from docx import document
        doc = Document(str(path))
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]     #keep paragraphs that are not empty
        return "\n\n".join(paragraphs)
        

    raise ValueError (f"Unsupported file type: '{suffix}'")

'''
Test: 
OBS! If you are inside the folder src, go up one directory: 
print(load_file("../samples/sample.txt"))

Or run from project root:
print(load_file("samples/sample.txt"))
'''
