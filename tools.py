import subprocess
import sys

def install_package(package_name):
    try:
        __import__(package_name)
        print(f"The package '{package_name}' is already installed.")
    except ImportError:
        print(f"The package '{package_name}' is not installed. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"The package '{package_name}' has been installed successfully.")

# Example usage
install_package('matplotlib')






