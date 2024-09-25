def apply_pattern_to_list(L, pattern="+-", from_start=True):
    pattern_list = list(pattern)
    p = len(pattern_list)
    pop_line = {}
    x = 0  # 错误次数
    n = 0  # 从左到右
    i = 1
    I = []

    while n < len(L):
        a = pattern_list[n % p]
        if i < len(L) - n:
            if (a == "+" and L[n] < L[n + i]) or (a == "-" and L[n] > L[n + i]):
                I.append(L[n])
                n += 1
            else:
                x += 1
                pop_line[n + x] = L[n + 1]
                L.pop(n + 1)
        else:
            I.append(L[n])
            break
    return pop_line, I


# 测试代码
L = [0, -4, 4, 4, 2, -2, 1, 3, -3, -4, -4, -2, -3, 0, 1, 2, -4, 3, -1, 1]
x = apply_pattern_to_list(L, "+-")
print("2", x)
