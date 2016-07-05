#coding=utf-8
#可变长度的参数，元组，字典



def print_para(x,y,*a,**b):
	print 'x:',x
	print 'y:',y
	for item in a:
		print 'tuple:  ',item
	for key in b.keys():
		print 'key: ',key,b[key]


if __name__=='__main__':
	print_para(1,2,3,4,t=5,e=6,w=7)
	print '\n\n'
 	atuple = (11,23,45)	
	adict  = {'name':'yjf','address':'gz','tel':'133'}
	print_para(1,2,t=5,e=6,*atuple,**adict)
