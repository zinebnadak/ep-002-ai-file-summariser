# Episode 002 — AI File Summariser

> Even when a document fits in an LLM's context window, chunking it produces better, cheaper, more structured summaries. Chunking is the foundation every RAG system is built on.

## The initial Question
When you ask ChatGPT or Claude to summarise something, it doesn't just return a blob of text. It returns structure: a title, bullet points, sections. I wanted to understand how that works. How do you make an LLM answer/return something structured (And then that my code can actually use). How does chunking work in practice, where do you split the text exactly and how does it work all together? 

## What I Built
 
A command-line tool that accepts a `.txt`, `.pdf`, `.md`, or `.docx` file, chunks it into manageable pieces, sends each chunk to an LLM API (OpenAI or Anthropic), and returns a structured summary.

## What I Learned

- Splitting text at exactly N characters breaks sentences mid-word — the LLM sees broken thoughts and the summary becomes incoherent. Splitting on paragraph breaks (`\n\n`) keeps ideas intact.
- I assumed the LLM would always return clean JSON. It kept wrapping responses in markdown code fences (` ```json `) so `json.loads()` crashed every time. Fixed it by stripping the fences before parsing.
- Anthropic and OpenAI have slightly different request formats, read the docs for that!
- Pydantic doesn't just validate types — it's what makes LLM output usable in code. Without it, you're building on data you can't trust. Using the classes made you can always be sure the data is int the correct format. 


## How to Set Up

**Prerequisites**
- Python 3.9+
- An OpenAI API key and/or an Anthropic API key

Set up your virtual environment, activate it and install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install anthropic openai pypdf python-dotenv pydantic python-docx
```

Copy the environment file and add your API keys:

```bash
cp .env.example .env
```

## How to Run

```bash
python3 src/main.py --file path/to/your/file.pdf --provider anthropic
python3 src/main.py --file path/to/your/file.pdf --provider openai
```

Example output:

```bash
Loading: /Users/nadak/Desktop/README_copy.md
2872 characters loaded
Split into 3 chunk(s)

Summarising 1 chunk(s) using openai...

Chunk 1/1...

Synthesising final summary...

──────────────────────────────────────────────────
Title: Command-Line Tool for API-Based Summarisation

Overview:
This document discusses the development of a command-line tool designed 
for summarising various file formats using APIs from OpenAI and Anthropic. 
It highlights the limitations of LLM API calls and emphasises the importance 
of enhanced output quality.

Key Sections:

  › Limitations of LLM API Calls
    Describes the content limitations and potential quality issues 
    associated with API calls to language models.

  › Command-Line Tool Development
    Outlines the creation of a tool that processes multiple file 
    formats for summarisation purposes.

  › API Utilisation
    Explains how the tool leverages APIs from OpenAI and Anthropic 
    for effective summarisation.

  › Prerequisites
    Lists necessary prerequisites such as Python installation and 
    acquiring API keys for operation.

  › Importance of Chunking
    Focuses on the significance of breaking down content into chunks 
    for achieving structured and coherent summaries.
──────────────────────────────────────────────────
```

## Tech Used

- `anthropic` — Anthropic Python SDK, Messages API
- `openai` — OpenAI Python SDK, Responses API
- `pypdf` — PDF text extraction
- `python-docx` — .docx text extraction
- `python-dotenv` — loading API keys from `.env`
- `pydantic` — structured output validation

## References

- [Anthropic API docs](https://docs.anthropic.com/en/api/messages)
- [OpenAI API docs](https://platform.openai.com/docs/api-reference/chat)
- [Pydantic docs](https://pydantic.dev/docs/validation/latest/get-started/)
- [Pypdf docs](https://pypi.org/project/pypdf/)
- [python-docx docs](https://pypi.org/project/python-docx/)


*by [Zineb Nadak](https://github.com/zinebnadak) · [X](https://x.com/zinebnadak?s=21) · [LinkedIn](https://www.linkedin.com/in/zinebnadak?utm_source=share_via&utm_content=profile&utm_medium=member_ios)*
