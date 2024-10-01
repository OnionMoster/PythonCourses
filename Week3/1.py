import unicodedata


def input_number():
    First_message = "Please input two integers a and b with 0 <= a <= b <= 1114111,\n       both integers being separated by ~, with possibly\n       spaces and tabs before and after the numbers:\n       "
    Error_message = "\nIncorrect input, try again!"
    second_message = "\nEnter a string: "
    all_list = []
    match_list = []

    # 获取输入
    number = input(First_message)
    # print(number)
    # 整理输入
    cleaned_num = number.replace(" ", "").replace("\t", "").replace("+", "")
    # print(cleaned_num)
    # 判断输入
    if cleaned_num.count("~") != 1:
        print(Error_message)
        return input_number()
    else:
        cleaned_num = cleaned_num.split("~")
        a, b = int(cleaned_num[0]), int(cleaned_num[1])
        # print(a, b)
        # 判断ab
        if 0 <= a <= b <= 1114111:
            x = 0
            for i in range(a, b + 1):
                try:
                    unicodedata.name(chr(i))
                    x += 1
                    name = unicodedata.name(chr(i))
                    all_list.append((name, chr(i)))
                except ValueError:
                    pass
            n = (x / (b - a + 1)) * 100
            n1 = f"{(x / (b - a + 1)) * 100:.2f}"
            # print(n1)
            if n == 100:
                if a == b:
                    print(f"\n{a} is the code point of a named character.")
                else:
                    print(
                        f"\nAll numbers between {a} and {b}\n  are code points of named characters."
                    )
            elif 0 < n < 100:
                print(
                    f"\nAmongst the numbers between {a} and {b},\n  {n1}% are code points of named characters."
                )
            else:
                if a == b:
                    print(f"\n{a} is not the code point of a named character.")
                else:
                    print(
                        f"\nNo number between {a} and {b}\n  is the code point of a named character."
                    )
                return ()

            # 匹配第二次输入
            String = input(second_message)
            # print(String)

            if not all_list:
                print(
                    f"\nNone of the characters you want me to consider\n  has a name that starts with {String}."
                )
                return ()
            else:
                print(
                    f"\nHere are those of the characters under consideration\n  whose name starts with {String}:"
                )
                max_length = max(len(name) for name, _ in all_list)
                all_list.sort(key=lambda x: x[0])
                for name, unicode in all_list:
                    print(f"{name.ljust(max_length)}: {unicode}")
        else:
            print(Error_message)
            return input_number()


input_number()
