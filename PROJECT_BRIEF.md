# Project Brief — Episode 002: AI File Summariser

 
## What I Am Building
 
A command-line tool that takes a file (.txt, .pdf, .md), chunks it, and uses the API to return a structured summary
 
## Why This Project
 
This is my first project that requires thinking about what happens *between* a file and an LLM. You can't just pass the whole document. You have to chunk it. This is the foundation of RAG I'm touching early.
 
## Decisions
 
| Decision | Choice | Reason |
|---|---|---|
| LLM API | OpenAI + Anthropic | Learning both SDKs and seeing how they differ in practice |
| Chunking strategy | - | - |
| Output format | Structured (JSON or typed) | - |
| File types | .txt, .pdf, .md, .docx | The most common formats in real-world use |
 
## What I Want to Understand by the End
 
- Why chunking matters and what breaks if you skip it
- How to get the Anthropic API to return structured output consistently
- What the actual limit is before quality degrades


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