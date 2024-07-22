from pydantic import BaseModel
from typing import Tuple
from pydantic_settings import BaseSettings

class MazeConfig(BaseModel):
    width: int
    height: int
    walls: int  # Number of walls to be generated
    exit_point: Tuple[int, int]

class Settings(BaseSettings):
    maze_width: int
    maze_height: int
    maze_walls: int
    maze_exit_x: int
    maze_exit_y: int

    class Config:
        env_file = ".env"

def get_maze_config() -> MazeConfig:
    settings = Settings()
    return MazeConfig(
        width=settings.maze_width,
        height=settings.maze_height,
        walls=settings.maze_walls,
        exit_point=(settings.maze_exit_x, settings.maze_exit_y)
    )