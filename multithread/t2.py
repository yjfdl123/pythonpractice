#coding=utf-8


import threading
from time import sleep,ctime
from Queue import Queue
import logging
logging.basicConfig(level=logging.INFO,filename='log/info.log')
class mytask(object):
	def __init__(self):
		self.num = 0
		self.task_queue = Queue(10)
		self.flag_thread = True
		self.task_thread = None
		logging.info('init')

	def add(self):
		while True:
			self.num+=1
			self.task_queue.put(self.num,1)
			logging.info('push:'+str(self.num))
			if self.task_thread==None:
				self.task_thread = threading.Thread(target=self.dec,args=())
				self.task_thread.setDaemon(True)
				self.task_thread.start()
			sleep(1)
				
			

	def dec(self):
		while self.flag_thread:
			xx=self.task_queue.get(1)
			logging.info('pop'+str(xx))
			sleep(2)

				
if __name__=='__main__':
	task=mytask()
	task.add()
