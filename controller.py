from flask import Flask, render_template, request

import service

app = Flask(__name__)


# flask框架启动
def startWeb(): app.run()


# 网站首页
@app.route('/')
def index():
    return render_template("index.html")


# 价格趋势分析
@app.route('/price', methods=['GET'])
def price():
    # 获取各菜品种类及最高价、最低价、平均价
    price_x, price_y = service.query_price()
    # 跳转页面并返回数据
    return render_template("price.html", price_x=price_x, price_y=price_y)


# 三餐种类分析
@app.route('/types', methods=['GET'])
def types():
    # 获取各三餐种类及食用数量
    types_x, types_y = service.query_types()
    # 跳转页面并返回数据
    return render_template("types.html", types_x=types_x, types_y=types_y)


# 菜品种类分析
@app.route('/kinds', methods=['GET'])
def kinds():
    # 获取各菜品种类及食用数量
    kinds_x, kinds_y = service.query_kinds()
    # 跳转页面并返回数据
    return render_template("kinds.html", kinds_x=kinds_x, kinds_y=kinds_y)


# 项目与技术
@app.route('/query', methods=['GET'])
def query():
    # 查询三餐种类
    types = service.query_types_list()
    # 查询餐品种类
    kinds = service.query_kinds_list()
    # 返回前端数据
    return render_template("query.html", types=types, kinds=kinds)


@app.route('/query_search', methods=['POST'])
def query_search():
    # 获取前端数据
    type = request.form['type']
    kind = request.form['kind']
    name = request.form['name']
    # 查询数据
    query_result = service.query_search(type, kind, name)
    # 查询三餐种类
    types = service.query_types_list()
    # 查询餐品种类
    kinds = service.query_kinds_list()
    # 返回前端数据
    return render_template("query.html", query_result=query_result, types=types, kinds=kinds)


@app.route('/forecast', methods=['GET'])
def forecast():
    # 查询数据
    fore_x, fore_y = service.query_forecast()
    # 返回前端数据
    return render_template("forecast.html", fore_x=fore_x, fore_y=fore_y)


# 项目与技术
@app.route('/project', methods=['GET'])
def project():
    return render_template("project.html")
