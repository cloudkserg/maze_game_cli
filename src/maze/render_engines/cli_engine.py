from src.maze.controllers.game_controller import GameController
from src.maze.render_views.cli_view import CliView


class CliEngine:
    def __init__(self, game_controller: GameController):
        self.game_controller = game_controller
        self.view = CliView(game_controller.maze_engine)
        game_controller.init_view(self.view)

    def run_app(self) -> None:
        """
        Runs the CLI game loop.
        """
        while True:
            self.view.render_maze()
            command = self.view.ask_command()
            if not command:
                self.view.render_quit()
                return

            response = self.game_controller.process_command(command)
            if response:
                print(response)