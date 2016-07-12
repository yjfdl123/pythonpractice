#coding=utf-8

import jenkinsapi
from jenkinsapi.jenkins import Jenkins
from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('config.ini')

class myjenkins(object):
	def __init__(self):
		self.host = cfg.get('jenkins','host')
		self.user = cfg.get('jenkins','username')
		self.pas = cfg.get('jenkins','password')
		self.jen  = Jenkins(self.host,username='yjfdl123',password='123456')
		print self.jen.keys()

	def trigger(self):
		pass

	def get_log(self):
		pass

	def get_all_jobs(self):
		for name,job in self.jen.get_jobs():
			print job.name,' '#job.get_description(),' ',
			#print job.is_running(),' '#,job.is_enabled()
			thejob = self.jen.get_job(name)
			#print 'descri: ',thejob.get_description()
			#print 'running:',thejob.is_running()
			print 'enable:',thejob.is_enabled()
			lgb = thejob.get_last_good_build()
			print 'lgb:',lgb
			print 'version:',lgb.get_revision()
			print '--------'
			

	def test(self):
		self.get_all_jobs()	


if __name__=='__main__':
	print 'yes'
	tjen = myjenkins()
	tjen.test()
