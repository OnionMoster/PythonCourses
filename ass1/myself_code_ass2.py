from itertools import chain
from random import seed, shuffle
from collections import defaultdict

poker = {
    0: "🃱",
    1: "🃲",
    2: "🃳",
    3: "🃴",
    4: "🃵",
    5: "🃶",
    6: "🃷",
    7: "🃸",
    8: "🃹",
    9: "🃺",
    10: "🃻",
    11: "🃽",
    12: "🃾",
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
    39: "🃡",
    40: "🃢",
    41: "🃣",
    42: "🃤",
    43: "🃥",
    44: "🃦",
    45: "🃧",
    46: "🃨",
    47: "🃩",
    48: "🃪",
    49: "🃫",
    50: "🃭",
    51: "🃮",
    52: " ",
}
record = []
stacks = [[], [], [], [], [], [], [], []]


def get_round_word(round_played):
    special_cases = {1: "first", 2: "second", 3: "third"}
    if round_played in special_cases:
        return special_cases[round_played]
    suffixes = {1: "st", 2: "nd", 3: "rd"}
    if 10 <= round_played % 100 <= 20:
        suffix = "th"
    else:
        suffix = suffixes.get(round_played % 10, "th")
    return str(round_played) + suffix


def show_deck(cards):
    record.append("".join(["]" for _ in cards]))


def get_stack_string(stack):
    L = ["[" for _ in stack]  # ]
    if len(L) != 0:
        L.pop()
        L.append(poker[stack[-1]])
    return "".join(L)


def show_taken_cards(cards):
    record.append(get_stack_string(cards))


def show_stacks():
    line1 = "    "
    line2 = "    "
    stack1 = []
    stack2 = []
    for i in range(8):
        if i < 4:
            stack1.append(f"{get_stack_string(stacks[i]):<13}")
        else:
            stack2.append(f"{get_stack_string(stacks[i]):<13}")

    line1 += "  ".join(stack1)
    line2 += "  ".join(stack2)
    record.append(line1.rstrip(" "))
    record.append(line2.rstrip(" "))


def get_3_cards(cards):
    L = []
    if len(cards) < 3:
        for _ in range(len(cards)):
            L.append(cards.pop())
    else:
        for _ in range(3):
            L.append(cards.pop())
    return L


def put_onto_stacks(cards):
    card = cards[-1]
    if card % 13 == 0:
        record.append("Placing one of the base cards!")
        stack_index = card // 13
        stacks[stack_index].append(cards.pop())
        return 1, cards
    elif card % 13 == 12:
        record.append("Placing one of the base cards!")
        stack_index = 4 + (card // 13)
        stacks[stack_index].append(cards.pop())
        return 1, cards
    else:
        for i in range(8):
            if len(stacks[i]) != 0:
                if i < 4 and card == stacks[i][-1] + 1:
                    record.append("Making progress on an increasing sequence!")
                    stacks[i].append(cards.pop())
                    return 1, cards
                elif i >= 4 and card == stacks[i][-1] - 1:
                    record.append("Making progress on a decreasing sequence!")
                    stacks[i].append(cards.pop())
                    return 1, cards
    return 0, cards


def handle_taken_cards(cards, taken_cards, round_state):
    while True:
        state, taken_cards = put_onto_stacks(taken_cards)
        if state != 0:
            round_state = state
            show_deck(cards)
            show_taken_cards(taken_cards)
            show_stacks()
            record.append("")
        else:
            break
        if len(taken_cards) == 0:
            break
    return taken_cards, round_state


def play_round(cards):
    round_played = 1
    round_state = 1
    taken_cards = []
    record.append(
        f"Starting to draw 3 cards (if possible) again and again for the {get_round_word(round_played)} time..."
    )
    record.append("")
    while True:
        new_cards = get_3_cards(cards)
        if len(new_cards) == 0:
            if len(taken_cards) == 0:
                record.pop()
                return 0
            elif round_state == 0:
                record.pop()
                return len(taken_cards)
            else:
                cards = taken_cards[::-1]
                taken_cards = []
                round_state = 0
                round_played += 1
                record.append(
                    f"Starting to draw 3 cards (if possible) again and again for the {get_round_word(round_played)} time..."
                )
                record.append("")
                continue
        taken_cards.extend(new_cards)
        show_deck(cards)
        show_taken_cards(taken_cards)
        show_stacks()
        record.append("")
        taken_cards, round_state = handle_taken_cards(cards, taken_cards, round_state)


def start(seed_value):
    record.clear()
    for i in stacks:
        i.clear()
    cards = list(range(52))
    seed(int(seed_value))
    shuffle(cards)
    record.append("Deck shuffled, ready to start!")
    show_deck(cards)
    record.append("")
    return play_round(cards)


def main():
    seed_value = input("Please enter an integer to feed the seed() function: ")
    print("")
    n = start(seed_value)
    if n == 0:
        print("All cards have been placed, you won!")
    else:
        print(f"{n} cards could not be placed, you lost!")
    print("")
    print(f"There are {len(record)} lines of output; what do you want me to do?")
    while True:
        print("")
        print("Enter: q to quit")
        print(f"       a last line number (between 1 and {len(record)})")
        print(f"       a first line number (between -1 and -{len(record)})")
        print(
            f"       a range of line numbers (of the form m--n with 1 <= m <= n <= {len(record)})"
        )
        s = input("       ")
        if s == "q":
            exit()
        else:
            try:
                if "--" in s:
                    s = s.replace(" ", "")
                    s = s.replace("\t", "")
                    lines = s.split("--")
                    lines = [int(x) for x in lines]
                    if 1 <= lines[0] <= lines[1] <= len(record):
                        print("")
                        print("\n".join(record[lines[0] - 1 : lines[1]]))
                else:
                    lines = [int(s)]
                    if lines[0] > 0:
                        print("")
                        print("\n".join(record[: lines[0]]))
                    elif lines[0] < 0:
                        print("")
                        print("\n".join(record[lines[0] :]))
            except:
                pass


if __name__ == "__main__":
    main()
