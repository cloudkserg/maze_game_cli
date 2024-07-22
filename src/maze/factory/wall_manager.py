from typing import List
import random

from src.maze.factory.path_finder import PathFinder
from src.maze.models.position import Position
from src.maze.models.maze import Maze


class WallManager:
    """
    Manages walls in the maze, including adding additional walls and pruning excess walls.

    Attributes:
        maze (Maze): The maze instance where walls are managed.
        max_walls (int): The maximum number of walls to be added.
    """
    def __init__(self, maze: Maze, max_walls: int):
        """
        Initialize the wall manager with the maze and maximum wall count.

        Args:
            maze (Maze): The maze instance.
            max_walls (int): The maximum number of walls to add.
        """
        self.maze = maze
        self.max_walls = max_walls

    def add_additional_walls(self, path_positions: List[Position]):
        """
        Add walls to the maze, excluding positions in the given path.

        Args:
            path_positions (List[Position]): The list of positions that must remain open.
        """
        all_positions = {Position(x=x, y=y) for x in range(self.maze.width) for y in range(self.maze.height)}
        all_positions.difference_update(path_positions)

        walls_added = 0
        while walls_added < self.max_walls and all_positions:
            pos = random.choice(list(all_positions))
            all_positions.remove(pos)
            self.maze.set_full(pos.x, pos.y)
            walls_added += 1

    def prune_excess_walls(self, start: Position, end: Position):
        """
        Remove excess walls to ensure a path exists from the start to the end position.

        Args:
            start (Position): The starting position of the path.
            end (Position): The ending position of the path.
        """
        path_finder = PathFinder(self.maze)

        def is_path_exists():
            return path_finder.has_path(start, end)

        while not is_path_exists():
            walls = self.maze.get_walls()
            if not walls:
                break
            wall_to_remove = random.choice(walls)
            self.maze.set_empty(wall_to_remove.x, wall_to_remove.y)
            walls.remove(wall_to_remove)
            if is_path_exists():
                break