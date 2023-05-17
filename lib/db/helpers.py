from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Maze, Game
import json

engine = create_engine('sqlite:///maze.db')
Session = sessionmaker(bind=engine)

player_pos = None


def load_maze(maze):
    session = Session()
    game_maze = json.loads(maze.maze)
    print(game_maze)
    session.close()


def start_game(maze):
    global player_pos
    player_pos = [0, 0]
    load_maze(maze)

    session = Session()
    # game = Game(maze.id)
    # session.add(game)
   # session.commit()


def move_up():
    if player_pos[0] > 0 and Maze[player_pos[0] - 1][player_pos[1]] == 0:
        player_pos[0] -= 1


def move_down():
    if player_pos[0] < len(Maze) - 1 and Maze[player_pos[0] + 1][player_pos[1]] == 0:
        player_pos[0] += 1


def move_left():
    if player_pos[1] > 0 and Maze[player_pos[0]][player_pos[1] - 1] == 0:
        player_pos[1] -= 1


def move_right():
    if player_pos[1] < len(Maze[0]) - 1 and Maze[player_pos[0]][player_pos[1] + 1] == 0:
        player_pos[1] += 1
