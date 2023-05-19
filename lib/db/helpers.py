from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Maze, Game, User
import json
import sys
from colorama import Fore, Back, Style
from playsound import playsound

engine = create_engine('sqlite:///maze.db')
Session = sessionmaker(bind=engine)

game_maze = None
player_pos = [0, 0]

celebrate = '''                                  .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =- /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
        *
        *
'''


def load_maze(maze):
    session = Session()
    global game_maze
    game_maze = json.loads(maze.maze)
    for row in range(len(game_maze)):
        for col in range(len(game_maze[row])):
            if row == player_pos[0] and col == player_pos[1]:
                print('X', end=' ')
            else:
                print(game_maze[row][col], end=' ')
        print()
    session.close()


def start_game(maze, username):
    load_maze(maze)
    session = Session()
    user = session.query(User).filter(User.username == username).first()
    print(user.username)
    game = Game(maze_id=maze.id, user_id=user.id)
    session.add(game)
    session.commit()


def move_up():
    if game_maze[player_pos[0] - 1][player_pos[1]] == 1:
        print(Fore.RED + 'Cannot move that direction. Please try another')
    elif player_pos[0] > 0:
        player_pos[0] -= 1
        for row in range(len(game_maze)):
            for col in range(len(game_maze[row])):
                if row == player_pos[0] and col == player_pos[1]:
                    print('X', end=' ')
                else:
                    print(game_maze[row][col], end=' ')
            print()
    else:
        print(Fore.RED + 'Cannot move that direction. Please try another')

    if player_pos == [len(game_maze) - 1, len(game_maze[0]) - 1]:
        print(Fore.MAGENTA + Style.BRIGHT +
              f'Congratulations, you have reached the goal!\n {celebrate}')
        playsound('sound/trumpet-fanfare-royal-announcement-soundroll-1-00-06.mp3')
        sys.exit(-1)


def move_down():
    if player_pos[0] < len(game_maze) - 1:
        if game_maze[player_pos[0] + 1][player_pos[1]] == 1:
            print(Fore.RED + 'Cannot move that direction. Please try another')
        else:
            player_pos[0] += 1
            for row in range(len(game_maze)):
                for col in range(len(game_maze[row])):
                    if row == player_pos[0] and col == player_pos[1]:
                        print('X', end=' ')
                    else:
                        print(game_maze[row][col], end=' ')
                print()
    else:
        print(Fore.RED + 'Cannot move that direction. Please try another')

    if player_pos == [len(game_maze) - 1, len(game_maze[0]) - 1]:
        print(Fore.MAGENTA + Style.BRIGHT +
              f'Congratulations, you have reached the goal!\n {celebrate}')
        playsound('sound/trumpet-fanfare-royal-announcement-soundroll-1-00-06.mp3')
        sys.exit(-1)


def move_left():
    if game_maze[player_pos[0]][player_pos[1] - 1] == 1:
        print(Fore.RED + 'Cannot move that direction. Please try another')
    elif player_pos[1] > 0:
        player_pos[1] -= 1
        for row in range(len(game_maze)):
            for col in range(len(game_maze[row])):
                if row == player_pos[0] and col == player_pos[1]:
                    print('X', end=' ')
                else:
                    print(game_maze[row][col], end=' ')
            print()
    else:
        print(Fore.RED + 'Cannot move that direction. Please try another')

    if player_pos == [len(game_maze) - 1, len(game_maze[0]) - 1]:
        print(Fore.MAGENTA + Style.BRIGHT +
              f'Congratulations, you have reached the goal!\n {celebrate}')
        playsound('sound/trumpet-fanfare-royal-announcement-soundroll-1-00-06.mp3')
        sys.exit(-1)


def move_right():
    if player_pos[1] < len(game_maze[0]) - 1:
        if game_maze[player_pos[0]][player_pos[1] + 1] == 1:
            print(Fore.RED + 'Cannot move that direction. Please try another')
        else:
            player_pos[1] += 1
            for row in range(len(game_maze)):
                for col in range(len(game_maze[row])):
                    if row == player_pos[0] and col == player_pos[1]:
                        print('X', end=' ')
                    else:
                        print(game_maze[row][col], end=' ')
                print()
    else:
        print(Fore.RED + 'Cannot move that direction. Please try another')

    if player_pos == [len(game_maze) - 1, len(game_maze[0]) - 1]:
        print(Fore.MAGENTA + Style.BRIGHT +
              f'Congratulations, you have reached the goal!\n {celebrate}')
        playsound('sound/trumpet-fanfare-royal-announcement-soundroll-1-00-06.mp3')
        sys.exit(-1)
