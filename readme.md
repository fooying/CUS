本系统采用uwsgi+nginx+web.py+python+mongo
开发
系统运行环境需要：

apt-get install web.py

apt-get install python=2.7.3

apt-get install nginx

apt-get install uwsgi

apt-get install mongodb



cnsite.conf 为nginx配置文件，根据具体情况进行相应修改

mongo数据库为check_result，表result



fooying目录为公共引用目录，需要加入path环境(ui/monitor/worker机器都需要)



运行系统：

ui：
	
    安装好相关环境后，配置好nginx的设置，进入ui目录，运行restart.sh即可

    ./restart.sh(需要执行权限)


worker：
	
    可以在多台服务器上配置worker

    根据具体的资源情况，修改config.py配置文件，修改队列服务器及存储服务器地址以，然后运行ctrl.sh即可

    ./ctrl (start/stop开始或者停止，需要执行权限)


monitor：
	
    以一台机器作为调度机
	
    配置好相关配置
	
    运行monitor.sh即可
	
    ./monitor.sh(需要执行权限)
	


可以通过ps -aux|grep worker/recive/sed等进行查看是否启动成功


添加新引擎需要在需要添加的引擎机器的woker目录下的modules目录下添加，可参考其他引擎
并且修改配置文件


新站点检测需要刷新显示检测结果，未做自动刷新处理

demo:
http://www.cnsite.so/
	
