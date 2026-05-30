# Takes the list of chunks from chunker.py and sends each one to an LLM and gets a structured summary (key point and main idea) for each chunk
# Then synthesises everything so takes all those key points together and sends to LLM one more time to and put it into one final "FileSummary"

from anthropic import Anthropic
from openai import OpenAI
from dotenv import load_dotenv
from models import ChunkSummary, FileSummary, Section # my three classes so we can validate the LLMs response
import json  #the LLM returns a JSON

load_dotenv()

chunk_prompt = """
Read this chunk of text and return JSON only with these fields:
- main_concept: one sentence summary
- key_points: list of 3-5 main points
- keywords: list of 5-10 important terms

Return valid JSON only. No markdown, no code fences, no backticks. Raw JSON only.

Chunk:
{chunk_text}    
"""
# {chunk_text} so I can use format later like: chunk_prompt.format(chunk_text=chunk) , chunk one at a time 


synthesis_prompt = """
Here are key points extracted from all chunks of a document.
Synthesise them into a final summary.

Return JSON only with these fields:
- title: short descriptive title for the document
- overview: 2-3 sentence summary of the whole document
- key_sections: list of sections, each with section_title and summary

Return valid JSON only. No markdown, no code fences, no backticks. Raw JSON only.

Key points:
{all_points}
"""

#this function will call the API and return raw text
def call_llm (provider: str, prompt: str) -> str:            # the provider argument will be taken from the terminal as user input later 
    if provider == "anthropic":
        client = Anthropic()
        message = client.messages.create(
            system = "" ,       # system prompt here
            model = "claude-haiku-4-5",
            max_tokens = 1024,
            messages = [
                {"role": "user", "content": prompt}    # one of our prompts here
                ]
            )
        return message.content[0].text
    

    if provider == "openai":
        client = OpenAI()
        response = client.responses.create(
            instructions = "",             #the system prompt does not work! WHY?
            model = "gpt-4o-mini",
            max_output_tokens= 1024, 
            input = [
                {"role":"user","content":prompt}
                ]
            )
        return response.output[0].content[0].text
    
    raise ValueError(f"Unknown provider: {provider}")

'''
Test 
Print the whole message object to know where to drill:
print(call_llm ("anthropic", chunk_prompt)) 

anthropic_response = print(message.content[0].text)
    return anthropic_response

openai_response = print(response.output[0].content[0].text)
    return openai_response
'''  
        

#this function will parse the text into structured data and validate it using our models.py
def summarise(chunks: list[str], provider: str) -> FileSummary:

    # fill in the "{chunk_text}" in chunk_prompt chunk by chunk
    chunk_summaries = []
    print(f"\nSummarizing {len(chunks)} chunk(s) using {provider}... \n")   #process indicator

    for i, chunk in enumerate(chunks): # enumerate gives both index adn chunk value
        print(f"Chunk {i+1}/{len(chunks)}...")  #process indicator
        complete_chunk_prompt = chunk_prompt.format(chunk_text=chunk)
        raw = call_llm(provider,complete_chunk_prompt)    # we will get a raw string response we need to convert to a dict using json
        raw = raw.strip().removeprefix("```json").removesuffix("```").strip()
        data = json.loads(raw)
        chunk_summaries.append(ChunkSummary(**data))    # validate the data using pydantic class we made, ** lets us create a ChunkSummay object (for the Pydantic class) from that json dict we loaded, with ** python unpacks the dict into named arguments


    # fill in the "{all_points}" in synthesis_prompt after with all the chunk_summaries
    all_points_list = []
    for c in chunk_summaries:
        all_points_list.extend(c.key_points) # key_points is now a list of strings from our ChunkSummary class

    print("\nSynthesising final summary...")    #process indicator
    complete_synthesis_prompt = synthesis_prompt.format(
        all_points = "\n".join(f"- {point}" for point in all_points_list)    #building the complete_synthesis_prompt neatly
    )
    raw = call_llm(provider, complete_synthesis_prompt)
    raw = raw.strip().removeprefix("```json").removesuffix("```").strip()
    data = json.loads(raw)
    return FileSummary(**data)



'''
Test

if __name__ == "__main__":
    from loader import load_file
    from chunker import chunk_text

    text = load_file("samples/sample.txt")
    chunks = chunk_text(text)
    summary = summarise(chunks, "anthropic")
    print(summary)

'''
