from itertools import chain
from collections import defaultdict
from random import seed, shuffle

suits = {
    "Hearts": 0x1F0B1,
    "Diamonds": 0x1F0C1,
    "Clubs": 0x1F0D1,
    "Spades": 0x1F0A1,
}


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


def process_query(select, upper_bound):
    str_select = ""
    for x in range(len(select)):
        if select[x] != " " and select[x] != "\t" and select[x] != "\n":
            if select[x] == "+":
                return False
            try:
                if (
                    select[x] == "-"
                    and (select[x + 1] == " " or select[x + 1] == "\t")
                    and not str_select
                ):
                    return False
            except:
                return False
            str_select += select[x]
    if str_select == "q":
        return "q"
    try:
        res = int(str_select)
        if 0 < res <= upper_bound:
            return [res]
        if -upper_bound <= res < 0:
            return [res]
        return False
    except:
        res = []
        n_r = ""
        count = 0
        for item in str_select:
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
    all_card_dict = {}
    all_card = []
    idx = 0
    for item in suits:
        for x in range(0, 14):
            if x == 11:
                continue
            all_card_dict[idx] = chr(suits[item] + x)
            all_card.append(idx)
            idx += 1

    all_dicts, cards = all_card_dict, all_card
    all_stucks = [[], [], [], [], [], [], [], []]
    current_stucks_expect_value = [0, 13, 26, 39, 12, 25, 38, 51]
    content.append(f"Deck shuffled, ready to start!\n")
    content.append("]" * 52 + "\n")
    round = 0
    seed(seed_num)
    shuffle(cards)
    cards = cards[::-1]
    while cards:
        round_placed = 0
        content.append("\n")
        content.append(
            f"Starting to draw 3 cards (if possible) again and again for the {calculate_round(round+1)} time...\n"
        )
        content.append("\n")
        current_opened_to = 0
        current_opened = []
        changed = True
        if len(current_opened) == 0 and current_opened_to < len(cards):
            current_opened, current_opened_to, changed = open_cards(
                cards, current_opened, current_opened_to
            )
        while changed:
            changed = False
            if not current_opened:
                content.append("]" * (len(cards) - current_opened_to) + "\n")
                content.append("\n")
                temp_res = []
                i = 0
                while i < len(all_stucks):
                    item = all_stucks[i]
                    length = len(item)
                    print(item)
                    if length > 0:
                        last = all_dicts[item[-1]]
                        final_str = ("[" * (length - 1) + last).ljust(15)
                        temp_res.append(final_str)
                    else:
                        temp_res.append(" " * 15)
                    i += 1
                content.append("    " + "".join(temp_res[0:4]).rstrip())
                content.append("    " + "".join(temp_res[4:8]).rstrip())
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
            content.append("]" * (len(cards) - current_opened_to) + "\n")
            content.append(
                "[" * (len(current_opened) - 1) + current_card_picture + "\n"
            )
            temp_res = []
            i = 0
            while i < len(all_stucks):
                item = all_stucks[i]
                length = len(item)
                if length > 0:
                    last = all_dicts[item[-1]]
                    final_str = ("[" * (length - 1) + last).ljust(15)
                    temp_res.append(final_str)
                else:
                    temp_res.append(" " * 15)
                i += 1
            content.append("    " + "".join(temp_res[0:4]).rstrip() + "\n")
            content.append("    " + "".join(temp_res[4:8]).rstrip() + "\n")
            if current_opened_to < len(cards):
                content.append("\n")
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
            elif current_opened_to < len(cards):
                current_opened, current_opened_to, changed = open_cards(
                    cards, current_opened, current_opened_to
                )
        total_palced += round_placed
        if round_placed == 0:
            break
        round += 1
    if total_palced < 52:
        print(f"\n{52-total_palced} cards could not be placed, you lost!\n")
    else:
        print(f"\nAll cards have been placed, you won!\n")
    lens = len(content)
    print(f"There are {lens} lines of output; what do you want me to do?\n")
    query_str = ""
    while True:
        try:
            query_str = input(
                f"Enter: q to quit\n       a last line number (between 1 and {lens})\n       a first line number (between -1 and -{lens})\n       a range of line numbers (of the form m--n with 1 <= m <= n <= {lens})\n       "
            )
            result = process_query(query_str, len(content))
            if not result:
                raise ValueError
            if result[0] == "q" and len(result) == 1:
                break
            print()
            if len(result) == 1:
                if result[0] > 0:
                    res_content = "".join(content[0 : result[0]])
                    print(res_content)
                else:
                    res_content = "".join(content[result[0] :])
                    print(res_content)
            if len(result) == 2:
                res_content = "".join(content[result[0] - 1 : result[1]])
                print(res_content)
        except ValueError:
            print()


run_self()
