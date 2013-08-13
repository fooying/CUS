#encoding=utf-8
#by Fooying 2013/03/13

'''
https://www.google.com/safebrowsing/diagnostic?site=qq.com
匹配结果
接口：site,自动取
'''

import re
from fooying.http import http_request
from fooying.retools import www

def check(site):
	html = http_request('https://www.google.com/safebrowsing/diagnostic?site=%s'%site)	
	regex = '''<blockquote><p>(.*?)</p>'''
	level = {'Site is listed as suspicious - visiting this web site may harm your computer.':'danger','This site is not currently listed as suspicious.':'safe','unknown':'unknown'}
	result = re.search(regex,html)
	if result:
		msg = result.group(1)
	else:
		msg = 'unknown'
	check_result = level.get(msg,'unknown')
	return check_result


if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		url = sys.argv[1]
	else:
		url = 'http://news.qq.com/zt2013/xlrs/index.htm'
	print check(url)

