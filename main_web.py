from flask import Flask, request, render_template_string

from src.maze.config.config import get_maze_config
from src.maze.engine.enemy import Enemy
from src.maze.engine.player import Player
from src.maze.factory.maze_generator import MazeGenerator
from src.maze.models.position import Position
from src.maze.render_views.web_view import WebView

app = Flask(__name__)

maze_config = get_maze_config()
maze_engine = MazeGenerator(
    width=maze_config.width,
    height=maze_config.height,
    max_walls=maze_config.walls,
    start=Position(x=0, y=0),
    end=Position(x=maze_config.exit_point[0], y=maze_config.exit_point[1])
).generate_maze()
view = WebView(maze_engine.maze, maze_engine.player, maze_engine.enemy)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        command = view.ask_command()
        if command is False:
            return view.render_quit()

        maze_engine.process_moves(command)
        if maze_engine.maze_state.isStop():
            return view.render_state(maze_engine.maze_state)

    return view.render_maze()


if __name__ == "__main__":
    app.run(debug=True)