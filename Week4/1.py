from math import sqrt


def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve


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
    # print(f"{n}:{num_list}")

    n, u, m = 0
    a, b, c = num[n], num[u], num[m]
