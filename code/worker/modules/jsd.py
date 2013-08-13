#encoding=utf-8
#by Fooying 2013/03/13

'''
金山下载url查询
匹配结果
'''

import re
import base64
import time
import hashlib
import json
from fooying.http import http_request

def check(site):
	secret='a176201e188a0969cd7b7fa2ef3c8d14'
	appkey='k-33356'
	now = time.time()
	safeurl = base64.b64encode(site)
	safeurl = safeurl.replace('+','-')
	safeurl = safeurl.replace('/','_')
	signature_base_string="/download/?appkey=k-33356&q="+safeurl+"&timestamp="+str(now)
	sign = signature_base_string+secret
	sign = hashlib.md5(sign).hexdigest().upper()
	url="http://open.pc120.com/download/?q="+safeurl+"&appkey=k-33356&timestamp="+str(now)+"&sign="+sign
	html = http_request(url)	
	dtype = json.loads(html).get('down_type',1)
	level = {1:'unknown',2:'safe',3:'danger',6:'unknown'}
	check_result = level.get(dtype,'unknown')
	return check_result


if __name__ == '__main__':
	print check('www.qq.com')
