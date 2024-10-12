import subprocess
import os 
def initialize_project():
# run npm init --> create package.json 
    subprocess.run(["npm", "init"], check=True)

    print("installing dependencies")

# install dependencies (npm i)
    subprocess.run(["npm", "install", "express"], check=True)

print("project initialized")

 if __name__ == "__main__":
  initialize_project()
