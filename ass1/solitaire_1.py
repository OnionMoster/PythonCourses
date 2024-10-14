# 扑克牌堆
from itertools import chain
from random import seed, shuffle
from collections import defaultdict


def frist_game():
    cards_num = 51
    Joker = {10, 11, 12, 23, 24, 25, 36, 37, 38, 49, 50, 51}
    remove_cards = 0
    times = 0
    original_matrix = []
    next_matrix = []
    seed_num = input(f"Please enter an integer to feed the seed() function: ")
    add_count = 0

    print(f"\nDeck shuffled, ready to start!")
    print("]" * (cards_num + 1))

    if times < 5:
        if times == 2:
            print(f"\nAfter shuffling, starting second round...\n")
            seed(seed_num + times - 1)
        elif times == 3:
            print(f"\nAfter shuffling, starting third round...\n")
            seed(seed_num + times - 1)
        elif times == 4:
            print(f"\nAfter shuffling, starting fourth round...\n")
            seed(seed_num + times - 1)
        else:
            print(f"\nStarting first round...\n")
            seed(seed_num)
        print("Drawing and placing 16 cards:")
        cards = list(range(cards_num + 1))
        shuffle(cards)
        # print(cards)
        origin = cards[:16]
        # print(first)

        cards_num = cards_num - 15
        print("]" * (cards_num + 1 - remove_cards))

        # 每次洗牌后的矩阵
        for i in range(0, len(origin), 4):
            row = origin[i : i + 4]
            original_matrix.append(row)
            print(row)

            # 取出 J Q K
            new_row = []
            for card in row:
                if card in Joker:
                    new_row.append("\t")
                    remove_cards += 1
                else:
                    new_row.append(str(card))
            next_matrix.append(new_row)

        print(f"\nPutting {remove_cards} pictures aside:\n")

        # 取出 J Q K后的矩阵
        for row in next_matrix:
            print(row)
            if remove_cards == 12:
                print(f"You uncovered all pictures, you won!")
                return ()

        print(f"\nDrawing and placing {remove_cards} cards:")
        print("]" * (cards_num - remove_cards))

        # 从牌堆抽需要的牌
        add = cards[16 : 16 + remove_cards]

        # 补充后的矩阵
        for row in next_matrix:
            add_row = []
            for card in row:
                if card == "\t":
                    add_row.append(add[add_count])
                    add_count += 1
                else:
                    add_row.append(card)
            print(add_row)
        # 继续
        times += 1
    else:
        if 12 - remove_cards > 1:
            print(f"You uncovered only {12 - remove_cards} pictures, you lost!")
        else:
            print(f"You uncovered only 1 picture, you lost!")


frist_game()
