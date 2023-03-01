from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("connect")
def handle_connect():
    print("【server】 has connected")
    emit("my response", "server has connected。 ")


@socketio.on("connect", namespace='/name1')
def handle_connect():
    print("【server1】 has connected")
    emit("my response", "server1 has connected。 ")


@socketio.on("my event", namespace='/name1')
def handle_event(message):
    print("【server1】-服务器已经接收到消息：" + message["data"])
    emit("my response", "服务器1已经接收到消息：" + message["data"])


@socketio.on("my event")
def handle_event(message):
    print("【server】-服务器已经接收到消息：" + message["data"])
    emit("my response", "服务器已经接收到消息：" + message["data"])


@socketio.on('message')
def handle_message(message):
    print('【server】接收到消息:' + message)


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port='5100', debug=True)