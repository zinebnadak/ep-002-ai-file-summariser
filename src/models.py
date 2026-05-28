# What a Chunck and file summury looks like, then Pydantic validates datatypes using its Basemodel

from pydantic import BaseModel  #checks if data types are valid 
from typing import List #fields contain MULTIPLE items, just just a single str , using only 

class ChunkSummary (BaseModel):
    main_concept: str
    key_points: list[str]
    keywords: list[str]

class Section (BaseModel):
    section_title: str
    summary: str

class FileSummary (BaseModel):
    title: str
    overview: str
    key_sections: list[Section] # list o dictionaries, each item is a dictionary BUT validate the dict is a str with Section

'''
chunk = ChunkSummary(
    main_concept="Machine Learning",
    key_points=[
        "Uses data to learn patterns",
        "Improves over time"
    ],
    keywords=["AI", "data", "models"]
)

print(chunk)
'''
