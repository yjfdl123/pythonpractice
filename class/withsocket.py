#coding=utf-8
import socket

class withclient(object):
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 11248

    def __enter__(self):
        print 'enter'
        self.csock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        hostport=(self.host,self.port)
        self.csock.connect(hostport)
        return self.csock

    def __exit__(self,a,b,c):
        print 'out'
        self.csock.close()


with withclient() as sock:
    print 1
    sock.send('hello world')
    xx=sock.recv(1000)
    print xx
    print 2

