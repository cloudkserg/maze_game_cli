from peewee import Model, SqliteDatabase

db = SqliteDatabase('highscores.db')

class BaseModel(Model):
    class Meta:
        database = db

