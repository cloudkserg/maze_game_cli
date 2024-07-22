from src.maze.engine.enemy import Enemy
from src.maze.engine.maze_engine import MazeEngine
from src.maze.engine.player import Player
from src.maze.factory.path_finder import PathFinder
from src.maze.factory.wall_manager import WallManager
from src.maze.models.maze import Maze
from src.maze.models.position import Position


class MazeGenerator:
    def __init__(self, width: int, height: int, max_walls: int, start: 'Position', end: 'Position'):
        self.width = width
        self.height = height
        self.max_walls = max_walls
        self.start = start
        self.end = end

    def generate_maze(self):
        maze = Maze(width=self.width, height=self.height)
        path_finder = PathFinder(maze)

        start = Position(x=0, y=0)

        # Ensure a path from start to end
        path_positions = []
        visited = set()
        visited.add((start.x, start.y))
        path_finder.has_path(start, self.end)

        # Add walls and prune excess walls
        wall_manager = WallManager(maze, self.max_walls)
        wall_manager.add_additional_walls(path_positions)
        wall_manager.prune_excess_walls(start, self.end)

        # Initialize player and enemy
        player = Player(start)
        enemy = Enemy(Position(x=self.width - 1, y=0))

        return MazeEngine(maze, player, enemy)
