from pydantic import BaseModel  #checks if data types are valid if not 
from typing import List

class ChunckSummary (BaseModel):
    main_concept: str
    key_points: str
    keywords: str

class Filesummary (BaseModel):
    title: str
    overview: str
    key_sections: List[dict] 