# read a file and return plain text 
# takes a filepath, figures out what type of file it is, reads it using the right library (.txt or .md using pythons built-in open(), .pdf with pypdf and .docx with docx), and returns plain text
# i the file ends with something else it raises an error


from pathlib import Path    # pathlib module handles filepaths as objects rather than strings like os does. We import Path object

def load_file(file_path: str) -> str:   #take a filepath as a string and return the plain text content of that file as a string
    path = Path(file_path)              # the Path object takes a variable inputted by the user (a file path) and assigns it to a function variable path
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    suffix = path.suffix.lower()

    if suffix in (".txt", ".md"):
        return path.read_text(encoding = "utf-8") #always specify UTF-8 when reading text files  so that the code works the same on every computer. Default on Mac is UTF-8 anyway

    if suffix == ".pdf":
        from pypdf import PdfReader
    
    if suffix == ".docx":
        from docx import document
        

    raise ValueError (f"Unsupported file type: '{suffix}'")



print(load_file("notes.md"))