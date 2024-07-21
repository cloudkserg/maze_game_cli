from typing import List
from src.maze.models.position import Position

class Maze:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.maze_info = [[0] * height for _ in range(width)]  # 0 for empty, 1 for wall

    def is_empty(self, x: int, y: int) -> bool:
        return self.maze_info[x][y] == 0

    def is_within_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def set_wall(self, x: int, y: int):
        self.maze_info[x][y] = 1

    def set_empty(self, x: int, y: int):
        self.maze_info[x][y] = 0

    def get_walls(self) -> List[Position]:
        return [Position(x=x, y=y) for x in range(self.width) for y in range(self.height) if self.maze[x][y] == 1]