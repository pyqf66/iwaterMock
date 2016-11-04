#!/bin/bash
set -e
HOST="127.0.0.1"
#HOST=$1
#SERVICENAME=$2
#LINENUM=$3
LINENUM=$1
LOGFILE="/usr/local/nginx/html/statics/logs/all.log"
#LOGFILE="/Users/zhangyufeng/Documents/iwater_Documents/QualityAssuranse/iwaterMock/statics/logs/all.log"
if [ $LINENUM ];then
    #ssh -A -T root@$HOST "sed -n ${LINENUM}p $LOGFILE"
    sed -n ${LINENUM}p $LOGFILE
else
    #ssh -A -T root@$HOST "wc -l $LOGFILE|awk '{print \$1}'"
    wc -l $LOGFILE|awk '{print "'$HOST'"}'
fi
