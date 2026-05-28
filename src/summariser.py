# Takes the list of chunks from chunker.py and sends each one to an LLM and gets a structured summary (key point and main idea) for each chunk
# Then synthesises everything so takes all those key points together and sends to LLM one more time to and put it into one final "FileSummary"

from anthropic import Anthropic
from openai import OpenAI
from dotenv import load_dotenv
from src.models import ChunkSummary, FileSummary, Section # my three classes so we can validate the LLMs response
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

def call_llm (provider: str, prompt: str) -> str:            # the provider argument will be taken from the terminal as user input later 
    if provider == "anthropic":
        return

    if provider == "openai":
        return 
    
    raise ValueError(f"Unknown provider: {provider}")



def summuarise(chunks: list[str], provider: str) -> FileSummary:
    # will print processes to the command line 
    return 

