from typing import List, Optional, Tuple

from src.maze.engine.enemy import Enemy
from src.maze.engine.player import Player
from src.maze.factory.wall_manager import WallManager
from src.maze.models.maze import Maze
from src.maze.models.maze_state import MazeState
from src.maze.models.position import Position

DEFAULT_AMOUNT_OF_STEPS = 1

class MazeEngine:
    def __init__(self, maze: Maze, player: Player, enemy: Enemy):
        self.maze = maze
        self.player = player
        self.enemy = enemy
        self.maze_state = MazeState(is_win = False, is_wall=False, is_enemy = False)

    def process_moves(self, command: str) -> None:
        direction, steps = self.parse_command(command.strip())
        self.player.move(direction, steps, self.maze)
        self.enemy.move_randomly(self.maze)
        self.update_game_state()

    def parse_command(self, command: str) -> Tuple[str, int]:
        parts = command.split()
        direction = parts[0]
        steps = int(parts[1]) if len(parts) > 1 else 1
        return direction, steps

    def update_game_state(self):
        if self.player.position == self.maze.win_point:
            self.maze_state.is_win = True
        elif self.player.position == self.enemy.position:
            self.maze_state.is_enemy = True
        elif not self.maze.is_empty(self.player.position.x, self.player.position.y):
            self.maze_state.is_wall = True