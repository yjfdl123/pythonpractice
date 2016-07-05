#coding=utf-8
#可变长度的参数，元组，字典



def print_para(x,y,*a,**b):
	print 'x:',x
	print 'y:',y
	for item in a:
		print item
	for key in b.keys():
		print key,b[key]


if __name__=='__main__':
	print_para(1,2,3,4,t=5,e=6,w=7)
