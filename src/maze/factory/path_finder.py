from collections import deque
from src.maze.models.position import Position
from src.maze.models.maze import Maze

class PathFinder:
    def __init__(self, maze: Maze):
        self.maze = maze

    def has_path(self, start: Position, end: Position) -> bool:
        queue = deque([start])
        visited = set()
        visited.add((start.x, start.y))

        while queue:
            x, y = queue.popleft()
            if Position(x=x, y=y) == end:
                return True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if self.maze.is_within_bounds(nx, ny) and (nx, ny) not in visited and self.maze.is_empty(nx, ny):
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        return False