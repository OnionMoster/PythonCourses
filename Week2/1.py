def apply_pattern_to_list(L, pattern='+-', from_start=True):
    pattern_list = list(pattern)
    p = len(pattern_list)
    pop_line = {}
    if from_start: 
        #from_start = True left to right
        n = 0 #left to right
        z = 0
        while n < len(L) - 1:
            a = pattern_list[n % p]
            if a == '+' :
                if L[n] < L[n+1]:
                    n += 1
                else:
                    z += 1
                    pop_line[n+z+1] = L[n+1]
                    L.pop(n+1)
            elif a == '-':
                if L[n] > L[n+1]:
                    n += 1
                else:
                    z +=1
                    pop_line[n+1+1] = L[n+1]
                    L.pop(n+1)

    return pop_line , L

L = [0, -4, 4, 4, 2, -2, 1, 3, -3, -4, -4, -2, -3, 0, 1, 2, -4, 3, -1, 1]
rusult =  apply_pattern_to_list(L, '-+')
print (rusult)