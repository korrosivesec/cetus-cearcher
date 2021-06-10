import json
from datetime import datetime

import requests
import typer
from rich.console import Console
from rich.syntax import Syntax
from rich.traceback import install

from .config import api_key, api_url

# Initiate Rich traceback handlers
install()

app = typer.Typer()
console = Console()
error_console = Console(stderr=True, style="bold red")

now = datetime.now().replace(microsecond=0).isoformat()


def process_query(index, query, start, end, raw, metadata):
    start = start.replace(microsecond=0).isoformat()
    end = end.replace(microsecond=0).isoformat()
    results = None

    if index == "DNS":
        query_string = (
            f"host.raw:{query} AND collection_timestamp:[{start} TO {end}]&index=dns"
        )
    else:
        query_string = f"data.leaf_cert.all_domains:{query} AND collection_timestamp:[{start} TO {end}]&index=certstream"

    with console.status(f"[bold green]Searching Cetus {index} index..."):
        results = requests.get(
            f"{api_url}/api/query?q={query_string}",
            headers={"Authorization": f"Token {api_key}"},
        )
        try:
            # Validates JSON response and convert to Python dict
            data = json.loads(results.text)
        except ValueError:
            error_console.print("Error: Response did not include valid JSON")
            error_console.print_exception()
            return

    if not metadata:
        data = data["data"]["es_response"]
        if not data:
            if not raw:
                console.print(":pile_of_poo: No results found.")
            else:
                print(json.dumps(data))
            return

    formatted_data = Syntax(json.dumps(data, indent=4), "json")
    console.print(formatted_data) if not raw else print(json.dumps(data))


@app.command()
def dns(
    query: str = typer.Argument(..., help="Lucene formatted query."),
    start: datetime = typer.Option(..., help="Beginning of search range. Required."),
    end: datetime = typer.Option(
        str(now), help="End of search range. If omitted, end == now"
    ),
    raw: bool = typer.Option(
        False, "--raw", help="Print raw output instead of pretty printed"
    ),
    metadata: bool = typer.Option(
        False, "--metadata", help="Include metadata in output"
    ),
):
    """
    Search the Cetus DNS index
    """
    process_query("DNS", query, start, end, raw, metadata)


@app.command()
def certstream(
    query: str = typer.Argument(..., help="Lucene formatted query."),
    start: datetime = typer.Option(..., help="Beginning of search range. Required."),
    end: datetime = typer.Option(
        str(now), help="End of search range. If omitted, end == now"
    ),
    raw: bool = typer.Option(
        False, "--raw", help="Print raw output instead of pretty printed"
    ),
    metadata: bool = typer.Option(
        False, "--metadata", help="Include metadata in output"
    ),
):
    """
    Search the Cetus Certstream index
    """
    process_query("Certstream", query, start, end, raw, metadata)
