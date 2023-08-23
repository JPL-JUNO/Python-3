#!/usr/bin/env python3
# """
# @Author : 19243 <19243@LAPTOP-FV4E46FR>
# @Date   : 2023-08-23
# @Purpose: Rock the Casbah
# """

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("word", metavar="word", help="A word")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    # Namespace instance
    args = get_args()
    word = args.word
    print(word)
    article = "an" if word[0].lower() in "aeiou" else 'a'

    print(f"Ahoy, Caption, {article} {word} off the larboard bow!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
