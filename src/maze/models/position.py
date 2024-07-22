from pydantic import BaseModel, conint

class Position(BaseModel):
    x: conint(ge=0)
    y: conint(ge=0)

    def __hash__(self) -> int:
        return hash((self.x, self.y))