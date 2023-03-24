#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
cd "$parent_path"


printlogfile="logs/xcheduler.log"

nohup ../backend-env/bin/python3 xcheduler.py $printlogfile 2>>$printlogfile &


echo "stdout is at $printlogfile"
