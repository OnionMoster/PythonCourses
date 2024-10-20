from itertools import chain
from collections import defaultdict
from random import seed, shuffle

suits = {
    "Hearts": 0x1F0B1,
    "Diamonds": 0x1F0C1,
    "Clubs": 0x1F0D1,
    "Spades": 0x1F0A1,
}


def init_game_one(s):
    all_card_dict = {}
    all_card = []
    idx = 0
    for item in s:
        for x in range(0, 14):
            if x == 11:
                continue
            all_card_dict[idx] = chr(s[item] + x)
            all_card.append(idx)
            idx = idx + 1
    return all_card_dict, all_card


def shaffle_one(arr, seeds):
    seed(seeds)
    shuffle(arr)
    return arr


def calculate_round(number):
    specials = {1: "first", 2: "second", 3: "third"}
    if number in specials:
        return specials[number]
    suffixes = {1: "st", 2: "nd", 3: "rd"}
    if 10 <= number % 100 <= 20:
        suffix = "th"
    else:
        suffix = suffixes.get(number % 10, "th")
    return str(number) + suffix


# 接收两个参数,一个是 输入的字符串 另一个 是 一共有多少行
# 什么是正确的输入？
# 1. 不能有 +
# 2. 不能有 - 2
# 3. 不能有 -- 2
def process_query(ini_q, upper_bound):
    str_q = ""
    for x in range(len(ini_q)):
        if ini_q[x] != " " and ini_q[x] != "\t" and ini_q[x] != "\n":
            # 保证没有 +
            if ini_q[x] == "+":
                return False
            try:
                # strq = '' 且当前我遇到了 '- 9' 或者 '-    9' '-'
                if (
                    ini_q[x] == "-"
                    and (ini_q[x + 1] == " " or ini_q[x + 1] == "\t")
                    and not str_q
                ):
                    return False
            except:
                return False
            str_q += ini_q[x]
    if str_q == "q":
        return "q"
    try:
        res = int(str_q)
        if 0 < res <= upper_bound:
            return [res]
        if -upper_bound <= res < 0:
            return [res]
        return False
    except:
        res = []
        n_r = ""
        count = 0
        for item in str_q:
            if item != "-":
                n_r += item
            else:
                if n_r:
                    res.append(n_r)
                    n_r = ""
                count += 1
        else:
            res.append(n_r)
        if count != 2 or len(res) != 2:
            return False
        try:
            num1, num2 = int(res[0]), int(res[1])
            if 0 < num1 <= num2 <= upper_bound:
                return [num1, num2]
        except ValueError:
            return False


def play_game(seed_num):
    total_placed, round = 0, 0
    cards = list(range(52))[::-1]
    cards = shaffle_one(cards, seed_num)
    current_stucks_expect_value = [0, 13, 26, 39, 12, 25, 38, 51]
    current_opened, current_opened_to = [], 0

    while cards:
        round_placed, changed = 0, True

        while changed:
            changed = False

            # 尝试打开新的牌，如果当前没有打开的牌
            if not current_opened and current_opened_to < len(cards):
                upper_bound = min(current_opened_to + 3, len(cards))
                current_opened += cards[current_opened_to:upper_bound]
                current_opened_to = upper_bound
                changed = True
                continue

            # 如果有牌可处理
            if current_opened:
                current_card = current_opened[-1]

                if current_card in current_stucks_expect_value:
                    round_placed += 1
                    changed = True
                    cards.remove(current_opened.pop())
                    current_opened_to -= 1
                    index = current_stucks_expect_value.index(current_card)
                    current_stucks_expect_value[index] += 1 if index < 4 else -1
                elif current_opened_to < len(cards):
                    upper_bound = min(current_opened_to + 3, len(cards))
                    current_opened += cards[current_opened_to:upper_bound]
                    current_opened_to = upper_bound
                    changed = True

        total_placed += round_placed
        if round_placed == 0:
            break
        round += 1

    return total_placed


def open_cards(cards, current_opened, current_opened_to):
    upper_bound = min(current_opened_to + 3, len(cards))
    current_opened += cards[current_opened_to:upper_bound]
    current_opened_to = upper_bound
    return current_opened, current_opened_to, True


def run_self():
    content = []
    total_palced = 0
    seed_num = 0
    try:
        seed_num = int(input("Please enter an integer to feed the seed() function: "))
    except ValueError:
        return
    all_dicts, cards = init_game_one(suits)
    all_stucks = [[], [], [], [], [], [], [], []]
    current_stucks_expect_value = [0, 13, 26, 39, 12, 25, 38, 51]
    content.append(f"Deck shuffled, ready to start!\n")
    content.append("]" * 52 + "\n")
    round = 0
    cards = shaffle_one(cards, seed_num)
    cards = cards[::-1]
    # 游戏进行的过程
    while cards:
        round_placed = 0
        content.append("\n")
        content.append(
            f"Starting to draw 3 cards (if possible) again and again for the {calculate_round(round+1)} time...\n"
        )
        content.append("\n")
        current_opened_to = 0
        current_opened = []
        # 开始一轮
        changed = True
        if len(current_opened) == 0 and current_opened_to < len(cards):
            current_opened, current_opened_to, changed = open_cards(
                cards, current_opened, current_opened_to
            )
        while changed:
            # 如果牌库空了,掀起三张牌
            changed = False
            # 如果准备牌库没牌了
            if not current_opened:
                content.append("]" * (len(cards) - current_opened_to) + "\n")
                # 打印当前的使用牌库
                content.append("\n")
                # 打印当前整理好的牌库
                temp_res = []
                for item in all_stucks:
                    length = len(item)
                    print(item)
                    if length > 0:
                        last = all_dicts[item[-1]]
                        final_str = ("[" * (length - 1) + last).ljust(15)
                        temp_res.append(final_str)
                    else:
                        temp_res.append(" " * 15)
                content.append("    " + "".join(temp_res[0:4]).rstrip() + "\n")
                content.append("    " + "".join(temp_res[4:8]).rstrip() + "\n")
                if current_opened_to < len(cards):
                    current_opened, current_opened_to, changed = open_cards(
                        cards, current_opened, current_opened_to
                    )
                    if round_placed > 0:
                        content.append("\n")
                    continue
                else:
                    break
            current_card_picture = all_dicts[current_opened[-1]]
            current_card = current_opened[-1]
            # 打印当前的准备牌库
            content.append("]" * (len(cards) - current_opened_to) + "\n")
            # 打印当前的使用牌库
            content.append(
                "[" * (len(current_opened) - 1) + current_card_picture + "\n"
            )
            # 打印当前整理好的牌库
            temp_res = []
            for item in all_stucks:
                length = len(item)
                if length > 0:
                    last = all_dicts[item[-1]]
                    final_str = ("[" * (length - 1) + last).ljust(15)
                    temp_res.append(final_str)
                else:
                    temp_res.append(" " * 15)
            content.append("    " + "".join(temp_res[0:4]).rstrip() + "\n")
            content.append("    " + "".join(temp_res[4:8]).rstrip() + "\n")
            if current_opened_to < len(cards):
                content.append("\n")
            # 进行check
            # 如果开局翻开的三张牌合法会掀开一张
            if current_card in current_stucks_expect_value:
                if current_opened_to >= len(cards):
                    content.append("\n")
                changed = True
                round_placed += 1
                current_card = current_opened.pop()
                cards.remove(current_card)
                current_opened_to -= 1
                index = current_stucks_expect_value.index(current_card)

                if current_card in [12, 25, 38, 51]:
                    index = 4 + [12, 25, 38, 51].index(current_card)
                all_stucks[index].append(current_card)
                if index < 4:
                    if len(all_stucks[index]) == 1:
                        content.append("Placing one of the base cards!\n")
                    else:
                        content.append("Making progress on an increasing sequence!\n")
                    current_stucks_expect_value[index] += 1
                else:
                    if len(all_stucks[index]) == 1:
                        content.append("Placing one of the base cards!\n")
                    else:
                        content.append("Making progress on an decreasing sequence!\n")
                    current_stucks_expect_value[index] -= 1
            # 如果开局掀开的三张牌不合法会再掀开三张, 不影响
            elif current_opened_to < len(cards):
                current_opened, current_opened_to, changed = open_cards(
                    cards, current_opened, current_opened_to
                )
        total_palced += round_placed
        if round_placed == 0:
            break
        round += 1
    # 打印的第二行 就是 游戏可接龙的牌的张数
    if total_palced < 52:
        print(f"\n{52-total_palced} cards could not be placed, you lost!\n")
    else:
        print(f"\nAll cards have been placed, you won!\n")

    # for item in content:
    #     print(item, end='')
    # 获取游戏的行数
    lens = len(content)
    print(f"There are {lens} lines of output; what do you want me to do?\n")
    # 初始化查询行数
    query_str = ""
    while True:
        try:
            query_str = input(
                f"Enter: q to quit\n\
       a last line number (between 1 and {lens})\n\
       a first line number (between -1 and -{lens})\n\
       a range of line numbers (of the form m--n with 1 <= m <= n <= {lens})\n\
       "
            )
            result = process_query(query_str, len(content))
            if not result:
                raise ValueError
            # print(result)
            if result[0] == "q" and len(result) == 1:
                break
            print()
            if len(result) == 1:
                if result[0] > 0:
                    res_content = "".join(content[0 : result[0] :])
                    print(res_content)
                else:
                    res_content = "".join(content[result[0] : :])
                    print(res_content)
            if len(result) == 2:
                res_content = "".join(content[result[0] - 1 : result[1]])
                print(res_content)
        except ValueError:
            print()


def simulate(game_num, seed_num):
    all_piecute_result = defaultdict(int)
    # 游戏次数进行遍历
    for games in range(game_num):
        current_seed = seed_num + games
        result_n = play_game(current_seed)
        result_n = 52 - result_n
        all_piecute_result[result_n] += 1


run_self()
