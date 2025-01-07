import click
from src.database import initialize_database

@click.group()
def cli():
    """Apex AI CLI."""
    pass

@cli.command()
def initdb():
    """Initialize the database."""
    initialize_database()
    click.echo("Database initialized.")

@cli.command()
def runserver():
    """Run the development server."""
    from src.main import app
    app.run(debug=True, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    cli()
