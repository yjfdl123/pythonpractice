#coding=utf-8
# map 
# reduce



xx=map(lambda x,y:(x,y),[1,2,3],[2,3,4]) 
print xx


yy=reduce(lambda x,y:(x,y),range(10))
print yy
