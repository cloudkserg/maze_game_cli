from abc import ABC, abstractmethod
from typing import Union
from src.maze.models.position import Position
from src.maze.db.score_collection import ScoreCollection
from src.maze.config.config import MazeConfig
from src.maze.models.maze_state import MazeState

class BaseView(ABC):
    """Abstract base class for different types of views (CLI, WEB)."""

    @abstractmethod
    def render_maze(self, additional_context: str) -> Union[str, None]:
        """Render the maze in the view format."""
        pass

    @abstractmethod
    def ask_command(self) -> Union[bool, str]:
        """Ask the user for a command and return the response."""
        pass

    @abstractmethod
    def render_state(self, maze_state: MazeState) -> Union[str, None]:
        """Render the state of the game."""
        pass

    @abstractmethod
    def render_high_scores(self, scores: list) -> Union[str, None]:
        """Render the high scores."""
        pass

    @abstractmethod
    def ask_name(self) -> str:
        """Ask for the user's name for scoring."""
        pass

    @abstractmethod
    def render_quit(self) -> Union[str, None]:
        """Render the quit message."""
        pass