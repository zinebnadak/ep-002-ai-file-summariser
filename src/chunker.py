#LLMs has a context limit, for claude about 200k tokens , if a 100 page document is 50k tokens its inefficient and costly to dump the whole thing at once 
#I will split on paragraph breaks (\n\n) so it does not cut mid sentance,  and summurize each chunck separateley, then combine summaries 

# test with: python3 -c "from src.chunker import chunk_text; from src.loader import load_file; text = load_file('docs/notes.md'); chunks = chunk_text(text); print(f'Number of chunks: {len(chunks)}'); print(f'First chunk: {chunks[0][:200]}')"




def chunk_text(text: str, chunk_size: int = 3000):  #default value of 3000

    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) < chunk_size:
            current_chunk += "\n\n" #new line 
        
        else:
            if current_chunk: 
                chunks.append(current_chunk.strip())
            current_chunk = paragraph + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks
            