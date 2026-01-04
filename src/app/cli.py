import typer
from rich import print

app = typer.Typer(no_args_is_help=True)


@app.command()
def hello(name: str = "world"):
    """Smoke command for local runs and CI."""
    print(f"[bold green]Hello,[/bold green] {name}!")


if __name__ == "__main__":
    app()
