#!/usr/bin
#encoding=utf-8
#by Fooying 2013/04/18

import config
import os

if __name__ == '__main__':
	for item,value in config.workers.items():
		num = value['num']
		timeout = value['timeout']
		for i in range(num):
			os.system('python worker.py %s %s &'%(item,timeout))
			
