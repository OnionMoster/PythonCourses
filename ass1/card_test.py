# unicode
def generate_unicode_cards_by_range():
    unicode_cards = []
    unicode_ranges = {
        "红桃": "1F0B",
        "方块": "1F0C",
        "梅花": "1F0D",
        "黑桃": "1F0A",
    }

    ranges = {
        "红桃": (0, 12),
        "方块": (13, 25),
        "梅花": (26, 38),
        "黑桃": (39, 51),
    }

    for suit_name, suit_code in unicode_ranges.items():
        start, end = ranges[suit_name]
        for i in range(start, end + 1):
            unicode_card = chr(int(suit_code + f"{(i - start + 1):X}", 16))
            unicode_cards.append(unicode_card)

    # print(unicode_cards[0])


generate_unicode_cards_by_range()
