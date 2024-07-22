import random

from src.maze.models.maze import Maze
from src.maze.models.position import Position

class Enemy:
    """
    Represents an enemy in the maze.

    Attributes:
        position (Position): The current position of the enemy.
    """
    def __init__(self, position: Position):
        """
        Initialize the enemy with a starting position.

        Args:
            position (Position): The initial position of the enemy.
        """
        self.position = position

    def move_randomly(self, maze: Maze):
        """
        Move the enemy to a random adjacent position within the maze.

        Args:
            maze (Maze): The maze in which the enemy moves.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = self.position.x + dx, self.position.y + dy
            if maze.is_within_bounds(nx, ny) and maze.is_empty(nx, ny):
                maze.set_empty(self.position.x, self.position.y)
                self.position = Position(x=nx, y=ny)
                maze.set_full(self.position.x, self.position.y)
                break