from src.maze.models.position import Position


class Player:
    def __init__(self, start: Position):
        self.position = start

    def move(self, direction: str, maze):
        dx, dy = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}[direction]
        nx, ny = self.position.x + dx, self.position.y + dy

        if maze.is_within_bounds(nx, ny) and maze.is_empty(nx, ny):
            self.position = Position(x=nx, y=ny)