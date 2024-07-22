from typing import List, Tuple, TypeAlias

from src.maze.db.base_model import db
from src.maze.db.score_model import ScoreModel

HighScoreList: TypeAlias = List[Tuple[str, int, str]]

class ScoreCollection:

    def save_score(self, name: str, steps: int):
        """Save the score using Peewee ORM."""
        with db.atomic():
            ScoreModel.create(name=name, steps=steps)

    def get_top_scores(self, limit: int = 10) -> HighScoreList:
        """Retrieve the top scores from the database."""
        top_scores = (ScoreModel
                      .select()
                      .order_by(ScoreModel.steps)
                      .limit(limit))
        return [(score.name, score.steps, score.date.strftime("%d.%m.%Y %H:%M:%S")) for score in top_scores]