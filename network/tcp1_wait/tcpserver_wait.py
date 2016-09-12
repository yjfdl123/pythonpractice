#coding=utf-8
#tcp server

import socket
import time
import threading
import Queue
import logging
import time
import config
logging.basicConfig(level=logging.INFO,filename='log/tcp1.log')
cliqueue = Queue.Queue(5)
maxsize=1000
flag_thread=True
def echoclient():
    while flag_thread:
        newclisock,addr = cliqueue.get(1)
        print "tackle info :",addr
        while True:
            total=''
            data = newclisock.recv(maxsize) 
            print 'data',data
            newclisock.send('hello '+data+'\n')
            newclisock.close()
            break

            if not data:
                break
            else:
                total+=data
                logging.info('data:'+str(data))
                print 'data:',data
                newclisock.send(time.ctime()+data+'\n')
                try:
            		newclisock.send(total)
                except Exception,e:
                    print e
    
        


def startserver():
    ip=''
    port=config.port
    tcpserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    
    tcpserver.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
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
            cliqueue.put((newcli,addr),1)
        except Exception,e:
            print "ex:",Exception
            print "e:",e
            tcpserver.close()
            
if __name__=='__main__':
    startserver()
