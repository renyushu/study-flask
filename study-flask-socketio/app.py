from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
# socketio = SocketIO(app, cors_allowed_origins="*")
socket_io = SocketIO(app, async_mode='gevent', cors_allowed_origins="*")


@socket_io.on('my_event', namespace='/')
def handle_my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)


@app.route("/")
def hello_world():
    return "<p>Hello, World! Hello Flask hhhh</p>"


if __name__ == "__main__":
    socket_io.run(app, host="localhost", port=5001)
