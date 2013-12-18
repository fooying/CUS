#encoding=utf-8
#by Fooying 2013/03/13

'''
http://browsingprotection.f-secure.com/swp/result?idc_hf_0=&url=qq.com&sa=&boxstate=1
匹配结果
接口：url
'''

import re
from fooying.http import http_request

def check(site):
	html = http_request('http://browsingprotection.f-secure.com/swp/result?idc_hf_0=&url=%s&sa=&boxstate=1'%site)	
	regex = '''<td\sid="url_rating_status"\sstyle="font-size:20px;line-height:1.5em">This\ssite\sis:\s<font.*?color=#417317><b>(.*?)</b></font></td>'''
	level = {'Harmful':'danger','Safe':'safe','Unknown':'unknown'}
	result = re.search(regex,html,re.S)
	if result:
		msg = result.group(1)
	else:
		msg = 'Unknown'
	check_result = level.get(msg,'unknown')
	return check_result


if __name__ == '__main__':
	print check('http://www.qq.com/1')

