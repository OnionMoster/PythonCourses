from itertools import chain
from random import seed, shuffle
from collections import defaultdict


def second_game(lost_cards_num=[], lines=[], done=[]):
    if done:
        print(f"All cards have been placed, you won!\n")
    else:
        print(f"{lost_cards_num} cards could not be placed, you lost!\n")
    print(f"There are {lines} lines of output; what do you want me to do?")
    select = input(
        f"Enter: q to quit\n\t a last line number (between 1 and {lines})\n\t  a first line number (between -1 and {-lines})\n\t a range of lines numbers (of the form m--n with 1 <= m <= n <= {lines}\n)"
    )

    select = select.replace(" ", "").replace("\t", "")
    if select == "q":
        return  # 第一个
    elif int(lines) >= select >= 1:
        return  # 第二个
    elif "-" in str(select) and -1 >= select >= int(-lines):
        return  # 第三个
    elif "--" in str(select):
        parts = select.split("--")
        m = parts[0]
        n = parts[1]
        if 1 <= m <= n <= int(lines):
            return  # 第四个
    else:
        return second_game()


def play_game():
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
        50: "🂬",
        51: "🂭",
    }
    lost_cards_num = 0
    lines = 0
    done = True
    cards_num = 52
    seed_num = input(f"Please enter an integer to feed the seed() function: \n")
    cards = sorted(set(range(52)))
    seed(seed_num)
    shuffle(cards)
    print("\nDeck shuffled, ready to start!")
    print("[" * cards_num)
