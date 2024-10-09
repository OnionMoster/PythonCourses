from itertools import chain
from random import seed, shuffle
from collections import defaultdict


def frist_game():
    # 开始
    n = 52
    unicode_cards = []
    remove_cards = 0
    x = 0  # 每排哪些
    seed_num = input(f"Please enter an integer to feed the seed() function:")

    # 第一次
    print(f"\nDeck shuffled, ready to start!")
    print("]" * n)
    seed(seed_num)
    cards = list(range(n))
    shuffle(cards)
    first = cards[:16]
    # print(first)
    while x < len(first):
        print(first[x], first[x + 1], first[x + 2], first[x + 3])
        x += 4


frist_game()
