# Episode 002 — AI File Summariser

> One sentence — your single takeaway

## The Problem / The Question
I kept running into the same wall: you can't just drop a whole document into an LLM API call. There's a context limit, and even when the document fits, the quality of the summary degrades. I wanted to understand what actually happens between "I have a file" and "the model gives me something useful" and build the simplest version of that pipeline myself.

## What I Built
 
A command-line tool that accepts a `.txt`, `.pdf`, `.md`, or `.docx` file, chunks it into manageable pieces, sends each chunk to an LLM API (OpenAI or Anthropic), and returns a structured summary.

## What I Learned

- [The thing that actually confused you before it clicked]
- [The assumption that broke]
- [Something about one of the APIs you didn't expect — or how they differed]
- [The detail about chunking or structured outputs worth remembering]


## How to build
 
**Prerequisites**
- Python 3.9+
- An OpenAI API key and/or an Anthropic API key

Setup your virtual environment, activate it and install the dependencies:
```python3 -m venv venv```
```source venv/bin/activate```
```pip install anthropic openai pypdf python-dotenv pydantic python-docx```


## How to Run





<!-- Add real example output after the build -->



## Tech Used
 
- `anthropic` — Anthropic Python SDK, Messages API
- `openai` — OpenAI Python SDK, Chat Completions API
<!-- Add or remove ... -->


## References



---
*by [Zineb Nadak](https://github.com/zinebnadak) · [X](https://x.com/zinebnadak?s=21) · [LinkedIn](https://www.linkedin.com/in/zinebnadak?utm_source=share_via&utm_content=profile&utm_medium=member_ios)*
