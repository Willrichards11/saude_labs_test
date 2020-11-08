import sqlite3

import click
from flask import g
from flask.cli import with_appcontext
import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = f"sqlite:///{BASEDIR}/data.db"


def get_db():
    """
    Assign the database connection to flask.g and assign row factory.
    :return: the database connection
    """
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    """
    Close the database connection
    """
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """
    Get the db
    """
    db = get_db()
    return db


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
