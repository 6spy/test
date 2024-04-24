import pymysql


# Mysql数据库相关定义
def MySqlHost(): return '127.0.0.1'
def MySqlPort(): return 3306
def MySqlUser(): return 'root'
def MySqlPasswd(): return '126152'
def MySqlDb(): return 'canteenflow'


# 数据库的CRUD
def executeCRUD(sql):
    # 连接数据库
    conn = pymysql.connect(host=MySqlHost(), port=MySqlPort(), user=MySqlUser(), passwd=MySqlPasswd(), db=MySqlDb(), charset='utf8')
    # 创建游标
    cur = conn.cursor()
    try:
        # 批量执行多条SQL语句
        # cur.executemany(sql, data)
        cur.execute(sql)
        # 提交事务
        conn.commit()
    except Exception as e:
        # 打印报错日志
        print('SQL语句：', sql)
        print('SQL语句执行错误提示：', e)
        # 有异常，回滚事务
        conn.rollback()
    # 关闭指针对象
    cur.close()
    # 关闭连接对象
    conn.close()


def executeQuery(sql):
    # 连接数据库
    conn = pymysql.connect(host=MySqlHost(), port=MySqlPort(), user=MySqlUser(), passwd=MySqlPasswd(), db=MySqlDb(), charset='utf8')
    # 创建游标
    cur = conn.cursor()
    try:
        cur.execute(sql)
        results = cur.fetchall()
    except Exception as e:
        # 打印报错日志
        print('SQL语句执行错误提示：', e)
        # 有异常，回滚事务
        conn.rollback()
    # 关闭指针对象
    cur.close()
    # 关闭连接对象
    conn.close()
    # 返回结果集
    return results
