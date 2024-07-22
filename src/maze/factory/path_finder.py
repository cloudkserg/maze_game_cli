from collections import deque

from src.maze.models.position import Position
from src.maze.models.maze import Maze

class PathFinder:
    """
    Finds paths in a maze to determine if there is a route between two positions.

    Attributes:
        maze (Maze): The maze instance in which to find paths.
    """
    def __init__(self, maze: Maze):
        """
        Initialize the path finder with the given maze.

        Args:
            maze (Maze): The maze instance to search for paths in.
        """
        self.maze = maze

    def has_path(self, start: Position, end: Position) -> bool:
        """
        Determine if a path exists from the start position to the end position.

        Uses breadth-first search (BFS) to explore the maze and find a route.

        Args:
            start (Position): The starting position of the path.
            end (Position): The target end position of the path.

        Returns:
            bool: True if a path exists from start to end, False otherwise.
        """
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