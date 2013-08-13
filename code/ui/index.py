#coding=utf-8
'''
api主调用模块
'''
import web
import views
from url import urls
from lib.auto import notfound,unloadhook,loadhook

web.config.debug = False
app = web.application(urls, locals())

#app.notfound = notfound
#app.add_processor(web.loadhook(loadhook))
#app.add_processor(web.unloadhook(unloadhook))

if __name__ == "__main__":
	app.run()
else:
	application = app.wsgifunc()
