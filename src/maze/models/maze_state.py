from pydantic import BaseModel


class MazeState(BaseModel):
    """
    Represents the current state of the maze game.

    Attributes:
        is_win (bool): Indicates if the game is won.
        is_enemy (bool): Indicates if the player has encountered an enemy.
        is_wall (bool): Indicates if the player has hit a wall.
    """
    is_win: bool
    is_enemy: bool
    is_wall: bool

    def is_stop(self):
        """
        Determine if the game has reached a stopping condition.

        Returns:
            bool: True if the game is in a state where it should stop (win, enemy encounter, or wall hit), False otherwise.
        """
        return self.is_win or self.is_enemy or self.is_wall