#!/usr/bin/python
#encoding=utf-8
#by Fooying 2013/04/18


import sys
sys.path.append('/opt/')
import redis
import pymongo
import datetime
from fooying.cnsite import config as a_config
from fooying.cnsite.public import create_task
from fooying.kslog import KSLOG

Db_mongo = pymongo.Connection(a_config.Mongo_ip, a_config.Mongo_port)
Db_rds = redis.Redis(a_config.Redis_ip)
Queue_rds = redis.Redis(a_config.Queue_redis_ip)
Log = KSLOG(a_config.Send_log_path)
Log_template = '%(messg)s'

if __name__ == '__main__':
	while True:
		try:
			task = Queue_rds.lrange(a_config.TASK_RESULT,0,1)
			if task:
				task = eval(task[0])
				try:
					db = Db_mongo.check_result
					result = {}
					result['c_result'] = task['result']
					result['c_time'] = task['c_time']
					codeurl = task['codeurl']
					eng = task['engine']
					db.result.update({'url':codeurl},{'$set':{'result.%s'%eng:result,'check_time':result['c_time']}},True)
					
				except Exception,e:
					messg = str(e)+'--'+str(task)
					Log.warning(Log_template%vars())
				else:
					Queue_rds.lpop(a_config.TASK_RESULT)
		except Exception,e:
			print e
			messg = str(e)
			Log.warning(Log_template%vars())

