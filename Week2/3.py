def apply_pattern_to_list(L, pattern="+-", from_start=False):
    pattern_list = list(pattern)
    p = len(pattern_list)
    pop_line = {}
    x = 0  # 错误次数
    n = 0
    I = L[::-1]
    PI = pattern_list[::-1]

    while n < len(I) - 1:
        b = PI[n % p]
        if (b == "+" and I[n] < I[n + 1]) or (b == "-" and I[n] > I[n + 1]):
            n += 1
        else:
            x += 1
            pop_line[-n - x - 1] = I[n + 1]
            I.pop(n + 1)

    L1 = I[::-1]
    return pop_line, L1


L = [0, -4, 4, 4, 2, -2, 1, 3, -3, -4, -4, -2, -3, 0, 1, 2, -4, 3, -1, 1]
x = apply_pattern_to_list(L, "+-")
print("3", x)
