from src.maze.config.config import get_maze_config
from src.maze.db.score_collection import ScoreCollection
from src.maze.factory.maze_generator import MazeGenerator
from src.maze.models.position import Position
from src.maze.render_views.base_view import BaseView
from src.maze.render_views.cli_view import CliView
from src.maze.render_views.web_view import WebView


class GameController:
    """
    Manages the flow of the maze game, including setup and game loop.

    Attributes:
        score_collection (ScoreCollection): Manages the high scores of the game.
        view (CliView | WebView | None): The view for rendering game state and interacting with the user.
        maze_engine (MazeEngine | None): The engine that handles maze generation and game logic.
    """

    def __init__(self):
        """
        Initializes the GameController with default attributes.
        """
        self.score_collection = ScoreCollection()
        self.view = None
        self.maze_engine = None

    def setup_game(self):
        """
        Sets up the game environment by configuring the maze, initializing
        the maze engine and view, and rendering the high scores.
        """
        maze_config = get_maze_config()
        maze_generator = MazeGenerator(
            width=maze_config.width,
            height=maze_config.height,
            max_walls=maze_config.walls,
            start=Position(x=0, y=0),
            end=Position(x=maze_config.exit_point[0], y=maze_config.exit_point[1])
        )
        self.maze_engine = maze_generator.generate_maze()

    def init_view(self, view: BaseView) -> str:
        self.view = BaseView
        return self.view.render_high_scores(self.score_collection.get_top_scores(10))

    def process_command(self, command: str) -> str:
        """
        Processes the user command and updates the game state.

        Args:
            command (str): The user command to process.

        Returns:
            str: The HTML content to be rendered or the CLI output based on the mode.
        """
        if command == 'quit':
            return self.view.render_quit()

        self.maze_engine.process_moves(command)
        if self.maze_engine.maze_state.is_win:
            name = self.view.ask_name()
            self.score_collection.save_score(name, self.maze_engine.player.steps_taken)
            self.view.render_high_scores(self.score_collection.get_top_scores(10))

        if self.maze_engine.maze_state.is_stop():
            return self.view.render_state(self.maze_engine.maze_state)
        self.view.render_maze()
