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
- main_idea: one sentence summary
- key_points: list of 3-5 main points
- keywords: list of 5-10 important terms

Return valid JSON only. No extra text.

Chunk:
{chunk_text}
"""

synthesis_prompt = """
Here are key points extracted from all chunks of a document.
Synthesise them into a final summary.

Return JSON only with these fields:
- title: short descriptive title for the document
- overview: 2-3 sentence summary of the whole document
- key_sections: list of sections, each with section_title and summary

Return valid JSON only. No extra text.

Key points:
{all_points}
"""

#this function will call the API and return raw text
def call_llm (provider: str, prompt: str) -> str:            # the provider argument will be taken from the terminal as user input later 
    if provider == "anthropic":
        client = Anthropic()
        message = client.messages.create(
            system = "Return valid JSON only.",       # system prompt here
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
            instructions = "Return valid JSON only.",
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
        


