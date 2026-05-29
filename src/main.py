# entry-point
# reads --file and --provider from the command line 
# calls all the the functions I made: load_file() to get text , chunk_text() to get chunks , summarise() to get the FileSummary
# prints everythign neatly to the terminal!

from loader import load_file
from chunker import chunk_text 
from summariser import summarise
import argparse 

def main(): 
    parser = argparse.ArgumentParser(description="Summarise a file using an LLM. By zinebnadak")
    parser.add_argument("--file", required=True, help="Path to file") # argparse automatically strips the -- and gives you the name as an attribute
    parser.add_argument("--provider", required=True, choices=["anthropic", "openai"]) # args.file has the file path, args.provider has the provider name
    args = parser.parse_args()

    print(f"\nLoading: {args.file}") #process indicator
    text = load_file(args.file)
    print(f"{len(text)} charachters loaded!\n\n") #process indicator

    chunks_list = chunk_text(text)
    print(f"Split into {len(chunks_list)} chunk(s)") #process indicator

    summary = summarise(chunks_list, args.provider)

    #pretty printing by accessing fields from the Pydantic objects 
    print("\n" + "––"*50)
    print(f"\nTitle: {summary.title}")
    print(f"\nOverview:\n{summary.overview}")

    print(f"\nKey Sections:")
    for section in summary.key_sections:
        print(f"\n{section.section_title}")
        print(f"    ›{section.summary}")

    print("\n" + "––"*50)

if __name__ == "__main__":
    main()



