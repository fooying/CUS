#encoding=utf-8
#by Fooying 2013/03/13

'''
https://safeweb.norton.com/report/show?url=http://www.qq.com/2
匹配结果
接口：domain,自动取
'''

import re
from fooying.http import http_request

def check(site):
	html = http_request('https://safeweb.norton.com/report/show?url=%s'%site)	
	regex = '''<div\sclass="ratingIcon\sico(.*?)">'''
	level = {'Caution':'danger','Safe':'safe','NSecured':'safe','Untested':'unknown','Warning':'warning'}
	result = re.search(regex,html)
	if result:
		msg = result.group(1)
	else:
		msg = 'Untested'
	check_result = level.get(msg,'unknown')
	return check_result


if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		url = sys.argv[1]
	else:
		url = 'http://news.qq.com/zt2013/xlrs/index.htm'
	print check(url)

