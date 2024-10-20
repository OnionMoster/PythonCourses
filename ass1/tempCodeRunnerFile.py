def play_more_game(n, i):
    JOKER_CARDS = {10, 11, 12, 23, 24, 25, 36, 37, 38, 49, 50, 51}
    false_results = defaultdict(int)

    game_times = 0
    while game_times < n:
        seed_value = i + game_times
        removed_cards = []
        rounds = 0

        while rounds < 4:
            card_index = 0
            replace_cards = []
            seed(seed_value + rounds)
            cards = sorted(set(range(52)) - set(removed_cards))
            shuffle(cards)
            cards.reverse()
            origin_cards = cards[:16]
            card_index += 16

            # 替换
            for i in range(len(origin_cards)):
                if origin_cards[i] in JOKER_CARDS:
                    replace_cards.append({"index": i, "card": ""})
                    removed_cards.append(origin_cards[i])
                    origin_cards[i] = ""

            while len(replace_cards) > 0:
                for i in range(len(replace_cards)):
                    replace_cards[i]["card"] = cards[card_index]
                    card_index += 1

                temp_replace_cards = []
                for i in range(len(replace_cards)):
                    if replace_cards[i]["card"] in JOKER_CARDS:
                        temp_replace_cards.append(replace_cards[i])
                        origin_cards[replace_cards[i]["index"]] = ""
                        removed_cards.append(replace_cards[i]["card"])
                    else:
                        origin_cards[replace_cards[i]["index"]] = replace_cards[i][
                            "card"
                        ]
                replace_cards = temp_replace_cards

            rounds += 1

            if len(removed_cards) == 12:
                break

        if len(removed_cards) == 12:
            false_results[12] += 1
        else:
            false_results[len(removed_cards)] += 1

        game_times += 1

    total_games = sum(false_results.values())
    print("Number of uncovered pictures | Frequency")
    print("----------------------------------------")
    for key in sorted(false_results.keys()):
        probability = (false_results[key] / total_games) * 100
        formatted_probability = f"{probability:.2f}%"
        if probability < 0.5:
            formatted_probability = "0.00%"
        print(f"{key:28} | {formatted_probability:>9}")
