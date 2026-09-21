import sys

from file_manager import organize_folder


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py organize <folder>")
        return

    command = sys.argv[1]
    folder = sys.argv[2]

    if command == "organize":
        organize_folder(folder)
    else:
        print("Unknown command.")


if __name__ == "__main__":
    main()