import click #package for creating command line interfaces 
import os #provides a way of using operating system dependent functionality 
import subprocess # run external commands or programs from within Python script -- enables bidirectional communication - send input & capture output 

# used for creating CLIs in python @click infront of function transforms this into command-line command 
# "The function below this decorator should be treated as a command that can be run from the command line."
@click.command()
# define a command line otpion for the project name 
# allows 3 options 1) user provides name ; 2) user doesnt provide name & is prompted with 'Project name' or they are for help
@click.option('--name', prompt='Project name', help='Name of the project')
def setup(name): # in all cases the name is setup here 
    """Set up Prisma""" #docstring that provides a breif description of the function 

    # print message to the console with click.echo
    click.echo(f"configuring prisms for Prisma: {name}")

# automatically change current working directory based on the inputted name provided by the user 
os.chdir(name) # preparing environment for next steps of setup process 

click.echo("initializing prisma shapes...")

# using subprocess to excecute shell commands running 'npx prisma init' command
# check=True means it will raise an exception if the command fails
subprocess.run(["npx", "prisma", "init"], check=True)

#open schema.prisma file in append mode ("a" --> append mode opens file for writing -> but does not overwrite -> new data added to end of file)
# here append mode is ensuring that you are adding new user model to existing prisma schema file without erasing any other models or configs 
# with statement ensures file is properly closed after were done -- even if error occurs 
with open("prisma/schema.prisma", "a") as f: #assigns opened file object to the variable f (which is what we use to interact with the file)

# write a user model definition to the file 
f.write('''
Model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
}
''')

#provide feedback - print a message
click.echo("prisma client is molding databases...")

#run 'npm install @prisma/client' command with subprocess 
subprocess.run(["npm", "install", "@prisma/client"], check=True)

#send message to inform user of completed task
click.echo(f"data shapes have been configured: {name}")

#if this script is run directly then call the setup() function 
if __name__ == '__main__':
    setup() 