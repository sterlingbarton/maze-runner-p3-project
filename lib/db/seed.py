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

maze2 = Maze(name='maze2', maze=json.dumps([
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, "E"]
]), difficulty='medium')

maze3 = Maze(name='maze3', maze=json.dumps([
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 'E']
]), difficulty='hard')

all_mazes = [maze1, maze2, maze3]
# random = session.query(Maze).delete()
# users = session.query(User).delete()

# session.add_all(all_mazes)
# session.commit()
