from random import seed, shuffle

# 乱序
cards = list(range(52))
print(cards)
shuffle(cards)
print(cards)
shuffle(cards)
print(cards)

# 排除
cards = sorted(set(range(52)) - {16, 36})
# print(cards)
shuffle(cards)
# print(cards)

# seed 标记
cards = list(range(52))
seed(678)
shuffle(cards)
# print(cards)
# print(cards)
