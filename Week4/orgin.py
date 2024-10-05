from math import sqrt


def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve


def tri_numbers(n):
    bool_num = sieve_of_primes_up_to(n)
    num = [i for i in range(2, n + 1) if bool_num[i]]
    num_list = []
    num_dict = {}
    rela_list = []
    key_dict = {}
    # print(f"{n}:{num}")

    # 所有三个数乘小于和等于n的 遍历*3
    for a in range(len(num)):
        if num[a] > n ** (1 / 3):
            break
        for b in range(a, len(num)):
            if num[a] * num[b] > (n ** (1 / 3)) ** 2:
                break
            for c in range(b, len(num)):
                final_num = num[a] * num[b] * num[c]
                if final_num > n:
                    break
                num_list.append(final_num)
                num_dict.update({final_num: (num[a], num[b], num[c])})

    fianl_list = sorted(num_list)
    fianl_dict = dict(sorted(num_dict.items()))
    Ma, Mb, Mc = fianl_dict[fianl_list[-1]]

    # 遍历
    for key, value in fianl_dict.items():
        p = value[1] - value[0]
        q = value[2] - value[1]
        if p <= q:
            rela_list.append(p)
            key_dict.update({key: p})
        else:
            rela_list.append(q)
            key_dict.update({key: q})
    max_gap = max(rela_list)
    # print(key_dict)

    # 遍历
    all_max_gap_list = [key for key, value in key_dict.items() if value == max_gap]

    if len(fianl_list) <= 1:
        print(f"There is {len(fianl_list)} trinumber at most equal to {n}.")
    else:
        print(f"There are {len(fianl_list)} trinumbers at most equal to {n}.")
    print(f"The largest one is {fianl_list[-1]}, equal to {Ma} x {Mb} x {Mc}.")
    print(f"\nThe maximum gap in decompositions is {(max_gap)}.")
    print(f"It is achieved with:")
    for i in all_max_gap_list:
        a, b, c = fianl_dict[i]
        print(f"  {i} = {a} x {b} x {c}")


tri_numbers(50000000)
