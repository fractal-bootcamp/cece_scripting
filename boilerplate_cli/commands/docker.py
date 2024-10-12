import click
import os

@click.command()
@click.option('--name', prompt='Project name', help='Name of the project')
def setup(name):
    """Set up Docker"""
    click.echo(f"Setting up Docker for project: {name}")
   
   # ensure correct project directory 
   os.chdir(name)

   #create docker file
   with open("Dockerfile", "w") as f: 
    f.write('''
    FROM node: 14
    WORKDIR /usr/src/app
    COPY package*.json ./
    RUN npm install
    COPY . . 
    EXPOSE 3000
    CMD [ "node", "backend/server.js" ] 
    ''')

    #create a .dockerignore file 
    with open(".dockerignore", "w") as f:
        f.write('''
        node_modules
        npm-debug.log
        ''')

        click.echo(f"Docker setup complete for project: {name}")

        if __name__ == '__main__':
            setup()
