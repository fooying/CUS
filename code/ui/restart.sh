export PYTHONPATH=/opt
ps -ef|grep 'uwsgi -s :6000'|grep -v grep |awk '{print $2} '|xargs kill -9
uwsgi -s :6000 -w index -p 2 -d /mnt/log/www/uwsgi_cnsite.log -M -p 4  -t 30  -R 10000 
