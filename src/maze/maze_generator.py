from typing import List
from src.maze.models.position import Position
from collections import deque
import random


class MazeGenerator:
    def __init__(self, width: int, height: int, max_walls: int, start: 'Position', end: 'Position'):
        self.width = width
        self.height = height
        self.max_walls = max_walls
        self.maze = [[0] * height for _ in range(width)]  # 0 for empty, 1 for wall
        self.start = start
        self.end = end

    def generate_maze(self):
        self.add_additional_walls()
        self.create_path()
        self.prune_excess_walls()

    def get_wall_positions(self) -> List[Position]:
        wall_positions = [
            Position(x=x, y=y)
            for x in range(self.width)
            for y in range(self.height)
            if self.maze[x][y] == 1
        ]
        return wall_positions

    def create_path(self):
        # Use BFS or DFS to ensure a path from start to end
        queue = deque([(self.start.x, self.start.y)])
        visited = set()
        visited.add((self.start.x, self.start.y))
        self.maze[self.start.x][self.start.y] = 0  # Clear start position

        while queue:
            x,y  = queue.popleft()
            if Position(x=x, y=y) == self.end:
                break
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.width and 0 <= ny < self.height and
                        (nx, ny) not in visited and self.maze[nx][ny] == 0):
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    self.maze[nx][ny] = 0

    def add_additional_walls(self):
        all_positions = {Position(x=x, y=y) for x in range(self.width) for y in range(self.height)}
        # Remove positions already used in the path
        for x in range(self.width):
            for y in range(self.height):
                if self.maze[x][y] == 1:
                    all_positions.discard(Position(x=x, y=y))

        # Add walls until reaching the maximum number of walls
        walls_added = 0
        while walls_added < self.max_walls and all_positions:
            pos = random.choice(list(all_positions))
            all_positions.remove(pos)
            self.maze[pos.x][pos.y] = 1
            walls_added += 1

    def prune_excess_walls(self):
        def is_path_exists():
            queue = deque([(self.start.x, self.start.y)])
            visited = set()
            visited.add((self.start.x, self.start.y))

            while queue:
                x, y = queue.popleft()
                if Position(x=x, y=y) == self.end:
                    return True
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < self.width and 0 <= ny < self.height and
                            (nx, ny) not in visited and self.maze[nx][ny] == 0):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return False

        # Remove walls if there’s no valid path from start to end
        while not is_path_exists():
            for x in range(self.width):
                for y in range(self.height):
                    if self.maze[x][y] == 1:
                        self.maze[x][y] = 0
                        if is_path_exists():
                            break
                else:
                    continue
                break
