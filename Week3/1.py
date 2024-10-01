import unicodedata


def input_number():
    First_message = "Please input two integers a and b with 0 <= a <= b <= 1114111,\n       both integers being separated by ~, with possibly \n       spaces and tabs before and after the numbers:"
    Error_message = "Incorrect input, try again!"
    second_message = "Enter a string: "
    match_list = []

    # 获取输入
    number = input(First_message)
    # print(number)
    # 整理输入
    cleaned_num = number.replace(" ", "").replace("\t", "")
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
        if 0 <= a <= 1114111 and 0 <= b <= 1114111 and a <= b:
            num_list = [i for i in range(a, b + 1)]
            x = 0
            for i in num_list:
                try:
                    unicodedata.name(chr(i))
                    x += 1
                except ValueError:
                    pass
            n = x / (b - a + 1)
            n1 = f"{(x / (b - a + 1)) * 100:.2f}"
            # print(n1)
            if a == b and n == 100:
                print(f"{a} is the code point of a named character.")
            # ab不同一个数
            elif n == 100:
                print(
                    f"All numbers between {a} and {b} \n  are code points of named characters."
                )
            elif 0 < n < 100:
                print(
                    f"Amongst the numbers between {a} and {b},\n  {n1}% are code points of named characters."
                )
            else:
                print(f"{a} is not the code point of a named character.")
                return ()

            # 匹配第二次输入
            String = input(second_message)
            # print(String)

        else:
            print(Error_message)
            for i in range(a, b + 1):
                try:
                    name = unicodedata.name(chr(i))
                    if name.startswith(String):
                        match_list.append((chr(i)), name)
                except ValueError:
                    continue
        if not match_list:
            print(
                f"None of the characters you want me to consider\n  has a name that starts with {String}"
            )
            return ()
        else:
            for unicode, name in match_list:
                print(
                    f"Here are those of the characters under consideration\n  whose name starts with {String}:"
                )
                print(f"{name}:{unicode}")


input_number()
