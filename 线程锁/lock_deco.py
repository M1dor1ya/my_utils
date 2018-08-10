# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 14:14
# @Author  : Zcs
# @File    : lock_deco.py
import json
from flask import make_response


#  lock = threading.Lock()
def lock_deco(lock):
    def _lock_deco(func):
        def warpper(*args, **kwargs):
            if lock.acquire(timeout=2):
                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    lock.release()
            else:
                return_dict = {"status": "1", "msg": "当前有其他用户正在操作该资源，请稍后再试"}
                json_data = json.dumps(return_dict)
                resp = make_response(json_data)
                resp.headers['Content-Type'] = 'text/json'
                return resp
        return warpper
    return _lock_deco

