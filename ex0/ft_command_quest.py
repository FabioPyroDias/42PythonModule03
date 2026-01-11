import sys


def print_params() -> None:
    """"""
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) != 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
    for index in range(1, len(sys.argv)):
        print(f"Argument {index}: {sys.argv[index]}")
    print(f"Total arguments: {len(sys.argv)}")
