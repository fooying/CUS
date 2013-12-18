#!/usr/bin/python
#encoding=utf-8

import redis
import time
import pymongo
from fooying.cnsite import config
from fooying.flog import FLOG

Db_mongo = pymongo.Connection(config.Mongo_ip, config.Mongo_port)
Db_rds = redis.Redis(config.Redis_ip)
Queue_rds = redis.Redis(config.Queue_redis_ip)
Log = FLOG(config.Log_path)
Log_template = '%(url)s- %(code)-%(messg)s'

def create_task(codeurl, url, force = False):
	msg ={
		0:'ok',
		1:'task repeat',
		2:'error',
		3:'create error',
		4:'push error',
	}
	now = int(time.time())
	try:
		with Db_rds.pipeline() as pipe:
			try:
				pipe.watch(config.TASK_INFO+codeurl)
				exist_job =  pipe.hgetall(config.TASK_INFO+codeurl)
				repeat_limit = config.TASK_REPEAT_LIMIT
				if not force and exist_job and int(time.time()) - int(exist_job['create_time']) < repeat_limit:
					code = 1
					messg = msg[code]
					Log.warning(Log_template%vars())
					return messg
				pipe.multi()
				pipe.hset(config.TASK_INFO+codeurl,'create_time',now)
				pipe.hset(config.TASK_INFO+codeurl,'code',0)
				pipe.hset(config.TASK_INFO+codeurl,'task_statu',0)
				pipe.execute()
			except Exception,e:
				code = 3
				messg = msg[code]
				Log.warning(Log_template%vars()+str(e))
				return messg
			finally:
				pipe.reset()
		task = {
			'url':url,
			'codeurl':codeurl,
			'create_time':now
		}
		if not Queue_rds.rpush(config.TASK_LIST, task):
			code = 4
			messg = msg[code]
			Log.warning(Log_template%vars())
			return messg
		db = Db_mongo.check_result
		db.result.delete({'url':codeurl})
		Db_rds.incr(config.TASK_COUNT,1)
		code = 0
		messg = msg[code]
		return messg
	except Exception,e:
		code = 2
		messg = msg[code]
		Log.warning(Log_template%vars()+str(e))
		return messg

