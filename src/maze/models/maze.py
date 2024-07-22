from typing import List
from src.maze.models.position import Position
from pydantic import BaseModel, Field, conint

class Maze(BaseModel):
    width: conint(ge=1)
    height: conint(ge=1)
    walls: List[Position]
    exit_point: Position
    maze_cells: List[List[int]] = Field(default_factory=list)

    def __init__(self, **data):
        super().__init__(**data)
        self.maze_cells = [[0] * self.height for _ in range(self.width)]  # 0 for empty, 1 for wall

    def is_empty(self, x: int, y: int) -> bool:
        return self.maze_info[x][y] == 0

    def is_within_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def set_full(self, x: int, y: int):
        self.maze_cells[x][y] = 1

    def set_empty(self, x: int, y: int):
        self.maze_cells[x][y] = 0

    def get_walls(self) -> List[Position]:
        return [Position(x=x, y=y) for x in range(self.width) for y in range(self.height) if self.maze_cells[x][y] == 1]

    def calculate_distance_to_exit(self, position: Position):
        return abs(position.x - self.exit_point.x) + abs(position.y - self.exit_point.y)