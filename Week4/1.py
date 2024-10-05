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
    # print(f"{n}:{num}")

    # 所有三个数乘小于和等于n的
    for a in range(len(num)):
        for b in range(a, len(num)):
            for c in range(b, len(num)):
                final_num = num[a] * num[b] * num[c]
                if final_num <= n:
                    num_list.append(final_num)
                    num_dict.update({final_num: (num[a], num[b], num[c])})

    fianl_list = sorted(num_list)
    fianl_dict = dict(sorted(num_dict.items()))
    # print(fianl_list)
    a, b, c = fianl_dict[fianl_list[-1]]

    # print(f"There are {len(fianl_list)} trinumbers at most equal to {n}.")
    # print(fianl_dict)
    # print(f"The largest one is {fianl_list[-1]}, equal to {a} x {b} x {c}.")


tri_numbers(123)
