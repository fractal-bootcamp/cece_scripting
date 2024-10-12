import click

@click.command()
@click.option('--name', prompt='Project name', help='Name of the project')
def setup(name):
    """Set up React Vite + Express"""
    click.echo(f"Setting up React Vite + Express for project: {name}")
    # TODO: Add implementation for setting up React Vite + Express
