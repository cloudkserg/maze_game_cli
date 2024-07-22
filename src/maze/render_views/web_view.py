from abc import ABC
from typing import Union
from flask import Flask, request, render_template_string

from src.maze.db.score_collection import HighScoreList
from src.maze.engine.maze_engine import MazeEngine
from src.maze.models.maze import Maze
from src.maze.models.position import Position
from src.maze.engine.player import Player
from src.maze.engine.enemy import Enemy
from src.maze.models.maze_state import MazeState
from src.maze.render_views.base_view import BaseView


class WebView(BaseView, ABC):
    """
    A web view for rendering the maze and interacting with the player through a web interface.

    Attributes:
        maze (Maze): The maze instance to be displayed.
        player (Player): The player instance to be displayed in the maze.
        enemy (Enemy): The enemy instance to be displayed in the maze.
    """
    def __init__(self, maze_engine: MazeEngine) -> None:
        """
        Initialize the CLI view with the maze, player, and enemy.

        Args:
            maze_engine (MazeEngine): The maze Engine instance.
        """
        self.maze = maze_engine.maze
        self.player = maze_engine.player
        self.enemy = maze_engine.enemy

    def render_maze(self, additional_context: str) -> str:
        """
        Render the maze to an HTML template.

        Returns:
            additional_context (str): The HTML additional context
            str: The HTML representation of the maze, including a form for user commands and the maze grid.
        """
        return render_template_string('''
            <html>
                <body>
                    {{ additional_context|safe}}
                    <form method="post">
                        <input type="text" name="command" placeholder="Enter move(s) (e.g., 'down 2, left 3') or 'quit' to exit">
                        <input type="submit" value="Submit">
                    </form>
                    {{ maze_html|safe }}
                </body>
            </html>
        ''', maze_html=self.render_maze_html(), additional_context=additional_context)

    def render_maze_html(self) -> str:
        """
        Generate HTML for displaying the maze grid.

        Returns:
            str: The HTML representation of the maze grid, showing player ('P'), enemy ('E'), walls ('#'),
                  goal ('W'), and empty spaces ('.').
        """
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
        """
        Retrieve the command input from the web form.

        Returns:
            Union[bool, str]: Returns 'False' if the user wants to quit, otherwise returns the command string entered by the user.
        """
        command = request.form.get("command")
        if command == 'quit':
            return False
        return command


    def render_state(self, maze_state: MazeState) -> str:
        """
        Render the current state of the maze game based on the provided maze state.

        Args:
            maze_state (MazeState): The current state of the maze game.

        Returns:
            str: HTML message indicating the game outcome (win, lose, or current position).
        """
        if maze_state.is_win:
            return "<p>You win!</p>"
        elif maze_state.is_enemy:
            return "<p>You lose! The enemy caught you!</p>"
        elif maze_state.is_wall:
            return "<p>You lose! You hit a wall!</p>"
        else:
            return f"<p>Your current position: x:{self.player.position.x} y:{self.player.position.y}</p>"

    def render_high_scores(self, top_scores: HighScoreList) -> str:
        """
        Generate HTML for displaying the high scores.

        Args:
            top_scores (HighScoreList): The list of top scores to be displayed.

        Returns:
            str: The HTML representation of the high scores.
        """
        html = "<ul>"
        for name, steps, date in top_scores:
            html += f"<li>Name: {name}, Steps: {steps}, Date: {date}</li>"
        html += "</ul>"
        return html

    def render_quit(self) -> str:
        """
        Render a message indicating that the user has quit the game.

        Returns:
            str: HTML message indicating the game was quit.
        """
        return "<p>You quit.</p>"