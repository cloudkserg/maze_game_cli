from typing import List, Optional

from src.maze.models.maze import Maze
from src.maze.models.position import Position

DEFAULT_AMOUNT_OF_STEPS = 1

class MazeGame:
    def __init__(self, maze: Maze) -> None:
        self.maze = maze
        self.player_position = Position(x=0, y=0)  # Starting position of the player
        self.steps_taken = 0  # Track the number of steps

    def display(self) -> None:
        distance_to_goal = self.calculate_distance_to_goal()
        print(f"Steps taken: {self.steps_taken}")
        print(f"Distance to the goal: {distance_to_goal} cells")
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                current_pos = Position(x=x, y=y)
                if current_pos == self.player_position:
                    print('P', end=' ')
                elif current_pos in self.maze.walls:
                    print('#', end=' ')
                elif current_pos == self.maze.exit_point:
                    print('E', end=' ')
                else:
                    print('.', end=' ')
            print()

    def calculate_distance_to_goal(self) -> int:
        return abs(self.player_position.x - self.maze.exit_point.x) + abs(self.player_position.y - self.maze.exit_point.y)


    def move_player(self, direction: str, steps: int) -> None:
        moves = {
            'up': (0, -1),
            'down': (0, 1),
            'left': (-1, 0),
            'right': (1, 0)
        }
        dx, dy = moves.get(direction, (0, 0))
        for _ in range(steps):
            new_position = Position(x=self.player_position.x + dx, y=self.player_position.y + dy)

            if (0 <= new_position.x < self.maze.width and
                    0 <= new_position.y < self.maze.height):
                if new_position in self.maze.walls:
                    self.end_game(f"Game Over! You hit a wall. Steps taken: {self.steps_taken}")
                    return
                elif new_position == self.maze.exit_point:
                    self.end_game(f"Congratulations! You've reached the exit. Steps taken: {self.steps_taken}")
                    return
                self.player_position = new_position
                self.steps_taken += 1
            else:
                break  # Stop moving if out of bounds

    def process_moves(self, commands: str) -> None:
        commands = commands.split(',')
        for command in commands:
            command = command.strip()
            if not command:
                continue  # Skip empty commands

            try:
                [direction, step_count] = self.get_direction_step_from_command(command)
                print(direction, step_count)
                self.move_player(direction, step_count)
            except ValueError as e:
                print(f"Invalid command '{command}': {e}")


    def get_direction_step_from_command(self, local_command: str) -> [str, int]:
        parts = local_command.split()

        if len(parts) == 0 or len(parts) > 2:
            raise ValueError("Invalid command format")

        #one step
        if len(parts) == 1:
            return [parts[0], DEFAULT_AMOUNT_OF_STEPS]

        #two and more steps
        try:
            steps = int(parts[1])
        except ValueError:
            raise ValueError("Step count must be an integer")
        return [parts[0], steps]

    def end_game(self, message: str) -> None:
        print(message)
        exit()  # Terminate the game