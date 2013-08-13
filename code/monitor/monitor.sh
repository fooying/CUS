#!/bin/sh

ps -ef | grep "python send.py" | grep -qv grep
if [ $? -ne 0 ]; then
    python send.py &
fi

ps -ef | grep "python recive.py" | grep -qv grep
if [ $? -ne 0 ]; then
    python recive.py &
fi

