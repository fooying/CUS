#!/usr/bin/python
#encoding=utf-8
#by Fooying 2013/04/18


import sys
import modules
import config
import datetime
import redis
from fooying.cnsite import config as a_config
from fooying.cnsite.public import create_task
from fooying.kslog import KSLOG

Db_rds = redis.Redis(a_config.Redis_ip)
Queue_rds = redis.Redis(a_config.Queue_redis_ip)
Log = KSLOG(config.Log_path)
Log_template = '%(messg)s'

def check(url,codeurl,eng,timeout):
	engine = getattr(__import__('modules.%s'%eng),eng)
	result = engine.check(url)
	s_result = {'codeurl':url,'c_time':datetime.datetime.now(),'result':result,'engine':eng}
	if not Db_rds.rpush(a_config.TASK_RESULT,s_result):
		create_task(codeurl,url)
	else:
		Queue_rds.lpop(a_config.TASK_ENGINE+eng)
		num = Db_rds.hget(a_config.TASK_INFO+codeurl,'code')
		Db_rds.hset(a_config.TASK_INFO+codeurl,'code',int(num)+1)
		if int(num)+1 == int(a_config.Engine_num):
			Db_rds.hset(a_config.TASK_INFO+codeurl,'task_statu',1)
		

if __name__ == '__main__':
	eng = sys.argv[1]
	timeout = sys.argv[2]
		
	while True:
		try:
			task = Queue_rds.lrange(a_config.TASK_ENGINE+eng,0,1)
			if task:
				task = eval(task[0])
				url = task['url']
				codeurl = task['codeurl']
				check(url,codeurl,eng,timeout)
		except Exception,e:
			messg = e
			Log.warning(Log_template%vars())

