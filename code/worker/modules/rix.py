#encoding=utf-8
#by Fooying 2013/03/13

'''
http://site.ikaka.com/Index/domaininfo/www.qqtz.com
匹配结果
接口：site,不能自动取
'''

import re
from fooying.http import http_request
from fooying.retools import www

def check(site):
	site = www.get_domain(site)
	html = http_request('http://site.ikaka.com/Index/domaininfo/%s'%site)	
	regex = '''<h1\sid="domaintd"\sclass="state-title">(.*?)</h1>'''
	level = {'不安全，该网站存在恶意行为，不建议进行访问。':'danger','安全，未在该网站发现重大的安全问题。':'safe','未知，还未对此网站进行检测，欢迎发表你的看法。':'unknown'}
	result = re.search(regex,html)
	if result:
		msg = result.group(1)
	else:
		msg = '未知，还未对此网站进行检测，欢迎发表你的看法。'
	check_result = level.get(msg,'unknown')
	return check_result


if __name__ == '__main__':
	print check('http://www.qqtz.com/1')

