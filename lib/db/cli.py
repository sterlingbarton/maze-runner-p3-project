#!/usr/bin/env python3
import click
from models import Maze, Game, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from helpers import *

engine = create_engine('sqlite:///maze.db')
Session = sessionmaker(bind=engine)
# quit = True


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


def validate_difficulty(difficulty):
    valid_difficulty = ['easy', 'medium', 'hard']
    if difficulty not in valid_difficulty:
        raise click.BadParameter(
            'Invalid difficulty. Please choose easy, medium, or hard.')
    return difficulty


@cli.command()
@click.option('--difficulty', help='Choose level of difficulty')
def set_difficulty(difficulty):
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
            start_game(maze)
            break
        except click.BadParameter as e:
            click.echo(e)


if __name__ == "__main__":
    cli()
