#encoding=utf-8
#by Fooying 2013/03/13

'''
公共调用模块
'''
import requests
import sys
import socket
reload(sys)
sys.setdefaultencoding('utf-8')
socket.setdefaulttimeout(10)

def http_request(url, proxy=False): 
	'''
	获取网页源码
	'''
	proxies = {
		'http':'http://0.0.0.0:8087',
		}
	if proxy:
		req = requests.get(url, proxies=proxies)
	else:
		req = requests.get(url)
	html = req.content
	return html

