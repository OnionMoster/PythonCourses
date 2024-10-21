import csv
from collections import defaultdict


# 分离开是否生病
def process_health_data(data):
    all_no_disease = {}
    all_disease = {}

    def add_data(target_dict, key, values):
        target_dict[key] = values
        return values["weight"], values["height"], values["ap_hi"], values["ap_lo"]

    weight_list_no_disease, height_list_no_disease = [], []
    weight_list_disease, height_list_disease = [], []
    ap_hi_list_no_disease, ap_lo_list_no_disease = [], []
    ap_hi_list_disease, ap_lo_list_disease = [], []

    for key, values in data.items():
        is_cardio = values["cardio"]

        if is_cardio == 0:
            weight, height, ap_hi, ap_lo = add_data(all_no_disease, key, values)
            weight_list_no_disease.append(weight)
            height_list_no_disease.append(height)
            ap_hi_list_no_disease.append(ap_hi)
            ap_lo_list_no_disease.append(ap_lo)

        else:
            weight, height, ap_hi, ap_lo = add_data(all_disease, key, values)
            weight_list_disease.append(weight)
            height_list_disease.append(height)
            ap_hi_list_disease.append(ap_hi)
            ap_lo_list_disease.append(ap_lo)

    # 计算大小值
    def calculate_min_max(lst):
        return max(lst), min(lst) if lst else (None, None)

    # 计算无病和有病的最大最小值
    n_max_height, n_min_height = calculate_min_max(height_list_no_disease)
    n_max_weight, n_min_weight = calculate_min_max(weight_list_no_disease)
    n_max_ap_hi, n_min_ap_hi = calculate_min_max(ap_hi_list_no_disease)
    n_max_ap_lo, n_min_ap_lo = calculate_min_max(ap_lo_list_no_disease)

    i_max_height, i_min_height = calculate_min_max(height_list_disease)
    i_max_weight, i_min_weight = calculate_min_max(weight_list_disease)
    i_max_ap_hi, i_min_ap_hi = calculate_min_max(ap_hi_list_disease)
    i_max_ap_lo, i_min_ap_lo = calculate_min_max(ap_lo_list_disease)

    # 输出结果
    # print("No Disease Data:", all_no_disease)
    # print("Disease Data:", all_disease)

    # print("\nNo Disease Stats:")
    # print(f"Max Height: {n_max_height}, Min Height: {n_min_height}")
    # print(f"Max Weight: {n_max_weight}, Min Weight: {n_min_weight}")
    # print(f"Max AP Hi: {n_max_ap_hi}, Min AP Hi: {n_min_ap_hi}")
    # print(f"Max AP Lo: {n_max_ap_lo}, Min AP Lo: {n_min_ap_lo}")

    # print("\nDisease Stats:")
    # print(f"Max Height: {i_max_height}, Min Height: {i_min_height}")
    # print(f"Max Weight: {i_max_weight}, Min Weight: {i_min_weight}")
    # print(f"Max AP Hi: {i_max_ap_hi}, Min AP Hi: {i_min_ap_hi}")
    # print(f"Max AP Lo: {i_max_ap_lo}, Min AP Lo: {i_min_ap_lo}")


# 主函数
def analyse(gender, age):
    if gender not in ("M", "F"):
        return
    gender = 1 if gender == "F" else 2
    if not isinstance(age, int):
        return
    # 奇怪的路径bug
    # 读取csv文件和表头
    with open(r"D:\Projects\9021\Week5\cardio_train.csv") as file:
        title = csv.reader(file, delimiter=";")
        titles = next(title)
        id_idx = titles.index("id")
        year_idx = titles.index("age")
        gender_idx = titles.index("gender")
        height_idx = titles.index("height")
        weight_idx = titles.index("weight")
        ap_hi_idx = titles.index("ap_hi")
        ap_lo_idx = titles.index("ap_lo")
        cholesterol_idx = titles.index("cholesterol")
        gluc_idx = titles.index("gluc")
        smoke_idx = titles.index("smoke")
        alco_idx = titles.index("alco")
        active_idx = titles.index("active")
        cardio_idx = titles.index("cardio")
        # 判断是否符合范围和条件
        good_data = {}
        for row in title:
            id = row[id_idx]
            year = int((int(row[year_idx]) - 1) // 365)
            height = int(row[height_idx])
            weight = float(row[weight_idx])
            ap_hi = int(row[ap_hi_idx])
            ap_lo = int(row[ap_lo_idx])
            if (
                int(year) == age
                and int(row[gender_idx]) == gender
                and 150 <= height <= 200
                and 50 <= weight <= 150
                and 80 <= ap_hi <= 200
                and 70 <= ap_lo <= 140
            ):
                good_data[id] = {
                    "year": int(year),
                    "gender": gender,
                    "height": int(height),
                    "weight": float(weight),
                    "ap_hi": int(ap_hi),
                    "ap_lo": int(ap_lo),
                    "cholesterol": int(row[cholesterol_idx]),
                    "gluc": int(row[gluc_idx]),
                    "smoke": int(row[smoke_idx]),
                    "alco": int(row[alco_idx]),
                    "active": int(row[active_idx]),
                    "cardio": int(row[cardio_idx]),
                }

        # print(good_data)
        print(len(good_data))

        process_health_data(good_data)


# 拆分五个区间
def five_pick():
    pass


analyse("F", 43)
