from typing import List
from src.maze.models.position import Position
import random

class Enemy:
    def __init__(self, position: Position):
        self.position = position

    def move_randomly(self, maze: List[List[int]], player_position: Position):
        """ Move the enemy randomly and avoid walls """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)  # Randomize direction order

        for dx, dy in directions:
            nx, ny = self.position.x + dx, self.position.y + dy
            if (0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and
                maze[nx][ny] == 0):  # Check bounds and if the cell is not a wall
                self.position = Position(x=nx, y=ny)
                break

    def is_at_position(self, pos: Position) -> bool:
        return self.position == pos