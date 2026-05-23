# This short code defines a Fruit data model with strict type rules using Pydantic, then creates and prints one instance of it.
# Pydantic automatically raises a ValidationError with a clear message telling you exactly which field failed and why. The instance Fruit should match exactly the rules defined in the class

from typing import Annotated, Literal
from annotated_types import Gt
from pydantic import BaseModel
class Fruit(BaseModel):
  name: str  
  color: Literal['red', 'green']  
  weight: Annotated[float, Gt(0)]  
  bazam: dict[str, list[tuple[int, bool, float]]]  #this is a dictionary with a string key and its value being a tuple with three items inside a list

print(
  Fruit(  #Fruit here is an instance
      name='Apple',
      color='red',
      weight=4.2,
      bazam={'foobar': [(1, True, 0.1)]},
  )
)