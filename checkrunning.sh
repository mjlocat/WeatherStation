#!/bin/bash

WSPID=`ps x | grep weatherstation | grep -v grep | awk '{ print $1 }'`
DBPID=`ps x | grep writetodb.py | grep -v grep | awk '{ print $1 }'`

if [ -z "${WSPID}" -o -z "${DBPID}" ]; then
  if [ ! -z "${WSPID}"]; then
    kill ${WSPID} 2>/dev/null
  fi
  if [ ! -z "${DBPID}" ]; then
    kill ${DBPID} 2>/dev/null
  fi
  ./weatherstation 2>/dev/null | python3 writetodb.py &
fi
