from src.maze.config.config import get_maze_config
from src.maze.factory.maze_generator import MazeGenerator
from src.maze.models.position import Position
from src.maze.render_views.cli_view import CliView


def main() -> None:
    """
    Main function to run the maze game.

    This function initializes the maze configuration and maze engine, sets up the
    CLI view, and enters the main game loop. In the loop, it continuously renders
    the maze, processes user commands, and updates the game state until the game
    is over or the user chooses to quit.

    Steps:
    1. Get maze configuration.
    2. Initialize the maze engine with the given configuration.
    3. Set up the CLI view with the maze and player information.
    4. Enter the main game loop:
        - Render the current state of the maze.
        - Ask the user for a command.
        - Process the command to update the game state.
        - If the game is over (stop condition is met), render the final state and exit.
        - If the user chooses to quit, render the quit message and exit.

    Returns:
        None
    """
    maze_config = get_maze_config()
    maze_engine = MazeGenerator(
        width=maze_config.width,
        height=maze_config.height,
        max_walls=maze_config.walls,
        start=Position(x=0, y=0),
        end=Position(x=maze_config.exit_point[0], y=maze_config.exit_point[1])
    ).generate_maze()

    view = CliView(maze_engine.maze, maze_engine.player, maze_engine.enemy)

    while True:
        view.render_maze()
        command = view.ask_command()
        if not command:
            view.render_quit()
            return

        maze_engine.process_moves(command)
        if maze_engine.maze_state.is_stop():
            view.render_state(maze_engine.maze_state)
            return

        view.render_state(maze_engine.maze_state)


if __name__ == "__main__":
    main()
