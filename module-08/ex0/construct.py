import sys
import os
import site


def matrix_sensor() -> None:
    try:
        # sys.base_prefix points to the global Python installation.
        # sys.prefix points to the currently active Python environment.
        # If they are different, it means we are running inside a virtual environment.
        is_in_venv = sys.prefix != sys.base_prefix
        if is_in_venv:
            print("MATRIX STATUS: Welcome to the construct\n")
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
            print(f"Environment Path: {sys.prefix}")
            print()
            print(
                "SUCCESS: You're in an isolated environment!\n"
                "Safe to install packages without affecting\n"
                "the global system."
            )
            print()
            print("Package installation path:")
            print(site.getsitepackages()[0])
        else:
            print("MATRIX STATUS: You're still plugged in\n")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected")
            print()
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print()
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env")
            print("Scripts")
            print("activate # On Windows")
            print("\nThen run this program again.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    matrix_sensor()
