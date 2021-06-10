import os
from enum import Enum

import typer
from rich.console import Console
from rich.syntax import Syntax
from rich.traceback import install

from . import search

# Initiate Rich traceback handlers
install()

console = Console()
error_console = Console(stderr=True, style="bold red")

app = typer.Typer(name="cetus", help="Cetus Cearcher")
app.add_typer(search.app, name="search", help="Search Cetus")


class index(str, Enum):
    dns = "dns"
    certstream = "certstream"


@app.command(help="Show example result data")
def example(
    index: index = typer.Argument(..., case_sensitive=False),
    raw: bool = typer.Option(
        False, "--raw", help="Print raw output instead of pretty printed"
    ),
):

    path = os.path.dirname(os.path.abspath(__file__))
    file = f"{path}/examples/{index.value}.json"
    formatted_example = Syntax.from_path(file)

    if not raw:
        console.print(formatted_example)
    else:
        with open(file) as raw_example:
            print(raw_example.read())
