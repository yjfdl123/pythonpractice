#coding=utf-8
#tcp server

import socket
import time
import threading
import Queue
import logging
import time
logging.basicConfig(level=logging.INFO,filename='log/tcp1.log')
cliqueue = Queue.Queue(5)
maxsize=1000
flag_thread=True
def echoclient():
	while flag_thread:
		newclisock = cliqueue.get(1)
		while True:
			total=''
			data = newclisock.recv(maxsize) 
			print 'data',data
			if not data:
				break
			else:
				total+=data
				logging.info('data:'+str(data))
                                print 'data:',data
				newclisock.send(time.ctime()+data)
                try:
		    newclisock.send(total)
                except Exception,e:
                    print e
	
		


def startserver():
	ip=''
	port=11248	
	tcpserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)	
	tcpserver.bind((ip,port))
        print 'server listen in ',port
	tcpserver.listen(3)


	th_cli = threading.Thread(target=echoclient,args=())
	th_cli.setDaemon(True)
	th_cli.start()

	while True:
		try:
			newcli,addr = tcpserver.accept()	
                        print 'connect from ',addr
			logging.info('connect from'+str(addr))
			cliqueue.put(newcli,1)
		except Exception,e:
			print "ex:",Exception
			print "e:",e
			tcpserver.close()
			
if __name__=='__main__':
	startserver()
