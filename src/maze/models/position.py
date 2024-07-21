from typing import List
from pydantic import BaseModel

class Position(BaseModel):
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))