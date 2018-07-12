from flask import Flask, request, g, make_response, session, Session
import json
import hashlib
import redis
import pymysql
import logging
from .session_interface import RedisSessionInterface

logging.basicConfig(filename='my_log.my_log',
                    format='[T:%(asctime)s|E:%(filename)s|F:%(funcName)s|L:%(lineno)d|L:%(levelname)s]|%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'mykey'

app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
app.config['SESSION_PERMANENT'] = True  # 如果设置为True，则关闭浏览器session就失效。
app.config['SESSION_USE_SIGNER'] = True  # 是否对发送到浏览器上session的cookie值进行加密
app.config['SESSION_KEY_PREFIX'] = 'TOKEN'  # 保存到session中的值的前缀
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port='6379', password='root')  # 用于连接redis的配置
app.session_interface = RedisSessionInterface()


@app.before_request
def conn_db():
    config = {
        'host': '192.168.0.101',
        'port': 3306,
        'user': 'admin007',
        'password': 'myadmin@816',
        'db': 'zcs',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor
    }

    g.conn = pymysql.connect(**config)
    g.cursor = g.conn.cursor()


@app.teardown_request
def release_db(response):
    g.cursor.close()
    g.conn.close()
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    data = json.loads(request.get_data(as_text=True))
    hash = hashlib.sha256(data['username'].encode('utf-8'))
    hash.update(data['password'].encode('utf-8'))
    secret = hash.hexdigest()
    g.cursor.execute('SELECT password FROM user_info WHERE username=%s', data['username'])
    db_data = g.cursor.fetchone()
    if db_data['password'] == secret:
        session['username'] = data['username']  # 如果登录成功，将生成的sid写入cookie
        response = make_response('登录成功')
        return response
    else:
        return '登录失败'


@app.route('/register', methods=['GET', 'POST'])
def register():
    data = json.loads(request.get_data(as_text=True))
    hash = hashlib.sha256(data['username'].encode('utf-8'))  # 加盐，使用用户名作为key
    hash.update(data['password'].encode('utf-8'))
    secret = hash.hexdigest()  # 加密后的密码
    try:
        g.cursor.execute('INSERT INTO user_info(username, password) VALUES (%s,%s)', (data['username'], secret))
        g.conn.commit()
        return '注册成功'
    except Exception as e:
        logging.debug(e)
        g.conn.rollback()
        return '出错'


@app.route('/index', methods=['GET'])
def index():
    return session['username']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

