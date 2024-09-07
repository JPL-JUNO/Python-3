import argparse


def main():
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )

    args = parser.parse_args()

    print(f"Hello, {args.name}!")


# Every program or module in Python has a
# name that can be accessed through the
# variable __name__. When the program is
# executing, __name__ is set to “__main__”.

if __name__ == "__main__":
    main()
