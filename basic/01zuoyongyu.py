#lambada 面试题
import sys
print(help(sys))
li = [lambda :x for x in range(10)]
  
res = li[0]()
res = li[1]()
print(res)
print(li)
print( len(li) )
  
#输出：9s