# L颠倒
def apply_pattern_to_list(L, pattern="+-", from_start=True):
    pattern_list = list(pattern)
    p = len(pattern_list)
    pop_line = {}
    error_count = 0  # 错误次数
    n = 0
    Right_L = L[::-1]
    PI = pattern_list[::-1]

    if from_start:
        n = 0
        while n < len(Right_L) - 1:
            a = PI[n % p]
            if (a == "+" and Right_L[n] < Right_L[n + 1]) or (
                a == "-" and Right_L[n] > Right_L[n + 1]
            ):
                n += 1
            else:
                error_count += 1
                pop_line[-n - error_count - 1] = Right_L[n + 1]
                Right_L.pop(n + 1)
    else:
        while n < len(Right_L) - 1:
            b = PI[n % p]
            if (b == "+" and Right_L[n] < Right_L[n + 1]) or (
                b == "-" and Right_L[n] > Right_L[n + 1]
            ):
                n += 1
            else:
                error_count += 1
                pop_line[-n - error_count - 1] = Right_L[n + 1]
                Right_L.pop(n + 1)

    L1 = Right_L[::-1]
    L.clear()
    L.extend(L1)

    return pop_line


L = [0, -4, 4, 4, 2, -2, 1, 3, -3, -4, -4, -2, -3, 0, 1, 2, -4, 3, -1, 1]
x = apply_pattern_to_list(L, "+-", False)
print("3", x)
print(L)
