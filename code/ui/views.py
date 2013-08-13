#!/usr/bin/python
#encoding=utf-8

import web
import sys
import pymongo
import urllib
import datetime
import time
import redis
from fooying.cnsite import config
from fooying.cnsite.public import create_task
from fooying.retools import www
from fooying.kslog import KSLOG
reload(sys)
sys.setdefaultencoding('utf-8')

Db_mongo = pymongo.Connection(config.Mongo_ip, config.Mongo_port)
Db_rds = redis.Redis(config.Redis_ip)
Queue_rds = redis.Redis(config.Queue_redis_ip)
Log = KSLOG(config.Log_path)
Log_template = '%(url)s- %(code)-%(messg)s'

render = web.template.render('templates/', cache=False)


class index:
	def run(self):
		return render.index()	

	def GET(self):
		return self.run()

	def POST(self):
		return self.run()

class report:
	def run(self, codeurl, newtask = False):
		#import pdb;pdb.set_trace()
		url = urllib.unquote(codeurl)
		if url.startswith('https:/'):
			url = url[7:len(url)]
		if url.startswith('http:/'):
			url = url[6:len(url)]
		codeurl = urllib.quote(url)
		if newtask and www.is_url_format(url):#判断是否重新检测
			stu = create_task(codeurl,url)
			return stu 
		else:
			recheck = '0'
			if not www.is_url_format(url):
				raise web.redirect('/')
			result_count = {'safe':0,'warning':0,'danger':0,'unknown':0}
			exist_job =  Db_rds.hgetall(config.TASK_INFO+codeurl) #判断是否旧版本数据,如果是，加入调度
			print exist_job
			if not exist_job or (exist_job.get('code',config.Engine_old_num) == config.Engine_old_num and exist_job.get('task_statu',1) ==1):
				create_task(codeurl,url,True)
				status = 'ing'
				url_result = {}
			else:
				recheck = '1'
				db = Db_mongo.check_result
				url_result = db.result.find_one({'url':codeurl})
				status = 'done'
				if not url_result:
					status = 'ing'
					url_result = {}
					create_task(codeurl,url,False)
				elif len(url_result.get('result',{}))< config.Engine_num:
					status = 'ing'
				if exist_job and exist_job.get('task_statu',1) == '0':
					status = 'ing'
				if url_result:
					result = url_result.get('result',{})
					for i in result:
						e_result = result.get(i,{})
						r = e_result.get('c_result','')
						if r == 'safe':
							result_count['safe'] += 1
						elif r == 'warning':
							result_count['warning'] += 1
						elif r == 'danger':
							result_count['danger'] += 1
						else:
							result_count['unknown'] += 1
					checktime = result.get('check_time','')
					if checktime:
						howlong = time.teime -  time.mktime(checktime.timetuple())
						if howlong < config.TASK_REPEAT_LIMIT:
							recheck = '0'
			now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			return render.report(url,url_result,config.Engines,config.Safe_type,config.Engine_num,status,now,result_count,recheck)

	def GET(self, codeurl):
		return self.run(codeurl)

	def POST(self, codeurl):
		newtask = web.input().get('newtask','')
		return self.run(codeurl, newtask)


