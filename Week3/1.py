import unicodedata


def input_unicode():
    First_message = "Please input two integers a and b with 0 <= a <= b <= 1114111,\n\t both integers being separated by ~, with possibly \n\t spaces and tabs before and after the numbers:"
    Error_message = "Incorrect input, try again!"
    second_message = "Enter a string:"
    match_list = []

    number = input(First_message)
    cleaned_num = number.replace(" ", "").replace("\t", "")
    if cleaned_num.count("~") != 1:
        print(Error_message)
        return input_unicode()
    else:
        cleaned_num = cleaned_num.strip("~")
        a, b = int(cleaned_num[0]), int(cleaned_num[1])
        if 0 <= a <= 1114111 and 0 <= b <= 1114111 and a <= b:
            # 百分比 （b-a+1）/unicode
            n = 1
            if n == 100:
                if a == b:
                    print("{a} is the code point of a named character.")
                else:
                    print(
                        "All numbers between {a} and {b} \n  are code points of named characters."
                    )
            elif 0 < n < 100:
                print(
                    "Amongst the numbers between {a} and {b},\n  8{n}% are code points of named characters."
                )
            else:
                # print(int(a) + " is not the code point of a named character.")
                exit
            # match unicode name
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
            else:
                for point, name in match_list:
                    print(
                        "Here are those of the characters under consideration\n  whose name starts with {String}:"
                    )
                    print("{name}:{point}")

        else:
            print(Error_message)
            return input_unicode()
