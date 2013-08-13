#encoding=utf-8
#by Fooying 2013/03/13

'''
https://spyeyetracker.abuse.ch/monitor.php?host=wx.qq.com
匹配结果
接口：site,不能自动取
'''

import re
from fooying.http import http_request
from fooying.retools import www

def check(site):
	site = www.get_domain(site)
	html = http_request('https://spyeyetracker.abuse.ch/monitor.php?host=%s'%site)	
	regex = '''<tr\sbgcolor="#.*?"><td>Level:</td><td>(\d)\s\(.*?\)</td></tr>'''
	level = {'1':'danger','2':'danger','5':'warning','3':'warning','4':'unknown'}
	result = re.search(regex,html)
	if result:
		msg = result.group(1)
	else:
		msg = '4'
	check_result = level.get(msg,'unknown')
	return check_result


if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		url = sys.argv[1]
	else:
		url = 'http://news.qq.com/zt2013/xlrs/index.htm'
	print check(url)

