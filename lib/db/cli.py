#!/usr/bin/env python3
import click
from models import Maze, Game, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers import start_game, move_down, move_left, move_right, move_up, move_up
from colorama import Fore, Back, Style

engine = create_engine('sqlite:///maze.db')
Session = sessionmaker(bind=engine)


player_pos = [0, 0]


@click.group()
def cli():
    pass


@cli.command()
@click.option('--username', prompt=(click.style('Enter a username', fg='green')), help="Choose your username")
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
        raise click.BadParameter(click.style(
            'Invalid difficulty. Please choose easy, medium, or hard.', fg='red'))
    return difficulty


def set_difficulty(username):
    while True:
        input = click.prompt(click.style(
            'Enter a difficulty (easy, medium, hard)', fg='green'))
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
        direction = input(click.style(
            'Type the direction you want to move in using "up", "down","right", or "left": ', fg='green'))
        if direction == 'up':
            move_up()
        elif direction == 'down':
            move_down()
        elif direction == 'right':
            move_right()
        elif direction == 'left':
            move_left()
        else:
            click.echo(click.style(
                "Invalid direction. Use 'up', 'down','right', or 'left'", fg='red'))


if __name__ == "__main__":
    cli()
