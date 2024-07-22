from pydantic import BaseModel


class MazeState(BaseModel):
    is_win: bool
    is_enemy: bool
    is_wall: bool

    def isStop(self):
        return self.is_win or self.is_enemy or self.is_wall