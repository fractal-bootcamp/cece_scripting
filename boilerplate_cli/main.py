
import click
from .commands import react_express, prisma, docker

@click.group()
def cli():
    """Boilerplate generator for React Vite + Express with Prisma and Docker."""
    pass

cli.add_command(react_express.setup, name="react-express")
cli.add_command(prisma.setup, name="prisma")
cli.add_command(docker.setup, name="docker")

if __name__ == '__main__':
    cli()
