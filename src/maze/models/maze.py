from typing import List
from pydantic import BaseModel
from src.maze.maze_generator import MazeGenerator
from .position import Position


class Maze(BaseModel):
    width: int
    height: int
    walls: List[Position]
    exit_point: Position

    @staticmethod
    def generate_maze(width: int, height: int, wall_count: int, exit_point: Position) -> 'Maze':
        start_point = Position(x=0, y=0)
        generator = MazeGenerator(width, height,
                                  wall_count,
                                  start_point, exit_point)
        generator.generate_maze()
        walls = generator.get_wall_positions()
        return Maze(
            width=width,
            height=height,
            walls=walls,
            exit_point=exit_point
        )
