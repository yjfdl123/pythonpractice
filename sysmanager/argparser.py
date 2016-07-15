#coding=utf-8
#arg parser

import argparse

class myparser(object):
	def __init__(self):
		self.parser = argparse.ArgumentParser(description='test argparser')
		self.parser.add_argument(dest='filenames',metavar='filename',nargs='*')
		self.parser.add_argument('-res',metavar='res svn',dest='res',help='res help')
		pass

	def test(self):
		print 'test:'

if __name__=='__main__':
	pa = myparser()
	args=pa.parser.parse_args()
	print args 
	print args.filenames
 
