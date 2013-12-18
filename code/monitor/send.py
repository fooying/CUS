#!/usr/bin/python
#encoding=utf-8
#by Fooying 2013/04/18


import sys
sys.path.append('/opt/')
import redis
from fooying.cnsite import config as a_config
from fooying.cnsite.public import create_task
from fooying.flog import FLOG

Db_rds = redis.Redis(a_config.Redis_ip)
Queue_rds = redis.Redis(a_config.Queue_redis_ip)
Log = FLOG(a_config.Send_log_path)
Log_template = '%(messg)s'

if __name__ == '__main__':
	while True:
		try:
			task = Queue_rds.lrange(a_config.TASK_LIST,0,1)
			if task:
				task = eval(task[0])
				try:
					for e in a_config.Engines:
						Queue_rds.rpush(a_config.TASK_ENGINE+e,task)
				except Exception,e:
					messg = str(e)
					Log.warning(Log_template%vars())
				else:
					Queue_rds.lpop(a_config.TASK_LIST)
		except Exception,e:
			print e
			messg = str(e)
			Log.warning(Log_template%vars())

