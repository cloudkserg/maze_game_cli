from src.maze.config import get_maze_config
from src.maze.game import MazeGame
from src.maze.models.maze import MazeInfo
from src.maze.models.position import Position


def main() -> None:
    maze_config = get_maze_config()
    maze = MazeInfo.generate_maze(
        width=maze_config.width,
        height=maze_config.height,
        wall_count=maze_config.walls,
        exit_point=Position(x=maze_config.exit_point[0], y=maze_config.exit_point[1])
    )
    game = MazeGame(maze)

    while True:
        game.display()
        command = input("Enter move(s) (e.g., 'down 2, left 3') or 'quit' to exit: ")
        if command == 'quit':
            break
        game.process_moves(command)

if __name__ == "__main__":
    main()