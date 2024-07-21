from typing import Tuple
from .models import Position

def print_maze(maze: 'Maze', player_pos: Position) -> None:
    for y in range(maze.height):
        for x in range(maze.width):
            pos = Position(x=x, y=y)
            if pos == player_pos:
                print('P', end=' ')
            elif maze.is_wall(pos):
                print('#', end=' ')
            else:
                print('.', end=' ')
        print()