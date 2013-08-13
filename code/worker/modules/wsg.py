#encoding=utf-8
#by Fooying 2013/03/13

'''
http://www.websecurityguard.com/detail.aspx?domain=qq.com
匹配结果
接口不分url或site,自动转site
'''

import re
from fooying.http import http_request
from fooying.retools import www
def check(site):
	site = www.get_domain(site)
	html = http_request('http://www.websecurityguard.com/detail.aspx?domain=%s'%site)	
	regex = '''<div\sid="website-head"\sclass="class-([a-z]*?)">'''
	level = {'red':'danger','green':'safe','grey':'unknown','orange':'warning'}
	result = re.search(regex,html)
	if result:
		color = result.group(1)
	else:
		color = 'grey'
		
	check_result = level.get(color,'unknown')
	return check_result


if __name__ == '__main__':
	print check('www.qq.com')
