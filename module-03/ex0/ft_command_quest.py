"""Exercise 0: Command Quest.

Demonstrates how to read and summarize command-line arguments.
"""

import sys


def main(argv):
    """Print a summary of the provided command-line arguments."""
    print("=== Command Quest ===")

    program_name = argv[0] if argv else ""
    if len(argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print("Total arguments: 1")
        return

    print(f"Program name: {program_name}")
    print(f"Arguments received: {len(argv) - 1}")
    for index, arg in enumerate(argv[1:], 1):
        print(f"Argument {index}: {arg}")
    print(f"Total arguments: {len(argv)}")


if __name__ == "__main__":
    main(sys.argv)
