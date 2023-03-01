from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import click


db_username = 'root'
db_pd = 'admin2022.'
db_name = 'flask_db'
db_host = '127.0.0.1'
db_port = '3306'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_username}:{db_pd}@{db_host}:{db_port}/{db_name}?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)


class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字


class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份


@app.cli.command()  # 注册为命令，可以传入 name 参数来自定义命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Movie=Movie)


@app.route('/')
def hello_world():
    return 'Hello World! db'

#
# if __name__ == '__main__':
#     app.run(port=5678)