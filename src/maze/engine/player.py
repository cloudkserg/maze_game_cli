from src.maze.models.maze import Maze
from src.maze.models.position import Position


class Player:
    def __init__(self, start: Position):
        self.position = start
        self.steps_taken = 0

    def move(self, direction: str, steps: int, maze: Maze):
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