# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 9:43
# @Author  : Zcs
# @File    : session_interface.py
import pickle
from datetime import timedelta
from uuid import uuid4
from redis import Redis
from werkzeug.datastructures import CallbackDict
from flask.sessions import SessionInterface, SessionMixin


class RedisSession(CallbackDict, SessionMixin):
    #  继承字典，同时自身拥有三个属性sid new modified
    #  如果没有进行session[key] = value 赋值操作的话，其是个空字典
    def __init__(self, initial=None, sid=None, new=False):
        def on_update(self):
            self.modified = True
        CallbackDict.__init__(self, initial, on_update)
        self.sid = sid
        self.new = new
        self.modified = False


class RedisSessionInterface(SessionInterface):
    serializer = pickle
    session_class = RedisSession

    def __init__(self, redis=None, prefix='session:'):
        if redis is None:
            redis = Redis()
        self.redis = redis
        self.prefix = prefix

    def generate_sid(self):
        return str(uuid4())

    def get_redis_expiration_time(self, app, session):
        if session.permanent:
            return app.permanent_session_lifetime
        return timedelta(days=1)

    #  在请求进入视图函数之前，从redis中取出session_id对应的数据供视图函数使用
    #  如果cookie中不存在session_id就生成一个
    def open_session(self, app, request):
        sid = request.cookies.get(app.session_cookie_name)  # 从cookie中获取session_id

        #  如果session_id不存在，生成一个并返回
        if not sid:
            sid = self.generate_sid()
            return self.session_class(sid=sid, new=True)
        val = self.redis.get(self.prefix + sid)
        if val is not None:
            data = self.serializer.loads(val)
            return self.session_class(data, sid=sid)
        return self.session_class(sid=sid, new=True)

    #  save_session执行与视图函数之后，传入的session为open_session生成或获取到的session
    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        #  没有进行session[key] = value赋值的话，session为空字典
        if not session:
            #  if not {} 返回True，执行以下代码
            self.redis.delete(self.prefix + session.sid)
            if session.modified:
                response.delete_cookie(app.session_cookie_name,
                                       domain=domain)
            return
        redis_exp = self.get_redis_expiration_time(app, session)
        cookie_exp = self.get_expiration_time(app, session)
        val = self.serializer.dumps(dict(session))
        self.redis.setex(self.prefix + session.sid, val,
                         int(redis_exp.total_seconds()))
        response.set_cookie(app.session_cookie_name, session.sid,
                            expires=cookie_exp, httponly=True,
                            domain=domain)
