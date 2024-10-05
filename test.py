def tri_numbers(n):
    num_list = []
    for i in range(2, n + 1):
        num = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                num = False
                break
        if num:
            num_list.append(i)
    print(f"{n}:{num_list}")


tri_numbers(123)
