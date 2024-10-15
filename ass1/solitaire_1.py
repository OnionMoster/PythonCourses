# 扑克牌堆
from itertools import chain
from random import seed, shuffle
from collections import defaultdict


def frist_game():
    cards_num = 52
    Joker = {10, 11, 12, 23, 24, 25, 36, 37, 38, 49, 50, 51}
    remove_cards = []
    times = 1
    original_matrix = []
    next_matrix = []
    cards_index = 16

    seed_num = input(f"Please enter an integer to feed the seed() function: ")
    print(f"\nDeck shuffled, ready to start!")
    print("]" * (cards_num))

    # 这里有一段将数字变成unicode

    while times < 5:
        # 回合数
        times_words = ["second", "third", "fourth"]
        if times == 1:
            print(f"\nStarting first round...\n")
            seed(int(seed_num))
        elif 2 <= times <= 4:
            print(f"\nAfter shuffling, starting {times_words[times - 2]} round...\n")
            seed(int(seed_num) + int(times) - 1)
        print("Drawing and placing 16 cards:")

        # 整理牌，去掉被remove的牌
        cards = sorted(set(range(52)) - set(remove_cards))
        shuffle(cards)
        # print(seed_num, ":", cards)
        origin = cards[:16]
        # print(first)
        showing_cards = []

        # 52张牌 - 被抽出的16张 - 上次被移除的牌
        print("]" * (cards_num - 16 - len(remove_cards)))

        # 每次洗牌后的抽出矩阵
        for i in range(0, len(origin), 4):
            row = origin[i : i + 4]
            original_matrix.append(row)
            showing_cards.extend(row)
            print(row)

        # 取出 J Q K 遍历row
        remove_num = 0
        add_count = 0
        for row in original_matrix:
            new_row = []
            for card in row:
                if card in Joker:
                    remove_num += 1
                    remove_cards.append(card)
                    new_row.append("\t")
                else:
                    new_row.append(str(card))
            next_matrix.append(new_row)

        print(f"\nPutting {int(remove_num)} pictures aside:\n")
        # print("\n取出 J Q K后的矩阵\n")

        # 取出 J Q K后的矩阵
        for row in next_matrix:  # bug
            print(row)

        # 判断条件
        if remove_num == 0:
            times += 1
            break
        elif remove_cards == 12:
            print(f"You uncovered all pictures, you won!")
            return
        else:
            print(f"\nDrawing and placing {int(remove_num)} cards:")
            print("]" * (cards_num - len(remove_cards)))

        # 从牌堆抽需要的牌
        add = cards[cards_index : cards_index + int(remove_num)]
        cards_index += int(remove_num)
        for card in add:
            if card in Joker:
                remove_num += 1
                remove_cards.append(card)
                # 补充后的矩阵
            for row in next_matrix:
                add_row = []
                for card in row:
                    if card == "\t":
                        add_row.append(add[add_count])
                        add_count += 1
                    else:
                        add_row.append(card)

    while times > 5:
        if 12 - len(remove_cards) > 1:
            print(f"You uncovered only {12 - len(remove_cards)} pictures, you lost!")
        else:
            print(f"You uncovered only 1 picture, you lost!")


frist_game()
