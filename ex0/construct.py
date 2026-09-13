import os
import site
import sys


def is_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if is_virtual_environment():
        package_paths = site.getsitepackages()
        package_path = package_paths[0] if package_paths else "Unavailable"
        print("MATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print(f"\nPackage installation path:\n{package_path}")
    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"\nCurrent Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
