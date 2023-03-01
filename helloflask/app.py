from flask import Flask, request

# 首先我们从 flask 包导入 Flask 类，通过实例化这个类，创建一个程序对象 app：
app = Flask(__name__)


# 注册一个处理函数，这个函数是处理某个请求的处理函数，Flask 官方把它叫做视图函数（view funciton），你可以理解为“请求处理函数”。
# 所谓的“注册”，就是给这个函数戴上一个装饰器帽子
@app.route('/') # 注册
@app.route('/index')
@app.route('/home')
def hello():  # 视图函数
    return 'Welcome to My Watchlist!'


@app.route('/users', methods=['GET', 'POST'])
def users():
    print(request.method)       # 请求方法
    print(request.headers)      # 请求的headers
    print(request.path)         # 资源路径
    print(request.url)          # 完整的url
    print(request.remote_addr)  # 客户端IP
    print(request.cookies)      # 请求的cookie
    return 'ok'

from flask import Flask, jsonify, render_template, Response


app = Flask(__name__)

@app.route('/text')
def get_text():
    return '返回文本'

@app.route('/dict')
def get_dict():
    return {'state': 0}


@app.route('/json')
def get_json():
    return jsonify({'state': 0})


@app.route('/html')
def get_html():
    return render_template('index.html')

@app.route('/response')
def get_resonponse():
    return Response('Not Found', status=404)
