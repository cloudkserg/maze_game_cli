from typing import List

from src.maze.models.maze import Maze
from src.maze.models.position import Position
import random

class Enemy:
    def __init__(self, position: Position):
        self.position = position

    def move_randomly(self, maze: Maze):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = self.position.x + dx, self.position.y + dy
            if maze.is_within_bounds(nx, ny) and maze.is_empty(nx, ny):
                maze.set_empty(self.position.x, self.position.y)
                self.position = Position(x=nx, y=ny)
                maze.set_full(self.position.x, self.position.y)
                break