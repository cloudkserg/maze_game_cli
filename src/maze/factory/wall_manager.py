from typing import List

from src.maze.factory.path_finder import PathFinder
from src.maze.models.position import Position
from src.maze.models.maze import Maze
import random


class WallManager:
    def __init__(self, maze: Maze, max_walls: int):
        self.maze = maze
        self.max_walls = max_walls

    def add_additional_walls(self, path_positions: List[Position]):
        all_positions = {Position(x=x, y=y) for x in range(self.maze.width) for y in range(self.maze.height)}
        all_positions.difference_update(path_positions)

        walls_added = 0
        while walls_added < self.max_walls and all_positions:
            pos = random.choice(list(all_positions))
            all_positions.remove(pos)
            self.maze.set_full(pos.x, pos.y)
            walls_added += 1

    def prune_excess_walls(self, start: Position, end: Position):
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