
class test(object):
	def __init__(self):
		print 'init'
		self._res={}
		self.body=""

	def __setitem__(self,key,value):
		self._res[key] = value

	def __getitem__(self,key):
		return self._res[key]

	def __iadd__(self,value):
		self.body+=value
		return self

	def __call__(self,key=""):
		print "call:",key

x=test()
x['a'] = 'ssd'
x+='123123'
x()
x("123")


