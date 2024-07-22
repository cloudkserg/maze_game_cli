from peewee import IntegerField, CharField, DateTimeField
from datetime import datetime

from src.maze.db.base_model import BaseModel


class ScoreModel(BaseModel):
    name = CharField()
    steps = IntegerField()
    date = DateTimeField(default=datetime.utcnow)