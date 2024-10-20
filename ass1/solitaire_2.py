from itertools import chain
from random import seed, shuffle
from collections import defaultdict


# 剩下的牌数量，总行数，是否完成
def user_control(lost_cards_num=[], lines=[], done=[]):
    if done:
        print(f"All cards have been placed, you won!\n")
    else:
        print(f"{lost_cards_num} cards could not be placed, you lost!\n")
    print(f"There are {lines} lines of output; what do you want me to do?")
    select = ""
    select = input(
        f"Enter: q to quit
        \n\t a last line number (between 1 and {lines})
        \n\t  a first line number (between -1 and {-lines})
        \n\t a range of lines numbers (of the form m--n with 1 <= m <= n <= {lines}\n)"
    )


def user_select(select, lines):
    for x in range(len(select)):
        if select[x] != " " and select[x] != "\t" and select != "\n":
            if select[x] == "+":
                return False
            try:
                if (
                    select[x] == "-"
                    and (select[x + 1] == " " or select[x + 1] == "\t")
                    and not select
                ):
                    return False
            except:
                return False
    if select == "q":
        return "q"
    try:
        if int(lines) >= int(select) > 0:
            return int(select)  # 第二个
        elif 0 > int(select) >= int(-lines):
            return int(select)  # 第三个
        return False
    except:
        ranges = select.split("--")
        if len(ranges) != 2:
            return False
        try:
            m, n = int(ranges[0]), int(ranges[1])
            if 0 < m <= n <= len(lines):
                return [m, n]
        except ValueError:
            return False


# 回合数的输出 (Starting to draw 3 cards (if possible) again and again for the {number} time...)
def round(number):
    specials = {1: "first", 2: "second", 3: "third"}
    if number in specials:
        return specials[number]
    suffixes = {1: "st", 2: "nd", 3: "rd"}
    if 10 <= number % 100 <= 20:
        suffix = "th"
    else:
        suffix = suffixes.get(number % 10, "th")
    return str(number) + suffix


def play_data(suits):
    card_dict = {}
    card_idx = 0
    for item in card_dict:
        for i in range(0, 14):
            if i != 11:
                card_dict[card_idx] = chr(card_dict[item] + i)
                card_idx += 1
    return card_idx, list(range(52))


def play_game():
    # suits = {
    #     "Hearts": 0x1F0B1,
    #     "Diamonds": 0x1F0C1,
    #     "Clubs": 0x1F0D1,
    #     "Spades": 0x1F0A1,
    # }
    seed_num = 0
    try:
        seed_num = int(input("Please enter an integer to feed the seed() function: "))
    except ValueError:
        return
    all_dict, card = play_data()
    main_stuck = [[], [], [], [], [], [], []]  # 这里可能导致错误
    main_cards = [0, 13, 26, 39, 12, 25, 38, 51]
    play_times = 0
    play_round = 0
    cards = sorted(set(range(52)))
    seed(seed_num)
    shuffle(cards)
    cards.reverse()
    # print(cards)

    # 成功放进main_stuck的卡牌数
    placed_count = 0

    content = []  # 打印内容
    # 开始游戏
    print(f"Deck suffled, ready to start!")
    print("]" * 52 + "\n")
    if len(cards) > 0:
        print(
            f"Starting to draw 3 cards (if possible) again and again for the {round(play_round + 1)} time...\n"
        )
        # 成功接龙
        place_num = 0
        # 已经翻开
        lost_cards = []
        # 翻开哪张
        lost_index = 0
        change = True
        # 判断是否有右派
        if len(lost_cards) == 0 and len(cards) > 0:
            # lost_cards, lost_index true
            # 能翻几张
            upper_bound = min(lost_index + 3, len(cards))
            lost_cards += cards[lost_index:upper_bound]
            lost_index = upper_bound
            change = True
        while change:
            change = False
            if not lost_cards:
                print("]" * (len(cards) - lost_index))
                print("\n")  # 注意
                # 8个牌堆
                stucks_8 = []
                for item in main_stuck:
                    length = len(main_stuck[item])
                    if length > 0:
                        last = all_dict[stucks_8[item][-1]]
                        last_card = all_dict[last]
                        final_str = "[" * (length - 1) + last_card
                        stucks_8.append(final_str)
                    else:
                        stucks_8.append("" * 15)
                print("    " + "".join(stucks_8[0:4]).rsplit())
                print("    " + "".join(stucks_8[4:8]).rsplit())
                if lost_index < len(cards):
                    print("\n")
                if 

        placed_count += place_num
        if place_num == 0:
            pass
        pass
    # debug
    for item in content:
        print(content, end="")


play_game()
