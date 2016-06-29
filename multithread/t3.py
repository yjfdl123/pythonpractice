#coding=utf-8

import threading
from Queue import Queue
from time import sleep,ctime
import logging
logging.basicConfig(level=logging.INFO,filename='log/t3.log')

class mythread(threading.Thread):
	def __init__(self,func,args):
		threading.Thread.__init__(self)
		self.func = func
		self.args = args

	def run(self):
		logging.info('begin')
		result=apply(self.func,self.args)


def add(x,y):
	logging.info(str(x)+'+'+str(y))
	sleep(30)



if __name__=='__main__':
	num=0
	th_list = []
	while True:
		num+=1
		newth =  mythread(add,(num,num+1))
		newth.setName('myth_'+str(num))
		newth.setDaemon(True)
		newth.start()
		logging.info('th count:'+str(threading.activeCount()))
		for th in threading.enumerate():	
			logging.info(th.getName()+' is alive')
		sleep(3)
		

		
