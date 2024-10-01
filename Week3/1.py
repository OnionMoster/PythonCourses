import unicodedata


def input_number():
    First_message = "Please input two integers a and b with 0 <= a <= b <= 1114111,\n       both integers being separated by ~, with possibly \n       spaces and tabs before and after the numbers:"
    Error_message = "Incorrect input, try again!"
    second_message = "Enter a string:"
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
            n = 1  # （b-a+1）/unicode
            if n == 100:
                # ab同一个数
                if a == b:
                    print("{a} is the code point of a named character.")
                # ab不同一个数
                else:
                    print(
                        "All numbers between {a} and {b} \n  are code points of named characters."
                    )
            elif 0 < n < 100:
                print(
                    "Amongst the numbers between {a} and {b},\n  {n}% are code points of named characters."
                )
            else:
                print("{a} is not the code point of a named character.")
                return ()
        else:
            print(Error_message)
            return input_number()


input_number()
