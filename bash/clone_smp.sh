#!/bin/bash

if [ "$1" = "" -o "$2" = "" ]
then
    echo "Usage: $0 event_code_id release_date"
    echo "Example: $0 44 20150109"
    exit 0
fi

check=$(( $1 % 2 ))
if test $check -eq 1
then
    echo "event_code_id for raid must be even"
    exit 0
fi

p1=`expr $1 - 2`
p2=`expr $1 - 4`

pprev="0$p2"
prev="0$p1"
next="0$1"
release_date=$2

echo " $pprev  $prev  $next $release_date"
