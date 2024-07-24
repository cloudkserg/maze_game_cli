from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class GameState(Base):
    __tablename__ = 'game_state'

    id = Column(Integer, primary_key=True)
    player1_x = Column(Integer, nullable=False)
    player1_y = Column(Integer, nullable=False)
    player2_x = Column(Integer, nullable=False)
    player2_y = Column(Integer, nullable=False)


# Database setup
DATABASE_URL = "sqlite:///game_state.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)