from src.maze.engine.enemy import Enemy
from src.maze.engine.maze_engine import MazeEngine
from src.maze.engine.player import Player
from src.maze.factory.path_finder import PathFinder
from src.maze.factory.wall_manager import WallManager
from src.maze.models.maze import Maze
from src.maze.models.position import Position


class MazeGenerator:
    """
    Generates a maze with a specified configuration.

    Attributes:
        width (int): The width of the maze.
        height (int): The height of the maze.
        max_walls (int): The maximum number of walls to be placed in the maze.
        start (Position): The starting position of the maze.
        end (Position): The ending position of the maze.
    """
    def __init__(self, width: int, height: int, max_walls: int, start: 'Position', end: 'Position'):
        """
        Initialize the maze generator with maze dimensions, wall count, and start/end positions.

        Args:
            width (int): The width of the maze.
            height (int): The height of the maze.
            max_walls (int): The maximum number of walls to be generated.
            start (Position): The starting position for the maze.
            end (Position): The ending position for the maze.
        """
        self.width = width
        self.height = height
        self.max_walls = max_walls
        self.start = start
        self.end = end

    def generate_maze(self):
        """
        Generate a maze with a path from start to end, add walls, and initialize game entities.

        Returns:
            MazeEngine: The maze engine containing the generated maze, player, and enemy.
        """
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
