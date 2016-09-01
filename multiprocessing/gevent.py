import gevent
import time
def sle(num):
	print num
	time.sleep(num)


g = gevent.spawn(sle,10)
i = 0
while g:
	i+=1
	print i
	time.sleep(1)
