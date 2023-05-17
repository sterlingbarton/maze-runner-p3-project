from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Maze, Game, Base
import json

engine = create_engine('sqlite:///maze.db')
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

maze1 = Maze(name='maze1', maze=json.dumps([
    [0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 0, 0, 'E']
]), difficulty='easy')

session.add(maze1)
session.commit()
