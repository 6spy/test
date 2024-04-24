import connect


def query_types_list():
    data_list = []
    sql = "select distinct type from catering;"
    results = connect.executeQuery(sql)
    if len(results) > 0:
        for row in results:
            data_list.append(row[0])
    return data_list


def query_kinds_list():
    data_list = []
    sql = "select distinct kind from catering;"
    results = connect.executeQuery(sql)
    if len(results) > 0:
        for row in results:
            data_list.append(row[0])
    return data_list


def query_name_list():
    data_list = []
    sql = "select distinct name from catering;"
    results = connect.executeQuery(sql)
    if len(results) > 0:
        for row in results:
            data_list.append(row[0])
    return data_list


def query_price_max():
    data_list = []
    sql = "select kind, round(max(price), 2) from catering group by kind;"
    results = connect.executeQuery(sql)
    if len(results) > 0:
        for row in results:
            data_list.append(int(row[1]))
    return data_list


def query_price_min():
    data_list = []
    sql = "select kind, round(min(price), 2) from catering group by kind;"
    results = connect.executeQuery(sql)
    if len(results) > 0:
        for row in results:
            data_list.append(int(row[1]))
    return data_list


def query_price_avg():
    data_list = []
    sql = "select kind, round(avg(price), 2) from catering group by kind;"
    results = connect.executeQuery(sql)
    if len(results) > 0:
        for row in results:
            data_list.append(int(row[1]))
    return data_list


def query_types_list_pie():
    data_list = []
    sql = "select type, count(*) from catering group by type;"
    results = connect.executeQuery(sql)
    if len(results) > 0:
        for row in results:
            data_list.append({'name': row[0], 'value': int(row[1])})
    return data_list


def query_types_list_bar():
    data_list = []
    sql = "select type, count(*) from catering group by type;"
    results = connect.executeQuery(sql)
    if len(results) > 0:
        for row in results:
            data_list.append(int(row[1]))
    return data_list


def query_kinds_list_bar():
    data_list = []
    sql = "select kind, count(*) from catering group by kind;"
    results = connect.executeQuery(sql)
    if len(results) > 0:
        for row in results:
            data_list.append(int(row[1]))
    return data_list


def query_kinds_list_pie():
    data_list = []
    sql = "select kind, count(*) from catering group by kind;"
    results = connect.executeQuery(sql)
    if len(results) > 0:
        for row in results:
            data_list.append({'name': row[0], 'value': int(row[1])})
    return data_list


def query_name_list_bar():
    data_list = []
    sql = "select name, count(*) from catering group by name;"
    results = connect.executeQuery(sql)
    if len(results) > 0:
        for row in results:
            data_list.append(int(row[1]))
    return data_list


def query_search(type, kind, name):
    data_list = []
    sql = "select * from catering where 1=1"
    if type is not None and len(type) > 0: sql = sql + " and type='" + str(type) + "'"
    if kind is not None and len(kind) > 0: sql = sql + " and kind='" + str(kind) + "'"
    if name is not None and len(name) > 0: sql = sql + " and name like '%" + str(name) + "%'"
    results = connect.executeQuery(sql)
    if len(results) > 0:
        for row in results:
            data = {"id": row[0], "type": row[1], "kind": row[2], "name": row[3], "price": row[4]}
            data_list.append(data)
    return data_list
