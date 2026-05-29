# Project Brief — Episode 002: AI File Summariser

 
## What I Am Building
 
A command-line tool that takes a file (.txt, .pdf, .md), chunks it, and uses the API to return a structured summary
 
## Why This Project
 
This is my first project that requires thinking about what happens *between* a file and an LLM. If the file is hundreds of pages long or if you want the LLM to remember a folder of files over multiple chat sessions, a RAG (Retrieval-Augmented Generation) pipeline is used in which there is a concept called chunking: cutting these large file's text into small, digestible paragraphs or sections before sending them to the LLM. This is the foundation of RAG I'm touching early.
 
## Decisions
 
| Decision | Choice | Reason |
|---|---|---|
| LLM API | OpenAI + Anthropic | Learning both SDKs and seeing how they differ in practice |
| Chunking strategy | Paragraph-aware with 3000 char limit | Splitting on \n\n keeps sentences intact — fixed character splitting breaks mid-sentence and makes summaries incoherent |
| Output format | Structured JSON validated with Pydantic | LLMs return strings. Pydantic converts them into typed objects and catches malformed responses immediately |
| File types | .txt, .pdf, .md, .docx | The most common formats in real-world use |
 
## What I Want to Understand by the End
 
- Why chunking matters and what breaks if you skip it
- How to get the Anthropic API to return structured output consistently


## Definition of Done
 
- [ ] Accepts a file path as input
- [ ] Handles .txt, .pdf, and .md
- [ ] Chunks the file correctly (no mid-sentence breaks)
- [ ] Returns a structured summary via API
- [ ] Runs without errors
- [ ] README complete
- [ ] Commit history is clean and meaningful

---
*by [Zineb Nadak](https://github.com/zinebnadak) · [X](https://x.com/zinebnadak?s=21) · [LinkedIn](https://www.linkedin.com/in/zinebnadak?utm_source=share_via&utm_content=profile&utm_medium=member_ios)*
