#!/bin/bash
#by Fooying

start () {
    python start.py
    echo "start ok"
}

stop () {
    ps -aux|grep 'python worker.py'|grep -v grep |awk '{print $2} '|xargs kill -9
    echo "stop ok"
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        start
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}" >&2
        ;;
esac
