from typing import Annotated

import typer

from .commands import DBCommands, sorter_command

app = typer.Typer(help='Utility for sorting files by their formats', add_completion=False)

db_app = typer.Typer(help='List of commands for working with the database')

app.add_typer(db_app, name='db')


@db_app.command('get-all')
def get_all():
    """Displays all registered sorting formats and their target paths stored in the database."""
    DBCommands().get_all_command()


@db_app.command('add')
def add_item(
    format: Annotated[str, typer.Option('--format', '-f', help='File format')],
    path: Annotated[
        str, typer.Option('--path', '-p', help='The path where files of this format are located')
    ],
):
    """Adds a new file format rule and assigns its destination path."""
    DBCommands().add_item(format, path)


@db_app.command('remove')
def remove_item(name: Annotated[str, typer.Option('--name', '-n', help='Name item')]):
    """Deletes an existing sorting rule by its name."""
    DBCommands().remove_item(name)


@app.command('sorter')
def sorter(output_dir: Annotated[str, typer.Option('--outpur-dir', '-o', help='Output dir')]):
    """Folder containing files to sort."""
    sorter_command(output_dir)
