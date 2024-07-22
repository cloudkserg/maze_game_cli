from flask import Flask, request, render_template_string

from src.maze.config.config import get_mode
from src.maze.config.mode import Mode
from src.maze.controllers.game_controller import GameController
from src.maze.db.init_db import init_db
from src.maze.render_engines.cli_engine import CliEngine
from src.maze.render_engines.web_engine import WebEngine
from src.maze.render_views.cli_view import CliView
from src.maze.render_views.web_view import WebView


def main() -> None:
    """Main function to start the application based on the mode."""
    init_db()
    game_controller = GameController()
    mode = get_mode()
    game_controller.setup_game()


    if mode == Mode.CLI:
        cli_engine = CliEngine(game_controller)
        cli_engine.run_app()
    elif mode == Mode.WEB:
        web_engine = WebEngine(game_controller)
        web_engine.run_app()
    else:
        raise ValueError(f"Unsupported mode: {mode}")


if __name__ == "__main__":
    main()