import socket
# from socket import *
host  = socket.gethostname()
print host
host = 'www.baidu.com'
ip = socket.gethostbyname(host)
print ip

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print s.gettimeout()
s.settimeout(10)
print s.gettimeout()
x=s.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
y=s.getsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF)
print x
print y
s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,2000)
x=s.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
y=s.getsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF)
print x
print y