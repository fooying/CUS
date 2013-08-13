#encoding=utf-8
#by Fooying 2013/03/13

'''
http://hosts-file.net/?s=http://www.qq.com/111
匹配结果
接口：site,自动取
'''

import re
from fooying.http import http_request
from fooying.retools import www

def check(site):
	site = www.get_domain(site)
	html = http_request('http://hosts-file.net/?s=%s'%site)	
	regex = '''<td\sclass="main_normal"\salign="left"\scolspan="1"\sstyle="[^>]*?">.*?\s*?([^\n]*?)\s\(<a\sclass="main\_normal\_noborder"'''
	result = re.search(regex,html,re.S)
	level = {'Not Specified':'unknown','TBV':'unknown','ATS':'safe','GRM':'warning','HFS':'warning',
		'MMT':'danger','WRZ':'danger','PSH':'danger','HJK':'danger','FSA':'danger',
		'EMD':'danger','EXP':'danger'}
	if result:
		msg = result.group(1).strip()
	else:
		msg = 'Not Specified'
	check_result = level.get(msg,'unknown')
	return check_result


if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		url = sys.argv[1]
	else:
		url = 'http://news.qq.com/zt2013/xlrs/index.htm'
	print check(url)

