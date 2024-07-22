from flask import Flask, request

from src.maze.controllers.game_controller import GameController
from src.maze.render_views.cli_view import CliView
from src.maze.render_views.web_view import WebView


class WebEngine:
    def __init__(self, game_controller: GameController):
        self.game_controller = game_controller
        self.view = WebView(game_controller.maze_engine)

    def run_app(self) -> None:
        """
        Runs the WEB game loop.
        """
        app = Flask(__name__)

        @app.route("/", methods=["GET", "POST"])
        def index():
            """Handle requests to the root URL, supporting both GET and POST methods."""
            if request.method == "POST":
                command = self.view.ask_command()
                if command is False:
                    return self.view.render_quit()

                return self.game_controller.process_command(command)
            else:
                top_scores = self.game_controller.init_view(self.view)
                return self.view.render_maze(top_scores)

        app.run(debug=True)