from random import seed, shuffle

# seed 标记
cards = list(range(52))
seed(7)
shuffle(cards)
print(cards)

# 乱序
cards = list(range(52))
shuffle(cards)
# print(cards)
shuffle(cards)
# print(cards)

# 排除
cards = sorted(set(range(52)) - {16, 36})
# print("1", cards)
shuffle(cards)
# print("2", cards)
