#coding=utf-8
#tcp client


import socket
import time
import logging
logging.basicConfig(level=logging.INFO,filename='log/cli1.log')


maxsize = 1000
def startclient():
	ip = 'localhost'
	port=11248	
	tcpsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:	
		tcpsock.connect((ip,port))
	except Exception,e:
		print 'not connect',Exception
		print e 
		return	

	while True:
		data = raw_input('>')
		print 'send:',data
		if  data:
			try:	
				tcpsock.send(data)
			except:
				print 'send error'
				print Exception
				print e
			
			try:	
				ret = tcpsock.recv(maxsize)	
			except Exception,e:
				print Exception
				print e
				print 'server bad,i will quit'
				break

			print 'server said:   ',ret
		else:
			tcpsock.close()
			break


if __name__=='__main__':
	startclient()

