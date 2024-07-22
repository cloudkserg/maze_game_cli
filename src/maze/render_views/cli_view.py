from abc import ABC
from typing import Union

from src.maze.db.score_collection import HighScoreList
from src.maze.engine.enemy import Enemy
from src.maze.engine.maze_engine import MazeEngine
from src.maze.engine.player import Player
from src.maze.models.maze import Maze
from src.maze.models.maze_state import MazeState
from src.maze.models.position import Position
from src.maze.render_views.base_view import BaseView


class CliView(BaseView, ABC):
    """
    A command-line interface (CLI) view for rendering the maze and interacting with the player.

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

    def render_maze(self, additional_context: str) -> None:
        """
        Render the maze to the CLI, displaying the current state including player, enemy, walls, and the goal.

        Prints:
            - The number of steps taken by the player.
            - The distance from the player to the goal.
            - The maze grid with symbols representing player ('P'), enemy ('E'), walls ('#'), goal ('W'), and empty spaces ('.').
        """
        print(additional_context)
        distance_to_goal = self.maze.calculate_distance_to_goal(self.player.position)
        print(f"Steps taken: {self.player.steps_taken}")
        print(f"Distance to the goal: {distance_to_goal} cells")
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                current_pos = Position(x=x, y=y)
                if current_pos == self.player.position:
                    print('P', end=' ')
                elif current_pos in self.maze.walls:
                    print('#', end=' ')
                elif current_pos == self.enemy.position:
                    print('E', end = ' ')
                elif current_pos == self.maze.win_point:
                    print('W', end=' ')
                else:
                    print('.', end=' ')

    def ask_command(self) -> Union[bool, str]:
        """
        Prompt the user to enter a command for moving or quitting the game.

        Returns:
            Union[bool, str]: Returns 'False' if the user wants to quit, otherwise returns the command string entered by the user.
        """
        command = input("Enter move(s) (e.g., 'down 2, left 3') or 'quit' to exit: ")
        if command == 'quit':
            return False
        return command

    def render_high_scores(self, top_scores: HighScoreList) -> str:
        context = ''
        for name, steps, date in top_scores:
            context += f"Name: {name}, Steps: {steps}, Date: {date}\n"
        return context

    def render_state(self, maze_state: MazeState) -> None:
        """
        Render the current state of the maze game based on the provided maze state.

        Args:
            maze_state (MazeState): The current state of the maze game.

        Prints:
            - A win message if the player has won.
            - A loss message if the player has encountered an enemy or hit a wall.
            - The current position of the player if the game is ongoing.
        """
        if maze_state.is_win:
            print("You win!")
        elif maze_state.is_enemy:
            print("You lose! The enemy caught you!")
        elif maze_state.is_wall:
            print("You lose! You hit a wall!")
        else:
            print(f"Your current position: x:{self.player.x} y:{self.player.y}")


    def render_quit(self) -> None:
        """
        Render a message indicating that the user has quit the game.

        Prints:
            - A quit message.
        """
        print("You quit.")

    def ask_name(self) -> str:
        """
        Prompt the user to enter a name for saving his score.

        Returns:
            str: name
        """
        return input("Enter name for saving score: ")
