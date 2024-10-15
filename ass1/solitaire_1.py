# 扑克牌堆
from itertools import chain
from random import seed, shuffle
from collections import defaultdict


def frist_game():
    cards_num = 51
    Joker = {10, 11, 12, 23, 24, 25, 36, 37, 38, 49, 50, 51}
    remove_cards = []
    times = 1
    original_matrix = []
    next_matrix = []
    cards_index = 16

    seed_num = input(f"Please enter an integer to feed the seed() function: ")
    print(f"\nDeck shuffled, ready to start!")
    print("]" * (cards_num + 1))

    if times < 5:
        if times == 2:
            print(f"\nAfter shuffling, starting second round...\n")
            seed(int(seed_num + times - 1))
        elif times == 3:
            print(f"\nAfter shuffling, starting third round...\n")
            seed(int(seed_num + times - 1))
        elif times == 4:
            print(f"\nAfter shuffling, starting fourth round...\n")
            seed(int(seed_num + times - 1))
        elif times == 1:
            print(f"\nStarting first round...\n")
            seed(int(seed_num))
        print("Drawing and placing 16 cards:")
        cards = sorted(set(range(52)) - set(remove_cards))
        shuffle(cards)
        # print(seed_num, ":", cards)
        origin = cards[:16]
        cards_num = cards_num - 15 
        # print(first)
        showing_cards = []

        print("]" * (cards_num - len(remove_cards)))

        # 每次洗牌后的矩阵
        for i in range(0, len(origin), 4):
            row = origin[i : i + 4]
            original_matrix.append(row)
            showing_cards.extend(row)
            print(row)

        # 取出 J Q K
        while any(card in Joker for card in showing_cards):
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
            print("remove_num",remove_num)

            print(f"\nPutting {int(remove_num)} pictures aside:\n")
            print("\n取出 J Q K后的矩阵\n")
            # 取出 J Q K后的矩阵

            for row in next_matrix:
                print(row)
                if remove_cards == 12:
                    print(f"You uncovered all pictures, you won!")
                    return ()

            print(f"\nDrawing and placing {int(remove_num)} cards:")
            print("]" * (cards_num - len(remove_cards)))

            # 从牌堆抽需要的牌
            add = cards[cards_index : cards_index + int(remove_num)]
            cards_index += int(remove_num)

            # 补充后的矩阵
            print("\n补充后的矩阵\n")
            for row in next_matrix:
                add_row = []
                for card in row:
                    if card == "\t":
                        add_row.append(add[add_count])
                        add_count += 1
                    else:
                        add_row.append(card)
                print(add_row)
        times += 1
    else:
        if 12 - len(remove_cards) > 1:
            print(f"You uncovered only {12 - len(remove_cards)} pictures, you lost!")
        else:
            print(f"You uncovered only 1 picture, you lost!")


frist_game()
