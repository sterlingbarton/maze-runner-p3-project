from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Maze, Game
import json

engine = create_engine('sqlite:///maze.db')
Session = sessionmaker(bind=engine)

maze = None
player_pos = None


def load_maze(maze_id):
    global maze
    session = Session()
    maze = json.loads(session.query(Maze).get(maze_id))
    session.close()


def start_game(player_id, maze_id):
    global player_pos
    player_pos = [0, 0]
    load_maze(maze_id)

    session = Session()
    game = Game()
    session.add(game)
    session.commit()


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
