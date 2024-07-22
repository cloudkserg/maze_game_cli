from src.maze.models.maze import Maze
from src.maze.models.position import Position

class Player:
    """
    Represents a player in the maze.

    Attributes:
        position (Position): The current position of the player.
        steps_taken (int): The number of steps taken by the player.
    """
    def __init__(self, start: Position):
        """
        Initialize the player with a starting position.

        Args:
            start (Position): The initial position of the player.
        """
        self.position = start
        self.steps_taken = 0

    def move(self, direction: str, steps: int, maze: Maze):
        """
        Move the player in the specified direction for a number of steps.

        Args:
            direction (str): The direction to move ('up', 'down', 'left', 'right').
            steps (int): The number of steps to move in the specified direction.
            maze (Maze): The maze instance to check for boundaries and empty spaces.
        """
        dx, dy = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}[direction]
        for _ in range(steps):
            nx, ny = self.position.x + dx, self.position.y + dy
            if maze.is_within_bounds(nx, ny) and maze.is_empty(nx, ny):
                maze.set_empty(self.position.x, self.position.y)
                self.position = Position(x=nx, y=ny)
                maze.set_full(self.position.x, self.position.y)
                self.steps_taken += 1
            else:
                break