from typing import Union

from src.maze.engine.enemy import Enemy
from src.maze.engine.player import Player
from src.maze.models.maze import Maze
from src.maze.models.maze_state import MazeState
from src.maze.models.position import Position


class CliView:

    def __init__(self, maze: Maze, player: Player, enemy: Enemy) -> None:
        self.maze = maze
        self.player = player
        self.enemy = enemy

    def render_maze(self) -> None:
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
        command = input("Enter move(s) (e.g., 'down 2, left 3') or 'quit' to exit: ")
        if command == 'quit':
            return False
        return command

    def render_state(self, maze_state: MazeState) -> None:
        if maze_state.is_win:
            print("You win!")
        elif maze_state.is_enemy:
            print("You lose! The enemy caught you!")
        elif maze_state.is_wall:
            print("You lose! You hit a wall!")
        else:
            print(f"Your current position: x:{self.player.x} y:{self.player.y}")


    def render_quit(self) -> None:
        print("You quit.")
