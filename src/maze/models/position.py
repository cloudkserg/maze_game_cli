from pydantic import BaseModel, conint

class Position(BaseModel):
    """
    Represents a position in a 2D grid.

    Attributes:
        x (int): The x-coordinate of the position.
        y (int): The y-coordinate of the position.
    """
    x: conint(ge=0)
    y: conint(ge=0)

    def __hash__(self) -> int:
        """
        Return a hash value for the Position instance.

        Returns:
            int: The hash value of the position, based on its x and y coordinates.
        """
        return hash((self.x, self.y))