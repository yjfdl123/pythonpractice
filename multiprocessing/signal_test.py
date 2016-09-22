import multiprocessing
import time,os
import signal
import sys

def atexit1(sig,frame):
	print 'chuli zijincheng'
	print sig,frame
	sys.exit(0)
	
childpid = None

def atchildexit(sig,frame):
	print 'child exit'
	print sig,frame

def atexit_kill(sig,frame):
	print 'kill child',childpid
	os.kill(childpid,signal.SIGINT)

def add():
	signal.signal(signal.SIGINT,atexit1)
	while True:
		time.sleep(3)
		print 3

signal.signal(signal.SIGCHLD,atchildexit)
signal.signal(signal.SIGINT, atexit_kill)
p = multiprocessing.Process(target=add,args=())	
p.Daemon = True
p.start()
childpid =  p.pid
print 'start'
time.sleep(2)
#p.terminate()
print p.pid
print 'terminate'
while True:
	time.sleep(1)
	if p.is_alive():
		print 'alive'
	else:
		p = multiprocessing.Process(target=add,args=())	
		p.Daemon = True
		p.start()
		childpid =  p.pid
		print 'restart at pid:',p.pid

