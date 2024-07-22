from typing import Union
from flask import Flask, request, render_template_string

from src.maze.models.maze import Maze
from src.maze.models.position import Position
from src.maze.engine.player import Player
from src.maze.engine.enemy import Enemy
from src.maze.models.maze_state import MazeState

class WebView:
    def __init__(self, maze: Maze, player: Player, enemy: Enemy) -> None:
        self.maze = maze
        self.player = player
        self.enemy = enemy

    def render_maze(self) -> str:
        return render_template_string('''
            <html>
                <body>
                    <form method="post">
                        <input type="text" name="command" placeholder="Enter move(s) (e.g., 'down 2, left 3') or 'quit' to exit">
                        <input type="submit" value="Submit">
                    </form>
                    {{ maze_html|safe }}
                </body>
            </html>
        ''', maze_html=self.render_maze_html())

    def render_maze_html(self) -> str:
        distance_to_goal = self.maze.calculate_distance_to_goal(self.player.position)
        html = f"<p>Steps taken: {self.player.steps_taken}</p>"
        html += f"<p>Distance to the goal: {distance_to_goal} cells</p>"
        html += "<pre>"
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                current_pos = Position(x=x, y=y)
                if current_pos == self.player.position:
                    html += 'P '
                elif current_pos in self.maze.walls:
                    html += '# '
                elif current_pos == self.enemy.position:
                    html += 'E '
                elif current_pos == self.maze.exit_point:
                    html += 'W '
                else:
                    html += '. '
            html += "\n"
        html += "</pre>"
        return html


    def ask_command(self) -> Union[bool, str]:
        command = request.form.get("command")
        if command == 'quit':
            return False
        return command


    def render_state(self, maze_state: MazeState) -> str:
        if maze_state.is_win:
            return "<p>You win!</p>"
        elif maze_state.is_enemy:
            return "<p>You lose! The enemy caught you!</p>"
        elif maze_state.is_wall:
            return "<p>You lose! You hit a wall!</p>"
        else:
            return f"<p>Your current position: x:{self.player.position.x} y:{self.player.position.y}</p>"


    def render_quit(self) -> str:
        return "<p>You quit.</p>"