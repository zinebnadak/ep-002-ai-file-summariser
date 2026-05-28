# LLMs has a context limit, for claude about 200k tokens , if a 100 page document is 50k tokens its inefficient and costly to dump the whole thing at once 
# A function chunk_text takes a whole document content as a string, and a default chunksize of 3000 chars
# I will split the string into sections as elements in a list where there is a empty line ("\n\n")
# chuncks can be added together but not so they exceed the chunk_size limit 
# each item in the list chunks is less than 3000 chars 

def chunk_text(text: str, chunk_size: int = 3000):  #default limit of 3000 chars

    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) <= chunk_size:
            if current_chunk:   #if it is not empty
                current_chunk += "\n\n" + paragraph
            else:
                current_chunk = paragraph
       
        else:
            if current_chunk:   #if it is not empty
                chunks.append(current_chunk.strip())
            
            current_chunk = paragraph + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks
'''
Test:
OBS! Run from project root: 

from loader import load_file
text = load_file("samples/sample.txt")
print(chunk_text(text, 50))
'''



