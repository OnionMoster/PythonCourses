# 零时数组
def apply_pattern_to_list(L, pattern="+-", from_start=True):
    pattern_list = list(pattern)
    p = len(pattern_list)
    pop_line = {}
    error_count = 0
    n = 0
    i = 1
<<<<<<< HEAD
    New_List = []
=======
    I = []
>>>>>>> fa1b678f90e392e10ca9d02d8986416e99e15761
    if from_start:
        while n < len(L):
            a = pattern_list[n % p]
            if i < len(L) - n:
                if (a == "+" and L[n] < L[n + i]) or (a == "-" and L[n] > L[n + i]):
<<<<<<< HEAD
                    New_List.append(L[n])
=======
                    I.append(L[n])
>>>>>>> fa1b678f90e392e10ca9d02d8986416e99e15761
                    n += 1
                else:
                    error_count += 1
                    pop_line[n + error_count] = L[n + 1]
                    L.pop(n + 1)
            else:
<<<<<<< HEAD
                New_List.append(L[n])
=======
                I.append(L[n])
>>>>>>> fa1b678f90e392e10ca9d02d8986416e99e15761
                break
    else:
        n = -1
        while n > -len(L):
            b = pattern_list[n % p]
            if (b == "+" and L[n] < L[n - 1]) or (b == "-" and L[n] > L[n - 1]):
                n -= 1
            else:
                error_count += 1
                pop_line[n - error_count] = L[n - 1]
                L.pop(n - 1)

    L.clear()
<<<<<<< HEAD
    L.extend(New_List)
=======
    L.extend(I)
>>>>>>> fa1b678f90e392e10ca9d02d8986416e99e15761
    return pop_line


# 测试代码
L = [0, -4, 4, 4, 2, -2, 1, 3, -3, -4, -4, -2, -3, 0, 1, 2, -4, 3, -1, 1]
x = apply_pattern_to_list(L, "+-")
print("2", x)
print(L)
