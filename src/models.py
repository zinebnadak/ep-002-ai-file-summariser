# What a Chunck and file summury looks like, then Pydantic validates datatypes using its Basemodel

from pydantic import BaseModel  #checks if data types are valid 
from typing import List #fields contain MULTIPLE items, just just a single str , using only 

class ChunckSummary (BaseModel):
    main_concept: str
    key_points: str
    keywords: str

class Filesummary (BaseModel):
    title: str
    overview: str
    key_sections: list[Section] # list o dictionaries, each item is a dictionary BUT validate the dict is a str with Section

class Section (BaseModel):
    sectio_title: str
    summary: str