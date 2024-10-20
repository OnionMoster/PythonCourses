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
        f"Enter: q to quit\n\t a last line number (between 1 and {lines})\n\t  a first line number (between -1 and {-lines})\n\t a range of lines numbers (of the form m--n with 1 <= m <= n <= {lines}\n)"
    )
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
    if number == 1:
        return "first"
    elif number == 2:
        return "second"
    elif number == 3:
        return "third"
    elif number % 10 == 1:
        return str(number) + "st"
    elif number % 10 == 2:
        return str(number) + "nd"
    elif number % 10 == 3:
        return str(number) + "rd"
    else:
        return str(number) + "th"


# play
def play_game():
    lost_cards_num = 0
    lines = 0
    done = True
    cards_num = 52
    seed = 0
    try:
        seed_num = int(
            input(f"Please enter an integer to feed the seed() function: \n")
        )
    except ValueError:
        return
    print("\nDeck shuffled, ready to start!")
    print("[" * cards_num)
    cards = sorted(set(range(52)))
    seed(seed_num)
    shuffle(cards)
