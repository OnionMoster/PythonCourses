# 定义每个范围的描述及对应的Unicode符号
ranges = {
    range(0, 13): "🂱",  # 红桃 A 到 K
    range(13, 26): "🃁",  # 方块 A 到 K
    range(26, 39): "🃑",  # 梅花 A 到 K
    range(39, 52): "🂡",  # 黑桃 A 到 K
}

# 创建整数与描述的字典
int_unicode_dict = {}
for r, symbol in ranges.items():
    for i in r:
        int_unicode_dict[i] = f"{symbol}{i - min(r) + 1}"

# 打印字典
for k, v in int_unicode_dict.items():
    print(f"({k}, {v})")
