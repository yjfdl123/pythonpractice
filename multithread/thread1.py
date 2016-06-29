#coding=utf-8
import threading
from time import ctime,sleep
def myprint():   
    print 'start;',ctime()
    sleep(3)
    print 'end:',ctime()


t= threading.Thread(target=myprint,args=())
t.start()
print t.isAlive()



sleep(4)
print t.isAlive()

