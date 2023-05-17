#!/usr/bin/env python3
import click
from models import Maze, Game, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers import start_game, move_down, move_left, move_right, move_up, move_up, player_pos

engine = create_engine('sqlite:///maze.db')
Session = sessionmaker(bind=engine)


# quit = True

player_pos = [0, 0]


@click.group()
def cli():
    pass


@cli.command()
@click.option('--username', prompt='Enter a username', help="Choose your username")
def new_user(username):
    # session = Session()
    user = User(username=username)
    # session.add(user)
    # session.commit()
    click.echo(f'New player created: {username}')
    set_difficulty(username=username)


def validate_difficulty(difficulty):
    valid_difficulty = ['easy', 'medium', 'hard']
    if difficulty not in valid_difficulty:
        raise click.BadParameter(
            'Invalid difficulty. Please choose easy, medium, or hard.')
    return difficulty


def set_difficulty(username):
    while True:
        input = click.prompt(
            'Enter a difficulty (easy, medium, hard)')
        difficulty = input.lower()
        try:
            validate_difficulty(difficulty)
            click.echo(f'You chose {difficulty} difficulty.')
            session = Session()
            maze = session.query(Maze).filter(
                Maze.difficulty == difficulty).first()
            start_game(maze, username)
            move()
            break
        except click.BadParameter as e:
            click.echo(e)


def move():
    while True:
        direction = input(
            'Type the direction you want to move in using "up", "down","right", or "left": ')
        print(direction)
        if direction == 'up':
            move_up()
        elif direction == 'down':
            move_down()
        elif direction == 'right':
            move_right()
        elif direction == 'left':
            move_left()
        else:
            click.echo(
                "Invalid direction. Use 'up', 'down','right', or 'left'")
            return


if __name__ == "__main__":
    cli()
