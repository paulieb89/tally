import json
import os
from pathlib import Path

import click


def _store():
    return Path(os.environ.get("TALLY_STORE", Path.home() / ".tally.json"))


def _load():
    path = _store()
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text())


def _save(data):
    _store().write_text(json.dumps(data, indent=2))


@click.group()
def cli():
    """Count things from the command line."""


@cli.command()
@click.argument("name")
def add(name):
    """Increment NAME by 1."""
    try:
        data = _load()
    except FileNotFoundError:
        data = {}
    data[name] = data.get(name, 0) + 1
    _save(data)
    click.echo(f"{name}: {data[name]}")


@cli.command()
def show():
    """Print all counters."""
    data = _load()  # raises FileNotFoundError if no counters have been added yet
    if not data:
        click.echo("No counters yet.")
        return
    for name, count in data.items():
        click.echo(f"{name}: {count}")
