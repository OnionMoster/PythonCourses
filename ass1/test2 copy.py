from itertools import chain
from collections import defaultdict
from random import seed, shuffle

card_symbols = {
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
    52: " ",
}

log_lines = []
all_stacks = [[], [], [], [], [], [], [], []]


def get_ordinal_suffix(number):
    """
    返回给定数字的序数后缀（例如，1 -> '1st'，2 -> '2nd'）。
    """
    special_cases = {1: "first", 2: "second", 3: "third"}
    if number in special_cases:
        return special_cases[number]
    suffixes = {1: "st", 2: "nd", 3: "rd"}
    if 10 <= number % 100 <= 20:
        suffix = "th"
    else:
        suffix = suffixes.get(number % 10, "th")
    return str(number) + suffix


def format_stack(stack):
    """
    返回格式化的牌堆字符串表示。
    """
    stack_representation = ["[" for _ in stack]
    if len(stack_representation) != 0:
        stack_representation.pop()
        stack_representation.append(card_symbols[stack[-1]])
    return "".join(stack_representation)


def close_cards(cards):
    """
    将剩余牌的闭合括号表示追加到日志中。
    """
    log_lines.append("".join(["]" for _ in cards]))


def parse_query(query, max_value):
    """
    解析用户输入的查询，以确定返回日志的哪些行。
    """
    query = str(query).strip()
    if not query:
        return False
    if query == "q":
        return ["q"]
    if query == "+" or (query.startswith("-") and not query[1:].strip()):
        return False
    try:
        result = int(query)
        if 0 < result <= max_value or -max_value <= result < 0:
            return [result]
    except ValueError:
        pass
    if "--" in query:
        try:
            start, end = map(int, query.split("--"))
            if 0 < start <= end <= max_value:
                return [start, end]
        except ValueError:
            return False
    return False


def reveal_cards(cards, current_opened, opened_index):
    """
    从牌堆中揭示最多 3 张牌，并返回更新后的打开牌列表和索引。
    """
    upper_bound = min(opened_index + 3, len(cards))
    current_opened += cards[opened_index:upper_bound]
    opened_index = upper_bound
    return current_opened, opened_index, True


def append_closed_brackets(cards, opened_index):
    """
    将剩余牌的闭合括号表示追加到日志中。
    """
    log_lines.append("]" * (len(cards) - opened_index) + "\n")


def run_game():
    """
    运行纸牌放置游戏，管理牌堆、打开的牌和游戏状态。
    """
    total_placed = 0
    seed_value = 0
    try:
        seed_value = int(input("Please enter an integer to feed the seed() function: "))
    except ValueError:
        return
    card_mapping = card_symbols
    card_list = list(card_symbols.keys())

    all_cards, cards = card_mapping, card_list
    expected_stack_values = [0, 13, 26, 39, 12, 25, 38, 51]
    log_lines.append(f"Deck shuffled, ready to start!\n")
    append_closed_brackets(cards, 0)
    round_number = 0
    seed(seed_value)
    shuffle(cards)
    cards.reverse()
    while cards:
        round_placed = 0
        log_lines.append("\n")
        log_lines.append(
            f"Starting to draw 3 cards (if possible) again and again for the {get_ordinal_suffix(round_number+1)} time...\n"
        )
        log_lines.append("\n")
        opened_index = 0
        opened_cards = []
        state_changed = True
        if len(opened_cards) == 0 and opened_index < len(cards):
            opened_cards, opened_index, state_changed = reveal_cards(
                cards, opened_cards, opened_index
            )
        while state_changed:
            state_changed = False
            if not opened_cards:
                append_closed_brackets(cards, opened_index)
                log_lines.append("\n")
                line1 = (
                    "    "
                    + "".join(
                        [f"{format_stack(all_stacks[i]):<13}" for i in range(4)]
                    ).rstrip()
                    + "\n"
                )
                line2 = (
                    "    "
                    + "".join(
                        [f"{format_stack(all_stacks[i]):<13}" for i in range(4, 8)]
                    ).rstrip()
                    + "\n"
                )
                log_lines.append(line1)
                log_lines.append(line2)
                if opened_index < len(cards):
                    opened_cards, opened_index, state_changed = reveal_cards(
                        cards, opened_cards, opened_index
                    )
                    if round_placed > 0:
                        log_lines.append("\n")
                    continue
                else:
                    break
            current_card_symbol = all_cards[opened_cards[-1]]
            current_card = opened_cards[-1]
            append_closed_brackets(cards, opened_index)
            log_lines.append("[" * (len(opened_cards) - 1) + current_card_symbol + "\n")
            line1 = (
                "    "
                + "".join(
                    [f"{format_stack(all_stacks[i]):<13}" for i in range(4)]
                ).rstrip()
                + "\n"
            )
            line2 = (
                "    "
                + "".join(
                    [f"{format_stack(all_stacks[i]):<13}" for i in range(4, 8)]
                ).rstrip()
                + "\n"
            )
            log_lines.append(line1)
            log_lines.append(line2)

            if opened_index < len(cards):
                log_lines.append("\n")

            if current_card in expected_stack_values:
                if opened_index >= len(cards):
                    log_lines.append("\n")
                state_changed = True
                round_placed += 1
                current_card = opened_cards.pop()
                cards.remove(current_card)
                opened_index = max(opened_index - 1, 0)
                stack_index = expected_stack_values.index(current_card)

                if current_card in [12, 25, 38, 51]:
                    stack_index = 4 + [12, 25, 38, 51].index(current_card)
                all_stacks[stack_index].append(current_card)
                if stack_index < 4:
                    if len(all_stacks[stack_index]) == 1:
                        log_lines.append("Placing one of the base cards!\n")
                    else:
                        log_lines.append("Making progress on an increasing sequence!\n")
                    expected_stack_values[stack_index] += 1
                else:
                    if len(all_stacks[stack_index]) == 1:
                        log_lines.append("Placing one of the base cards!\n")
                    else:
                        log_lines.append("Making progress on an decreasing sequence!\n")
                    expected_stack_values[stack_index] -= 1
            elif opened_index < len(cards):
                opened_cards, opened_index, state_changed = reveal_cards(
                    cards, opened_cards, opened_index
                )
        total_placed += round_placed
        if round_placed == 0:
            break
        round_number += 1
    if total_placed < 52:
        print(f"\n{52-total_placed} cards could not be placed, you lost!\n")
    else:
        print(f"\nAll cards have been placed, you won!\n")

    num_lines = len(log_lines)
    print(f"There are {num_lines} lines of output; what do you want me to do?\n")
    query = ""
    while True:
        try:
            query = input(
                f"Enter: q to quit\n       a last line number (between 1 and {num_lines})\n       a first line number (between -1 and -{num_lines})\n       a range of line numbers (of the form m--n with 1 <= m <= n <= {num_lines})\n       "
            )
            result = parse_query(query, len(log_lines))
            if not result:
                raise ValueError
            if result[0] == "q" and len(result) == 1:
                break
            print()
            if len(result) == 1:
                result_lines = "".join(
                    log_lines[: result[0]] if result[0] > 0 else log_lines[result[0] :]
                )
                print(result_lines)
            elif len(result) == 2:
                result_lines = "".join(log_lines[result[0] - 1 : result[1]])
                print(result_lines)
        except ValueError:
            print()


run_game()
