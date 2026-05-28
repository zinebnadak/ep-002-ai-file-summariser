# Takes the list of chunks from chunker.py and sends each one to an LLM and gets a structured summary (key point and main idea) for each chunk
# Then synthesises everything so takes all those key points together and sends to LLM one more time to and put it into one final "FileSummary"

import openai
