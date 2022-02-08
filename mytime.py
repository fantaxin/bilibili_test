# -*- coding:utf-8 -*-
import time

import mytime
import datetime
from functools import wraps


def time_now():
    time = datetime.datetime.now()
    return time


def sleep(seconds=1.0):
    """
    睡眠时间
    """
    time.sleep(seconds)


def running_time(func):
    """函数运行时间"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time_now()
        res = func(*args, **kwargs)
        print("校验元素done！用时%.3f秒！" % (time_now() - start))
        return res

    return wrapper


if __name__ == '__main__':
    a = time_now()
    print(a)
    sleep(3)
    b = time_now()
    print(b)
    print(b-a)
