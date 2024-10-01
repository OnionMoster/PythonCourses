# 整理输入
    cleaned_num = number.replace(" ", "").replace("\t", "")

    if cleaned_num.count("~") != 1:
        print(Error_message)
        return input_number()
    else:
        cleaned_num = cleaned_num.strip("~")
        a, b = int(cleaned_num[0]), int(cleaned_num[1])
        # 判断ab是否符合条件
        if 0 <= a <= 1114111 and 0 <= b <= 1114111 and a <= b:
            # 百分比 （b-a+1）/unicode
            n = 1  # 占位符
            # 百分百
            if n == 100:
                if a == b:
                    print("{a} is the code point of a named character.")
                else:
                    print(
                        "All numbers between {a} and {b} \n  are code points of named characters."
                    )
            # 小于100大于0
            elif 0 < n < 100:
                print(
                    "Amongst the numbers between {a} and {b},\n  {n}% are code points of named characters."
                )
            # 等于0
            else:
                print("{a} is not the code point of a named character.")
                return ()

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
