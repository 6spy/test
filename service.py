import random

import mapper


def query_price():
    # 生成返回数据集
    data_list = []
    # 获取各菜品种类名称
    kinds_list = mapper.query_kinds_list()
    # 菜品种类最高价
    price_max = mapper.query_price_max()
    # 菜品种类最低价
    price_min = mapper.query_price_min()
    # 菜品种类平均价
    price_avg = mapper.query_price_avg()
    # 存入数据集并返回
    data_list.append(price_max)
    data_list.append(price_min)
    data_list.append(price_avg)
    return kinds_list, data_list


def query_types():
    # 生成返回数据集
    data_list = []
    # 获取各菜品种类名称
    tpyes_list = mapper.query_types_list()
    # 获取各三餐数量
    types_list_pie = mapper.query_types_list_pie()
    types_list_bar = mapper.query_types_list_bar()
    # 存入数据集并返回
    data_list.append(types_list_pie)
    data_list.append(types_list_bar)
    data_list.append(types_list_bar)
    return tpyes_list, data_list


def query_kinds():
    # 生成返回数据集
    data_list_x = []
    data_list_y = []
    # 获取各地区名称
    kinds_list = mapper.query_kinds_list()
    names_list = mapper.query_name_list()
    # 获取各菜品种类数量
    kinds_list_bar = mapper.query_kinds_list_bar()
    kinds_list_pie = mapper.query_kinds_list_pie()
    # 获取各菜品数量
    name_list_bar = mapper.query_name_list_bar()
    # 存入数据集并返回
    data_list_x.append(kinds_list)
    data_list_x.append(names_list)

    data_list_y.append(kinds_list_bar)
    data_list_y.append(kinds_list_pie)
    data_list_y.append(name_list_bar)
    return data_list_x, data_list_y


def query_types_list(): return mapper.query_types_list()


def query_kinds_list(): return mapper.query_kinds_list()


def query_search(type, kind, name):
    return mapper.query_search(type, kind, name)


def query_forecast():
    # 生成返回数据集
    data_list = []
    # 获取各地区名称
    kinds = mapper.query_kinds_list()
    # 获取各菜品种类数量
    kinds_list = mapper.query_kinds_list_bar()
    kinds_list1 = [int(item * random.random()) for item in kinds_list]
    kinds_list2 = [int(item * random.random()) for item in kinds_list]
    kinds_list3 = [int(item * random.random()) for item in kinds_list]
    kinds_list4 = [int(item * random.random()) for item in kinds_list]
    # 存入数据集并返回
    data_list.append(kinds_list)
    data_list.append(kinds_list1)
    data_list.append(kinds_list2)
    data_list.append(kinds_list3)
    data_list.append(kinds_list4)

    print(kinds)
    print(kinds_list)
    print(kinds_list1)
    print(kinds_list2)
    print(kinds_list3)
    print(kinds_list4)

    return kinds, data_list

