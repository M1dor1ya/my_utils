# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 17:17
# @Author  : Zcs
# @File    : test.py
import hashlib
#from werkzeug.datastructures import CallbackDict
from flask.sessions import SessionInterface, SessionMixin
# hash = hashlib.sha256('mysalt'.encode('utf-8'))
# hash.update('admin'.encode('utf-8'))
# secret = hash.hexdigest()
# print(secret)


class UpdateDictMixin(object):

    """Makes dicts call `self.on_update` on modifications.

    .. versionadded:: 0.5

    :private:
    """

    on_update = None

    def calls_update(name):
        def oncall(self, *args, **kw):
            rv = getattr(super(UpdateDictMixin, self), name)(*args, **kw)
            if self.on_update is not None:
                self.on_update(self)
            return rv
        oncall.__name__ = name
        return oncall


class CallbackDict(UpdateDictMixin, dict):

    """A dict that calls a function passed every my_time something is changed.
    The function is passed the dict instance.
    """

    def __init__(self, initial=None, on_update=None):
        dict.__init__(self, initial or ())
        self.on_update = on_update

    def __repr__(self):
        return '<%s %s>' % (
            self.__class__.__name__,
            dict.__repr__(self)
        )


class RedisSession(CallbackDict, SessionMixin):

    def __init__(self, initial=None, sid=None, new=False):
        def on_update(self):
            self.modified = True
        CallbackDict.__init__(self, initial, on_update)
        self.sid = sid
        self.new = new
        self.modified = False

        print(self.sid, self.new, self.modified)






obj = RedisSession(sid='qwejiqt', new=True)
print(obj)
if obj == {}:
    print(2)
    print(obj.sid)

if not obj:
    print(1)