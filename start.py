#run this to install libraries
import subprocess
import sys

# Function to install a package
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install packages from requirements.txt
def install_requirements(requirements_file='requirements.txt'):
    with open(requirements_file, 'r') as file:
        for line in file:
            install(line.strip())

# Call the function to install requirements
install_requirements()