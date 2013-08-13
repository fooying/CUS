#encoding=utf-8
#by Fooying 2013/03/13

'''
http://www.siteadvisor.com/sites/xssing.org
匹配结果
接口：自动取domain
'''

import re
from fooying.http import http_request
from fooying.retools import www

def check(site):
	site = www.get_domain(site)
	html = http_request('http://www.siteadvisor.com/sites/%s'%site)	
	regex = '''<img\ssrc="/images/.*?\.gif"\salt="([a-zA-Z]*?)\sVerdict\sImage"\sborder="0"\s/>'''
	level = {'Red':'danger','Green':'safe','Grey':'unknown','Yellow':'warning'}
	result = re.search(regex,html)
	if result:
		color = result.group(1)
	else:
		color = 'Grey'
	check_result = level.get(color,'unknown')
	return check_result


if __name__ == '__main__':
	print check('www.qq.com')
