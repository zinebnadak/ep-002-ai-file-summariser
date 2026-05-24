from pathlib import Path 

file_path = Path("documents/myfile.PDF")
print(file_path.suffix)
print(file_path.name)
print(file_path.parent)
print(file_path.exists())

file_path_2 = Path("notes.md")
print()
print(file_path_2.suffix)
print(file_path_2.name)
print(file_path_2.parent)
print(file_path_2.exists())