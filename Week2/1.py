def apply_pattern_to_list(L, pattern="+-", from_start=True):
    pattern_list = list(pattern)
    p = len(pattern_list)
    pop_line = {}
    error_count = 0

    if from_start:
        # from_start = True left to right
        n = 0
        while n < len(L) - 1:
            a = pattern_list[n % p]
            ###    if a == "+":
            ###        if L[n] < L[n + 1]:
            ###            n += 1
            ###        else:
            ###            error_count += 1
            ###            pop_line[n + error_count] = L[n + 1]
            ###            L.pop(n + 1)
            ###    elif a == "-":
            ###        if L[n] > L[n + 1]:
            ###            n += 1
            ###        else:
            ###            error_count += 1
            ###            pop_line[n + error_count] = L[n + 1]
            ###            L.pop(n + 1)
            if (a == "+" and L[n] < L[n + 1]) or (a == "-" and L[n] > L[n + 1]):
                n += 1
            else:
                error_count += 1
                pop_line[n + error_count] = L[n + 1]
                L.pop(n + 1)

    else:
        # from_start = false right to left
        n = -1
        while n > -len(L):
            b = pattern_list[n % p]
            ###if b == "+":
            ###if L[n] < L[n - 1]:
            ###    n -= 1
            ###else:
            ###    error_count += 1
            ###    pop_line[n - error_count] = L[n - 1]
            ###    L.pop(n - 1)
            ###elif b == "-":
            ###if L[n] > L[n - 1]:
            ###    n -= 1
            ###else:
            ###    error_count += 1
            ###    pop_line[n - error_count] = L[n - 1]
            ###    L.pop(n - 1)
            if (b == "+" and L[n] < L[n - 1]) or (b == "-" and L[n] > L[n - 1]):
                n -= 1
            else:
                error_count += 1
                pop_line[n - error_count] = L[n - 1]
                L.pop(n - 1)

    return pop_line


L = [0, -4, 4, 4, 2, -2, 1, 3, -3, -4, -4, -2, -3, 0, 1, 2, -4, 3, -1, 1]
x = apply_pattern_to_list(L, "+-", False)
print("1", x)
print(L)
