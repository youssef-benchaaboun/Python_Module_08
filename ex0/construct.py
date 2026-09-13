import os
import site
import sys


def main() -> None:
    if sys.prefix != sys.base_prefix:
        print("Inside virtual environment")
        print(f"Python: {sys.executable}")
        print(f"Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment path: {sys.prefix}")
        print(f"Packages path: {site.getsitepackages()[0]}")
    else:
        print("Outside virtual environment")
        print(f"Python: {sys.executable}")
        print("No virtual environment detected")
        print("Create one with:")
        print("python3 -m venv matrix_env")
        print("Activate it with:")
        print("source matrix_env/bin/activate")


if __name__ == "__main__":
    main()
