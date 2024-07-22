from src.maze.db.base_model import db
from src.maze.db.score_model import ScoreModel


def init_db():
    """Create the database tables if they don't exist."""
    db.connect()
    db.create_tables([ScoreModel], safe=True)
    db.close()