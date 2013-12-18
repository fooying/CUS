#encoding=utf-8

Mongo_ip = '127.0.0.1'
Mongo_port = 27017

Redis_ip = '127.0.0.1'
Queue_redis_ip = '127.0.0.1'

Log_path = '/data/log/cnsite/task.log'
Send_log_path = '/data/log/cnsite/send.log'
Safe_type = {
	'safe':'安全',
	'danger':'危险',
	'warning':'警告',
	'unknown':'未知',
	'error':'未知',
	'ing':'检测中',
}

TASK_REPEAT_LIMIT = 60*60*24
TASK_INFO = 'task.info.'
TASK_LIST = 'task.list'
TASK_COUNT = 'task.count'
TASK_ENGINE = 'task.engine.'
TASK_RESULT = 'task.result'

Engine_num = 12
Engine_old_num = 0

Engines = {
	'fse':'F-Secure Browsing Protection',
	'gsb':'谷歌安全浏览',
	'hfn':'hpHosts',
	'jsd':'金山下载网址检测',
	'jsu':'金山钓鱼网址检测',
	'mcf':'McAfee SiteAdvisor',
	'ntn':'诺顿网页安全',
	'rix':'瑞星卡卡网站吧',
	'spa':'The Spamhaus Project',
	'spt':'SpyEye Tracker',
	'wsg':'Web Security Guard',
	'zeu':'ZeuS Tracker',
}



