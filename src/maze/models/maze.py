from typing import List
from pydantic import BaseModel, Field, conint

from src.maze.models.position import Position

class Maze(BaseModel):
    """
    Represents a maze with dimensions, walls, and a winning point.

    Attributes:
        width (int): The width of the maze.
        height (int): The height of the maze.
        walls (List[Position]): The list of wall positions in the maze.
        win_point (Position): The position that indicates the win point.
        maze_cells (List[List[int]]): A 2D list representing the maze grid; 0 for empty, 1 for wall.
    """
    width: conint(ge=1)
    height: conint(ge=1)
    walls: List[Position] = Field(default_factory=int)
    win_point: Position
    maze_cells: List[List[int]] = Field(default_factory=list)

    def __init__(self, **data):
        """
        Initialize the maze with dimensions and wall information.

        Args:
            **data: Additional keyword arguments passed to the BaseModel constructor.
        """
        super().__init__(**data)
        self.maze_cells = [[0] * self.height for _ in range(self.width)]  # 0 for empty, 1 for wall

    def is_empty(self, x: int, y: int) -> bool:
        """
        Check if a cell at the specified coordinates is empty.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.

        Returns:
            bool: True if the cell is empty, False otherwise.
        """
        return self.maze_info[x][y] == 0

    def is_within_bounds(self, x: int, y: int) -> bool:
        """
        Check if the given coordinates are within the bounds of the maze.

        Args:
            x (int): The x-coordinate to check.
            y (int): The y-coordinate to check.

        Returns:
            bool: True if the coordinates are within bounds, False otherwise.
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def set_full(self, x: int, y: int):
        """
        Set a cell at the specified coordinates as occupied by a wall.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
        """
        self.maze_cells[x][y] = 1

    def set_empty(self, x: int, y: int):
        """
        Set a cell at the specified coordinates as empty.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
        """
        self.maze_cells[x][y] = 0

    def get_walls(self) -> List[Position]:
        """
        Get a list of all positions that contain walls.

        Returns:
            List[Position]: A list of positions where walls are located.
        """
        return [Position(x=x, y=y) for x in range(self.width) for y in range(self.height) if self.maze_cells[x][y] == 1]

    def calculate_distance_to_exit(self, position: Position):
        """
        Calculate the Manhattan distance from a given position to the win point.

        Args:
            position (Position): The position from which to calculate the distance.

        Returns:
            int: The Manhattan distance to the win point.
        """
        return abs(position.x - self.win_point.x) + abs(position.y - self.win_point.y)