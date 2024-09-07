import argparse
import os, sys


def get_args():
    parser = argparse.ArgumentParser(
        description="Rock the Casbah",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    # 定义一个位置参数
    parser.add_argument("positional", metavar="str", help="A positional argument")

    parser.add_argument(
        "-a",
        "--arg",
        help="A named string argument",
        metavar="str",
        type=str,
        default="",
    )

    # 定义一个可选参数，必须是整数
    parser.add_argument(
        "-i",
        "--int",
        help="A named integer argument",
        metavar="int",
        type=int,
        default=0,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="A readable file",
        metavar="FILE",
        type=argparse.FileType("r"),
        default=None,
    )

    parser.add_argument("-o", "--on", help="A boolean flag", action="store_true")

    args = parser.parse_args()

    return parser.parse_args()


def main():
    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f"str_arg = '{str_arg}'")
    print(f"int_arg = '{int_arg}'")
    print(f"file_arg = '{file_arg.name if file_arg else ''}'")
    print(f"flag_arg = '{flag_arg}'")
    print(f"positional = '{pos_arg}'")


if __name__ == "__main__":
    main()
