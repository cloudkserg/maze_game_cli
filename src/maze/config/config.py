from pydantic import BaseModel, Field
from typing import Tuple
from pydantic_settings import BaseSettings

from src.maze.config.mode import Mode


class MazeConfig(BaseModel):
    """Configuration for the maze."""
    width: int
    height: int
    walls: int  # Number of walls to be generated
    exit_point: Tuple[int, int]

class Settings(BaseSettings):
    """Settings for maze configuration."""
    maze_width: int
    maze_height: int
    maze_walls: int
    maze_exit_x: int
    maze_exit_y: int
    mode: Mode  # Add the mode setting

    class Config:
        env_file = ".env"

def get_maze_config() -> MazeConfig:
    """Get maze configuration from settings.

    Returns:
        MazeConfig: The configuration for the maze.
    """
    settings = Settings()
    return MazeConfig(
        width=settings.maze_width,
        height=settings.maze_height,
        walls=settings.maze_walls,
        exit_point=(settings.maze_exit_x, settings.maze_exit_y)
    )

def get_mode() -> Mode:
    """Get the application mode from settings.

    Returns:
        str: The mode of the application ('CLI' or 'WEB').
    """
    settings = Settings()
    return settings.mode