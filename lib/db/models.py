from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///maze.db')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)

    game = relationship('Game', back_populates='user')


class Maze(Base):
    __tablename__ = 'mazes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    maze = Column(String)
    difficulty = Column(String)

    game = relationship('Game', back_populates='maze')


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    maze_id = Column(Integer, ForeignKey('mazes.id'))

    user = relationship('User', back_populates='game')
    maze = relationship('Maze', back_populates='game')
