from flask import Flask, session, make_response, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to gusss'

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/login/<string:username>')
def name_view(username):
    session['username'] = username
    return 'ok'

@app.route('/')
def get_name():
    if 'username' not in session:
        return 'not login'
    else:
        return 'welcome ' + session['username']

@app.route('/set/<name>')
def set_cookie(name):
    res = make_response(redirect(url_for('hello')))
    res.set_cookie('name', name)
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5501)