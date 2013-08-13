#!/usr/bin/python
#encoding=utf-8
#by Fooying

import re
import web

def unloadhook():
	pass

def loadhook():
	params = web.input()
	for key,value in params.items():
		if not is_url_format(value):
			raise web.redirect('/')
		

def notfound():
	raise web.redirect('/')	

	

def is_url_format(url_str):
	is_url_format_reg = """
		 ^ #必须是串开始
        (?:http(?:s)?://)? #protocol
        (?:[\w]+(?::[\w]+)?@)? #user@password
        ([-\w]+\.)+[\w-]+(?:.)? #domain
        (?::\d{2,5})? #port
        (/?[-:\w;\./?%&=#]*)? #params
         $
		"""
	is_url_format_re_obj = re.compile(is_url_format_reg,re.X|re.I)
	if is_url_format_re_obj.search(url_str):
		domain = get_domain(url_str)
		if not domain:
			return False
		if is_domain_format(domain) or is_ip_format(re.sub(':\d+','',domain)):
			return True
		else:
			return False
	else:
		return False

def get_domain(url):
	if not url.startswith(('http://','https://')):
		url = 'http://' + url
	url = url.lower()
	head_pos = url.find('//')
	if head_pos != -1:
		url = url[head_pos+2:]
	end_pos = url.find('/')
	if end_pos != -1:
		url = url[:end_pos]
	else:
		end_pos = url.find('?')
		if end_pos != -1:
			url = url[:end_pos]
		else:
			end_pos = url.find('#')
			if end_pos != -1:
				url = url[:end_pos]
	domain = url
	return domain

def is_domain_format(domain):
	is_domain_format_reg = """^(?:https?://)?(?:[A-Za-z0-9\u4E00-\u9FA5-][A-Za-z0-9\u4E00-\u9FA5-]{0,62}\.){1,20}
		(?:(?:aero)|(?:asia)|(?:biz)|(?:cat)|(?:com)|(?:coop)|(?:info)|(?:int)|(?:jobs)|(?:mobi)|(?:museum)|
		(?:name)|(?:net)|(?:org)|(?:pro)|(?:tel)|(?:travel)|(?:xxx)|(?:edu)|(?:gov)|(?:mil)|(?:ac)|(?:ad)|
		(?:ae)|(?:af)|(?:ag)|(?:ai)|(?:al)|(?:am)|(?:an)|(?:ao)|(?:aq)|(?:ar)|(?:as)|(?:at)|(?:au)|(?:aw)|
		(?:ax)|(?:az)|(?:ba)|(?:bb)|(?:bd)|(?:be)|(?:bf)|(?:bg)|(?:bh)|(?:bi)|(?:bj)|(?:bm)|(?:bn)|(?:bo)|
		(?:br)|(?:bs)|(?:bt)|(?:bv)|(?:bw)|(?:by)|(?:bz)|(?:ca)|(?:cc)|(?:cd)|(?:cf)|(?:cg)|(?:ch)|(?:ci)|
		(?:ck)|(?:cl)|(?:cm)|(?:cn)|(?:co)|(?:cr)|(?:cs)|(?:cu)|(?:cv)|(?:cx)|(?:cy)|(?:cz)|(?:dd)|(?:de)|
		(?:dj)|(?:dk)|(?:dm)|(?:do)|(?:dz)|(?:ec)|(?:ee)|(?:eg)|(?:eh)|(?:er)|(?:es)|(?:et)|(?:eu)|(?:fi)|
		(?:fj)|(?:fk)|(?:fm)|(?:fo)|(?:fr)|(?:ga)|(?:gb)|(?:gd)|(?:ge)|(?:gf)|(?:gg)|(?:gh)|(?:gi)|(?:gl)|
		(?:gm)|(?:gn)|(?:gp)|(?:gq)|(?:gr)|(?:gs)|(?:gt)|(?:gu)|(?:gw)|(?:gy)|(?:hk)|(?:hm)|(?:hn)|(?:hr)|
		(?:ht)|(?:hu)|(?:id)|(?:ie)|(?:il)|(?:im)|(?:in)|(?:io)|(?:iq)|(?:ir)|(?:is)|(?:it)|(?:je)|(?:jm)|
		(?:jo)|(?:jp)|(?:ke)|(?:kg)|(?:kh)|(?:ki)|(?:km)|(?:kn)|(?:kp)|(?:kr)|(?:kw)|(?:ky)|(?:kz)|(?:la)|
		(?:lb)|(?:lc)|(?:li)|(?:lk)|(?:lr)|(?:ls)|(?:lt)|(?:lu)|(?:lv)|(?:ly)|(?:ma)|(?:mc)|(?:md)|(?:me)|
		(?:mg)|(?:mh)|(?:mk)|(?:ml)|(?:mm)|(?:mn)|(?:mo)|(?:mp)|(?:mq)|(?:mr)|(?:ms)|(?:mt)|(?:mu)|(?:mv)|
		(?:mw)|(?:mx)|(?:my)|(?:mz)|(?:na)|(?:nc)|(?:ne)|(?:nf)|(?:ng)|(?:ni)|(?:nl)|(?:no)|(?:np)|(?:nr)|
		(?:nu)|(?:nz)|(?:om)|(?:pa)|(?:pe)|(?:pf)|(?:pg)|(?:ph)|(?:pk)|(?:pl)|(?:pm)|(?:pn)|(?:pr)|(?:ps)|
		(?:pt)|(?:pw)|(?:py)|(?:qa)|(?:re)|(?:ro)|(?:rs)|(?:ru)|(?:rw)|(?:sa)|(?:sb)|(?:sc)|(?:sd)|(?:se)|
		(?:sg)|(?:sh)|(?:si)|(?:sj)|(?:sk)|(?:sl)|(?:sm)|(?:sn)|(?:so)|(?:sr)|(?:ss)|(?:st)|(?:su)|(?:sv)|
		(?:sy)|(?:sz)|(?:tc)|(?:td)|(?:tf)|(?:tg)|(?:th)|(?:tj)|(?:tk)|(?:tl)|(?:tm)|(?:tn)|(?:to)|(?:tp)|
		(?:tr)|(?:tt)|(?:tv)|(?:tw)|(?:tz)|(?:ua)|(?:ug)|(?:uk)|(?:us)|(?:uy)|(?:uz)|(?:va)|(?:vc)|(?:ve)|
		(?:vg)|(?:vi)|(?:vn)|(?:vu)|(?:wf)|(?:ws)|(?:ye)|(?:yt)|(?:yu)|(?:za)|(?:zm)|(?:zw)|(?:arpa)|
		(?:gov\.cn)|(?:com\.cn)|(?:net\.cn)|(?:org\.cn)|(?:com\.tw)|(?:com\.hk)|(?:me\.uk)|(?:org\.uk)|
		(?:ltd\.uk)|(?:plc\.uk)|(?:com\.co)|(?:net\.co)|(?:nom\.co)|(?:com\.ag)|(?:net\.ag)|(?:org\.ag)|
		(?:com\.bz)|(?:net\.bz)|(?:net\.br)|(?:com\.br)|(?:com\.es)|(?:nom\.es)|(?:org\.es)|(?:co\.in)|
		(?:firm\.in)|(?:gen\.in)|(?:ind\.in)|(?:net\.in)|(?:org\.in)|(?:com\.mx)|(?:co\.nz)|(?:net\.nz)|
		(?:org\.nz)|(?:org\.tw)|(?:idv\.tw)|(?:co\.uk)|(?:co.jp)|(?:com.au)|(?:co.za)|(?:com.ar)|(?:co.kr)|
		(?:com.ua)|(?:co.il)|(?:com.tr)|(?:com.pl)|(?:or.jp)|(?:co.id)|(?:org.br)|(?:ne.jp)|(?:co.cc)|
		(?:ac.jp)|(?:com.ve)|(?:ac.in)|(?:com.my)|(?:gov.in)|(?:org.ua)|(?:com.vn)|(?:co.th)|(?:com.sg)|
		(?:spb.ru)|(?:nic.in)|(?:kiev.ua)|(?:gov.uk)|(?:ac.ir)|(?:gen.tr)|(?:com.pe)|(?:or.kr)|(?:com.pk)|
		(?:com.de)|(?:at.tc)|(?:it.tc)|(?:com.nu)|(?:cn.ms)|(?:edu.cn)|(?:hk.tc)|(?:ok.to)|(?:net.tc)|
		(?:net.tf)|(?:at.hm))(?:\.)?(?::[\d]{1,5})?$"""
	is_domain_format_re_obj = re.compile(is_domain_format_reg,re.M|re.I|re.X)
	if is_domain_format_re_obj.search(domain):
		return True
	else:
		return False
