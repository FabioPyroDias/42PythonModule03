import sys


if __name__ == "__main__":
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
    argument = 1
    while argument < len(sys.argv):
        print(f"Argument {argument}: {sys.argv[argument]}")
        argument += 1
    print(f"Total arguments: {len(sys.argv)}")
