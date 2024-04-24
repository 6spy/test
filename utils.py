import random
import connect


# 读取Excel文件数据，存入Mysql数据库
def createMysqlData():
    global price, name
    names1 = [
        '白灼大虾',
        '红烧猪蹄',
        '卤鸡腿',
        '黑椒猪扒',
        '黄相鸡',
        '鱼香排骨',
        '可乐鸡翅',
        '香酥肉排',
        '红烧肉',
        '脆皮带鱼',
        '荔枝肉',
        '清蒸鳄鱼',
        '椒盐龙利鱼',
        '口水鸡',
        '烤鸭',
        '锅包肉',
        '椒盐大排',
        '盐煎肉',
        '东坡肉',
        '咖喔鸡',
        '葱油花蛤',
        '白切鸡',
        '蒜香牛仔骨',
        '姜母鸭',
        '潮式卤鸭',
        '叉烧排骨',
        '炸黄瓜鱼',
        '奥尔良腿排',
        '爆炒跳鱼',
        '尖椒回锅肉',
        '辣子鸡',
        '松子鱼',
        '爆炒猪肝',
        '烧小酥肉',
        '拌猪耳',
        '红烧牛脯',
        '蒜泥白肉',
        '啤酒鸭',
        '红烧马鲸鱼',
        '卤鸭边腿',
        '粉蒸鸡',
        '三杯鸡',
        '红烧鱼',
        '螃蟹爆蛋',
        '咸水鸭',
        '泡椒田鸡',
        '开胃鸭畛',
        '五香卷',
        '蛋肉堡',
        '宫爆鸡丁',
        '椒盐猪尾',
        '梅菜扣肉',
        '清蒸淡水瓜',
        '红油猪心',
        '醉排骨',
        '炸鸡柳',
        '炸虾饼',
        '美味猪舌',
        '宫保虾球',
        '蒸蛋饺'
    ]
    names2 = [
        '甜笋炒肉', 
        '蒜台炒肉丝', 
        '西芹炒腊肉', 
        '香菇炒肉', 
        '青椒炒拱嘴', 
        '蒜台炒香肠', 
        '虾米炖蛋', 
        '腐竹炒肉', 
        '韭黄炒蛋', 
        '芹菜炒肉末', 
        '西红柿炒蛋', 
        '西芹炒肉', 
        '木耳炒肉', 
        '杏鲍菇炒肉', 
        '双菇烷牛滑', 
        '粉条炖肉', 
        '菱白炒肉', 
        '青椒炒蛋', 
        '双椒炒凤片', 
        '斐白炒蛋', 
        '青椒炒肉', 
        '水煮肉片', 
        '平菇炒肉', 
        '豆干炒肉', 
        '双冬燃火腿', 
        '土豆炒肉', 
        '酸菜烧肉', 
        '玉米炒蛋', 
        '京酱肉丝', 
        '豆角炒沫', 
        '酸菜炒蛋', 
        '青椒炒小肠', 
        '胡瓜炒花蛤', 
        '丝瓜烧丸子', 
        '魔域烧鸭', 
        '香菇滑鸡片', 
        '花菜炒香肠', 
        '韭菜炒肉丝', 
        '榨菜炒肉丝', 
        '葛笋炒肉片', 
        '青椒炒鸭心', 
        '酸辣猪皮', 
        '海带结烧肉', 
        '水煮鱼', 
        '蚂蚁上树', 
        '青椒罗汉肉', 
        '尖椒炒培根', 
        '肉丁烧芋头'
    ]
    names3 = [
        '清炒荷兰豆', 
        '清炒黄笋', 
        '干煽四季豆', 
        '酸辣莲穗', 
        '木耳炒山药', 
        '青蒜炒平菇', 
        '香炒芋头', 
        '红烧冬瓜', 
        '酸辣海带丝', 
        '拌苦瓜', 
        '韭菜炒豆芽', 
        '玉米三鲜', 
        '雷爆加子', 
        '蒜泥长豆', 
        '燎黄瓜', 
        '红烧面筋', 
        '炒西兰花', 
        '烧日本豆腐', 
        '青椒炒土豆', 
        '千页豆腐', 
        '炒花菜', 
        '清炒丝瓜', 
        '炒胡瓜', 
        '花生拌西芹', 
        '家常豆腐', 
        '蒸南瓜', 
        '冬笋炒酸菜', 
        '韭菜豆腐泡', 
        '麻辣豆腐', 
        '佛手瓜', 
        '拌金针菇', 
        '芹菜拌千张', 
        '清炒小瓜', 
        '蒜苗炒萝卜', 
        '素炒长豆', 
        '卤豆腐片'
    ]
    names4 = [
        '玉米老鸭汤', 
        '海带结排骨', 
        '虫草枸杞鸡汤', 
        '酸辣猪皮汤', 
        '萝卜排骨汤', 
        '海蛎豆腐汤', 
        '山药萝卜羹', 
        '榨菜肉丝汤', 
        '香菇豆腐汤', 
        '苦瓜蛋羹', 
        '萝卜筒骨汤', 
        '丝瓜蛋汤', 
        '莲藕排骨汤', 
        '花蛤豆腐汤', 
        '海带肉丝汤', 
        '鲫鱼豆腐汤', 
        '冬瓜淡菜汤', 
        '枸杞山药乌鸡'
    ]
    names5 = ['米饭', '馒头', '花卷', '糖三角', '炒饭', '水饺', '馄饨', '包子', '炒面', '炸酱面', '面包']
    names6 = ['八宝粥', '绿豆粥', '银耳莲子粥', '黑米粥', '皮蛋瘦肉粥', '南瓜粥', '鸡肉粥', '红枣粥', '小米粥', '大米粥']
    types = ['早餐', '午餐', '晚餐']
    kinds1 = ['主食', '粥']
    kinds2 = ['荤菜', '荤素', '素菜', '汤类']

    for row in range(2490):
        type = random.choice(types)
        if type == '早餐':
            kind = random.choice(kinds1)
            if kind == '主食': name = random.choice(names5); price = random.randint(1, 3)
            if kind == '粥': name = random.choice(names6); price = random.randint(2, 5)
        else:
            kind = random.choice(kinds2)
            if kind == '荤菜': name = random.choice(names1); price = random.randint(6, 11)
            if kind == '荤素': name = random.choice(names2); price = random.randint(3, 8)
            if kind == '素菜': name = random.choice(names3); price = random.randint(2, 5)
            if kind == '汤类': name = random.choice(names4); price = random.randint(5, 10)

        sql = "insert into catering(type, kind, name, price) values('"+type+"', '"+kind+"', '"+name+"', '"+str(price)+"');"

        connect.executeCRUD(sql)
