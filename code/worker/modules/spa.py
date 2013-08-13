#encoding=utf-8
#by Fooying 2013/03/13

'''
http://www.spamhaus.org/query/domain/new.qq.com
匹配结果
接口：site,不能自动取
'''

import re
from fooying.http import http_request
from fooying.retools import www

def check(site):
	site = www.get_domain(site)
	html = http_request('http://www.spamhaus.org/query/domain/%s'%site)	
	regex = '''<B><FONT\scolor="green">(.*?\sis\snot\slisted\sin\sthe\sDBL)</FONT></B><br>'''
	result = re.search(regex,html)
	if result:
		check_result = 'safe'
	else:
		check_result = 'danger'
	return check_result


if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		url = sys.argv[1]
	else:
		url = 'http://news.qq.com/zt2013/xlrs/index.htm'
	print check(url)

