# read a file and return plain text 
# takes a filepath, figures out what type of file it is, reads it using the right library (.txt or .md using pythons built-in open(), .pdf with pypdf and .docx with docx), and returns plain text
# i the file ends with something else it raises an error
# test with: python3 -c "from src.loader import load_file;print(load_file('samples/sample.txt'))"


from pathlib import Path                                                        # pathlib module handles filepaths as objects rather than strings like os does. We import Path object

def load_file(file_path: str) -> str:                                           #take a filepath as a string and return the plain text content of that file as a string
    path = Path(file_path)                                                      # the Path object takes a variable inputted by the user (a file path) and assigns it to a function variable path
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    suffix = path.suffix.lower()

    if suffix in (".txt", ".md"):
        return path.read_text(encoding = "utf-8")                               #always specify UTF-8 when reading text files  so that the code works the same on every computer. Default on Mac is UTF-8 anyway

    if suffix == ".pdf":
        from pypdf import PdfReader
        reader = PdfReader(str(path))
        pages = [page.extract_text() or "" for page in reader.pages]        #go through every page, pull out the text, or "" is used instead of crashing
        return "\n\n".join(pages)                                           #join all pages with a blank line between each

    if suffix == ".docx":
        from docx import document
        doc = Document(str(path))
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]         #keep paragraphs that are not empty
        return "\n\n".join(paragraphs)
        

    raise ValueError (f"Unsupported file type: '{suffix}'")
    print(load_file("sample.txt"))