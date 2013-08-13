#coding=utf-8
'''
路由模块，这是只是把路由地址分出来
'''
urls = (
    '/', 'views.index',
    '/report/(.*)', 'views.report',
    )

