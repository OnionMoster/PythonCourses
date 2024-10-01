            # 匹配 ？
            String = input(second_message)
            for codepoint in range(a, b + 1):
                try:
                    char_name = unicodedata.name(chr(codepoint))
                    if char_name.startswith(String):
                        match_list.append((chr(codepoint)), char_name)
                except ValueError:
                    continue

            if not match_list:
                print(
                    "None of the characters you want me to consider\n  has a name that starts with {String}."
                )
                return ()
            else:
                for point, name in match_list:
                    print(
                        "Here are those of the characters under consideration\n  whose name starts with {String}:"
                    )
                    print("{name}:{point}")