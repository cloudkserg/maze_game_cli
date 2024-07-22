from src.maze.config.config import get_maze_config
from src.maze.factory.maze_generator import MazeGenerator
from src.maze.models.position import Position
from src.maze.render_views.cli_view import CliView


def main() -> None:
    maze_config = get_maze_config()
    maze_engine = MazeGenerator(
        width=maze_config.width,
        height=maze_config.height,
        max_walls=maze_config.walls,
        start=Position(x=0, y=0),
        end=Position(x=maze_config.exit_point[0], y=maze_config.exit_point[1])
    ).generate_maze()

    maze_render = CliView(maze_engine.maze, maze_engine.player, maze_engine.enemy)

    while True:
        maze_render.render_maze()
        command = maze_render.ask_command()
        if not command:
            maze_render.render_quit()
            return

        maze_engine.process_moves(command)
        maze_render.render_state(maze_engine.maze_state)
        if maze_engine.maze_state.isStop():
            return

if __name__ == "__main__":
    main()
