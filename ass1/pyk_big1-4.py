# 扑克牌堆
from itertools import chain
from operator import truediv
from random import seed, shuffle
from collections import defaultdict


def matrix(origin_cards, mode_front=True, replace_cards=[]):
    cards_dict = {
        0: "🂱",
        1: "🂲",
        2: "🂳",
        3: "🂴",
        4: "🂵",
        5: "🂶",
        6: "🂷",
        7: "🂸",
        8: "🂹",
        9: "🂺",
        10: "🂻",
        11: "🂽",
        12: "🂾",
        13: "🃁",
        14: "🃂",
        15: "🃃",
        16: "🃄",
        17: "🃅",
        18: "🃆",
        19: "🃇",
        20: "🃈",
        21: "🃉",
        22: "🃊",
        23: "🃋",
        24: "🃍",
        25: "🃎",
        26: "🃑",
        27: "🃒",
        28: "🃓",
        29: "🃔",
        30: "🃕",
        31: "🃖",
        32: "🃗",
        33: "🃘",
        34: "🃙",
        35: "🃚",
        36: "🃛",
        37: "🃝",
        38: "🃞",
        39: "🂡",
        40: "🂢",
        41: "🂣",
        42: "🂤",
        43: "🂥",
        44: "🂦",
        45: "🂧",
        46: "🂨",
        47: "🂩",
        48: "🂪",
        49: "🂫",
        50: "🂭",
        51: "🂮",
    }
    if len(replace_cards) > 0:
        for card in replace_cards:
            origin_cards[card["index"]] = card["card"]
    if mode_front:
        for i in range(0, len(origin_cards), 4):
            row = origin_cards[i : i + 4]
            print(
                "\t"
                + "\t".join(
                    cards_dict[card] if card in cards_dict else str(card)
                    for card in row
                )
            )


def first_game(init_seed=None):
    CARD_NUM = 52
    JOKER = {10, 11, 12, 23, 24, 25, 36, 37, 38, 49, 50, 51}
    remove_cards = []
    times = 0
    times_words = ["second", "third", "fourth"]
    game_mode_front = False

    if init_seed is None:
        try:
            game_mode_front = True
            seed_num = int(
                input("Please enter an integer to feed the seed() function: ")
            )
        except EOFError:
            return
    else:
        seed_num = init_seed

    game_mode_front and print(f"\nDeck shuffled, ready to start!")

    while times < 4:
        cards_index = 0
        replace_cards = []
        # 本轮牌堆数量
        cards_num = CARD_NUM - len(remove_cards)

        if times == 0:
            game_mode_front and print("]" * (cards_num))
            game_mode_front and print(f"\nStarting first round...\n")
        else:
            game_mode_front and print(
                f"\nAfter shuffling, starting {times_words[times - 1]} round...\n"
            )
        seed(int(seed_num) + int(times))

        # 整理牌，去掉被remove的牌
        cards = sorted(set(range(52)) - set(remove_cards))
        shuffle(cards)
        cards.reverse()
        origin_cards = cards[:16]
        cards_index += 16

        # 每次洗牌后的抽出矩阵
        game_mode_front and print("Drawing and placing 16 cards:")
        # 52张牌 - 被抽出的16张 - 上次被移除的牌
        game_mode_front and print("]" * (cards_num - 16))
        game_mode_front and matrix(origin_cards)

        # 替换
        remove_num = 0
        for i in range(len(origin_cards)):
            if origin_cards[i] in JOKER:
                replace_cards.append({"index": i, "card": ""})
                remove_cards.append(origin_cards[i])
                remove_num += 1
                origin_cards[i] = " "
        # print(remove_cards)
        if remove_num > 0:
            plural = "s" if remove_num > 1 else ""
            game_mode_front and print(f"\nPutting {remove_num} picture{plural} aside:")
            game_mode_front and matrix(origin_cards)
            # 若已找出全部JQK 中断循环
            if len(remove_cards) == 12:
                break

        while len(replace_cards) > 0:
            # 补牌
            remove_num = 0  # 初始化本轮被移出数量
            # 从cards中按顺序摸牌
            for i in range(len(replace_cards)):
                replace_cards[i]["card"] = cards[cards_index]
                cards_index += 1

            # 每次补牌后的抽出矩阵
            game_mode_front and print(
                f"\nDrawing and placing {len(replace_cards)} {'cards' if len(replace_cards) > 1 else 'card'}:"
            )
            game_mode_front and print("]" * (cards_num - cards_index))
            matrix(origin_cards, game_mode_front, replace_cards)

            # 暂存本轮替换牌组 JQK
            tmp_replace_cards = []
            for i in range(len(replace_cards)):
                if replace_cards[i]["card"] in JOKER:
                    tmp_replace_cards.append(replace_cards[i])
                    origin_cards[replace_cards[i]["index"]] = ""
                    remove_cards.append(replace_cards[i]["card"])
                    remove_num += 1

            # print("remove", remove_num)
            if remove_num > 0:
                game_mode_front and print(
                    f"\nPutting {int(remove_num)} picture{'s' if remove_num > 1 else ''} aside:"
                )
                game_mode_front and matrix(origin_cards)
            # 若已找出全部JQK 中断循环
            if len(remove_cards) == 12:
                break

            replace_cards = tmp_replace_cards

        times += 1

    # print(remove_cards)
    jqk_num = len(remove_cards)
    if game_mode_front:
        if times <= 4 and jqk_num == 12:
            game_mode_front and print(f"\nYou uncovered all pictures, you won!")
        elif times == 4 and jqk_num < 12:
            game_mode_front and print(
                f"\nYou uncovered only {jqk_num} pictures, you lost!"
            )
    else:
        return jqk_num


def simulate(games_times: int, init_seed: int):
    uncovered_list = [0] * 13
    for i in range(games_times):
        uncovered = first_game(init_seed + i)
        uncovered_list[uncovered] += 1
    print("Number of uncovered pictures | Frequency")
    print("----------------------------------------")
    for i in range(len(uncovered_list)):
        if uncovered_list[i] > 0:
            print("{:>28d} | {:.2%}".format(i, uncovered_list[i] / games_times))


first_game()
