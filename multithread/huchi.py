#coding=utf-8
import threading

class Counter(object):
	def __init__(self):
		self.x = 1

	def incre(self):
		self.x +=1

	def out(self):
		print self.x

counter = Counter()

def add():
	for i  in range(10000): 
		counter.incre()

t1 = threading.Thread(target=add,args=())
t2 = threading.Thread(target=add,args=())
t1.start()
t2.start()

t1.join()
t2.join()

counter.out()

