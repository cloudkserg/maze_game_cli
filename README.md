Certainly! Here's the updated `README.md` using `uv` for creating a virtual environment and installing packages.

```markdown
# Maze Game

## Overview

The Maze Game is a simple command-line Python game where players navigate through a maze. The maze is represented as a grid with walls, and the player can move up, down, left, or right to explore the maze.

## Project Structure

- `src/models.py`: Contains Pydantic models for maze and position data.
- `src/utils.py`: Includes utility functions such as printing the maze.
- `src/game.py`: Implements the core game logic, including player movement and maze interaction.
- `src/config.py`: Manages configuration settings using environment variables.
- `.env`: Configuration file for environment variables.
- `main.py`: Entry point of the game, where the game loop and user input handling occur.
- `requirements.txt`: Lists required Python packages.

## Requirements

- `uv` (for managing virtual environments)
- `pydantic`
- `mypy`
- `python-dotenv`

To install the required packages, you need to have `uv` installed. You can install it using pip if you don't have it:

```bash
pip install uv
```

## Getting Started

1. **Create a Virtual Environment**

   ```bash
   uv venv venv
   ```

2. **Activate the Virtual Environment**

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   uv pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the root directory with the following content (can copy from .env.local):

   ```
   MAZE_WIDTH=5
   MAZE_HEIGHT=5
   MAZE_WALLS=2,1;2,2;2,3
   ```

5. **Run the Game**

   Execute the `main.py` script to start the game:

   ```bash
   python main.py
   ```

   You will be prompted to enter moves (up, down, left, right) with a amount of step (like up 2, down 3) or type 'quit' to exit the game.

## Example

Here's an example of how the game will display the maze:

```
. . . . .
. . . . .
. # # # .
. . . . .
. . . . .
```

The `P` represents the player's position, and `#` represents walls. You can move the player with the following commands:

- `up`
- `down`
- `left`
- `right`

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
