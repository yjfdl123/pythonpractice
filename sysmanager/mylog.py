#coding=utf-8
# log 
# 装饰函数打印执行时间
import logging
from functools import wraps
import time
logging.basicConfig(level=logging.INFO,
        filename='wraplog.txt',
        format='%(levelname)s,%(asctime)s,%(message)s')
def log_wrap(func):
    @wraps(func)
    def decorate(*args,**kwargs):
        logging.info('exec %s time:%s',func.__name__,time.ctime())
        result = func(*args,**kwargs)
        return result

    return decorate
@log_wrap
def add(x):
    return x+1

print add(3)

