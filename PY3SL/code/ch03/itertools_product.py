"""
@Title: product
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 21:37:26
@Description: 
"""

from itertools import product, chain

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')

DECK = list(
    product(
        chain(range(2, 11), FACE_CARDS),
        SUITS,
    )
)

for card in DECK:
    print("{:>2}{}".format(*card), end=" ")
    if card[1] == SUITS[-1]:
        # 遇到 S 直接换行
        print()
print()
# To change the order of the cards,
# change the order of the arguments to product().

DECK = list(
    product(SUITS,
            chain(range(2, 11), FACE_CARDS)),
)
for card in DECK:
    print("{:>2}{}".format(card[1], card[0]), end=" ")
    if card[1] == FACE_CARDS[-1]:
        print()
