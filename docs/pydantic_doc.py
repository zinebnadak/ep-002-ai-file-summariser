from typing import Annotated, Literal
from annotated_types import Gt
from pydantic import BaseModel
class Fruit(BaseModel):
  name: str  
  color: Literal['red', 'green']  
  weight: Annotated[float, Gt(0)]  
  bazam: dict[str, list[tuple[int, bool, float]]]  #this is a dictionary with a string key and its value being a tuple with three items inside a list

print(
  Fruit(
      name='Apple',
      color='red',
      weight=4.2,
      bazam={'foobar': [(1, True, 0.1)]},
  )
)