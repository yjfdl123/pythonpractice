#coding=utf-8
# 时间戳装饰函数

from functools import wraps
import time
def time_wrap(func):
    print func
    @wraps(func)
    def decrator(*args,**kwargs):
        start = time.time()
        print 'start time:',start,'exec',func.__name__
        result = func(*args,**kwargs)
        end = time.time()
        print 'end time:',end
        print 'use time:',end-start
        return result
    return decrator


@time_wrap
def printx(x=100):
    '''
        reverse print x
    '''
    while x>0:
        x=x-1
    return x+2


if __name__=='__main__':
    import sys
    print sys.argv
    argnum = len(sys.argv)
    inputx = 100
    if argnum>1:
        inputx = int(sys.argv[1])
    printx(inputx)
