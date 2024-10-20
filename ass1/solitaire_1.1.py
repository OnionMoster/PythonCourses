# 扑克牌堆
from itertools import chain
from random import seed, shuffle
from collections import defaultdict


def matrix(origin_cards, replace_cards=[]):
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
    for i in range(0, len(origin_cards), 4):
        row = origin_cards[i : i + 4]
        while row and row[-1] == "":
            row.pop()
        output = []
        for idx, card in enumerate(row):
            if card == "":
                if idx != len(row) - 1:
                    output.append("\t")
            else:
                output.append(
                    "\t" + (cards_dict[card] if card in cards_dict else str(card))
                )
        print("".join(output), end="\n")


def first_game():
    CARD_NUM = 52
    JOKER = {10, 11, 12, 23, 24, 25, 36, 37, 38, 49, 50, 51}
    remove_cards = []
    remove_num = 0
    times = 0
    times_words = ["second", "third", "fourth"]

    seed_num = input(f"Please enter an integer to feed the seed() function: ")
    print(f"\nDeck shuffled, ready to start!")

    while times < 4:
        cards_index = 0
        replace_cards = []
        cards_num = CARD_NUM - len(remove_cards)

        if times == 0:
            print("]" * (cards_num))
            print(f"\nStarting first round...\n")
        else:
            print(f"\nAfter shuffling, starting {times_words[times - 1]} round...\n")
        seed(int(seed_num) + int(times))

        # 整理牌，去掉被remove的牌
        cards = sorted(set(range(52)) - set(remove_cards))
        shuffle(cards)
        cards.reverse()
        origin_cards = cards[:16]
        cards_index += 16

        # 每次洗牌后的抽出矩阵
        print("Drawing and placing 16 cards:")
        # 52张牌 - 被抽出的16张 - 上次被移除的牌
        print("]" * (cards_num - 16))
        matrix(origin_cards)

        # 替换
        remove_num = 0
        for i in range(len(origin_cards)):
            if origin_cards[i] in JOKER:
                replace_cards.append({"index": i, "card": ""})
                remove_cards.append(origin_cards[i])
                remove_num += 1
                origin_cards[i] = ""
        # print(remove_cards)
        if remove_num > 0:
            plural = "s" if remove_num > 1 else ""
            print(f"\nPutting {remove_num} picture{plural} aside:")
            matrix(origin_cards)

        if len(remove_cards) == 12:
            print(f"\nYou uncovered all pictures, you won!")
            return

        while len(replace_cards) > 0:
            # 补牌
            remove_num = 0  # 初始化本轮被移出数量
            # 从cards中按顺序摸牌
            for i in range(len(replace_cards)):
                replace_cards[i]["card"] = cards[cards_index]
                cards_index += 1

            # 每次补牌后的抽出矩阵
            print(
                f"\nDrawing and placing {len(replace_cards)} {'cards' if len(replace_cards) > 1 else 'card'}:"
            )
            # print("pickafter", origin_cards)
            print("]" * (cards_num - cards_index), end="\n")
            matrix(origin_cards, replace_cards)

            # 暂存本轮替换牌组 JQK
            tmp_replace_cards = []
            for i in range(len(replace_cards)):
                if replace_cards[i]["card"] in JOKER:
                    tmp_replace_cards.append(replace_cards[i])
                    origin_cards[replace_cards[i]["index"]] = ""
                    remove_cards.append(replace_cards[i]["card"])
                    remove_num += 1
                else:
                    origin_cards[replace_cards[i]["index"]] = replace_cards[i]["card"]

            # print("remove", remove_num)
            if remove_num > 0:
                print(
                    f"\nPutting {int(remove_num)} picture{'s' if remove_num > 1 else ''} aside:"
                )
                matrix(origin_cards)
            replace_cards = tmp_replace_cards

        times += 1

    # print(remove_cards)
    jqk_num = len(remove_cards)
    if jqk_num == 12:
        print(f"\nYou uncovered all pictures, you won!")
    elif times == 4 and jqk_num < 12:
        print(f"\nYou uncovered only {jqk_num} pictures, you lost!")


def play_more_game(num_games, initial_seed):
    JOKER_CARDS = {10, 11, 12, 23, 24, 25, 36, 37, 38, 49, 50, 51}
    uncovered_results = defaultdict(int)

    for game_index in range(num_games):
        seed_value = initial_seed + game_index
        removed_cards = []
        shuffle_round = 0

        while shuffle_round < 4:
            current_card_index = 0
            cards_to_replace = []

            seed(seed_value + shuffle_round)
            cards = sorted(set(range(52)) - set(removed_cards))
            shuffle(cards)
            cards.reverse()
            current_cards = cards[:16]
            current_card_index += 16

            # 替换
            for i in range(len(current_cards)):
                if current_cards[i] in JOKER_CARDS:
                    cards_to_replace.append({"index": i, "card": ""})
                    removed_cards.append(current_cards[i])
                    current_cards[i] = ""

            while len(cards_to_replace) > 0:
                for i in range(len(cards_to_replace)):
                    if current_card_index < len(cards):
                        cards_to_replace[i]["card"] = cards[current_card_index]
                        current_card_index += 1
                    else:
                        # 如果没有足够的牌，跳出补牌循环
                        cards_to_replace = []
                        break

                temp_cards_to_replace = []
                for i in range(len(cards_to_replace)):
                    if cards_to_replace[i]["card"] in JOKER_CARDS:
                        temp_cards_to_replace.append(cards_to_replace[i])
                        current_cards[cards_to_replace[i]["index"]] = ""
                        removed_cards.append(cards_to_replace[i]["card"])
                    else:
                        current_cards[cards_to_replace[i]["index"]] = cards_to_replace[
                            i
                        ]["card"]
                cards_to_replace = temp_cards_to_replace

            shuffle_round += 1

            if len(removed_cards) == 12:
                break

        if len(removed_cards) == 12:
            uncovered_results[12] += 1
        else:
            uncovered_results[len(removed_cards)] += 1

    total_games = sum(uncovered_results.values())
    print("Number of uncovered pictures | Frequency")
    print("----------------------------------------")
    for key in sorted(uncovered_results.keys()):
        probability = (uncovered_results[key] / total_games) * 100
        formatted_probability = f"{probability:.2f}%"
        if probability < 0.5:
            formatted_probability = "0.00%"
        print(f"{key:28} | {formatted_probability:>9}")


play_more_game(500, 11)
