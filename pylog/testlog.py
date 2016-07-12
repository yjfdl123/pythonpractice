#coding=utf-8


import logging
import logging.handlers
#logging.basicConfig(level = logging.INFO,filename='info.log')

myhandler = logging.StreamHandler()
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
myhandler.setFormatter(formatter)

logger = logging.getLogger('yjf')
logger.addHandler(myhandler)
logger.setLevel(logging.DEBUG)

logger.info('start')
logger.debug('test')
