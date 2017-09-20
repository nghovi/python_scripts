#!/bin/bash

if test "$1" = ""
then
	echo 'Please enter file path'
	exit 0
fi

echo "Using $0 for checking $1"
if [ -s $1 ]; then
	echo "$1 is non empty file"
fi

if [ -f $1 ];
then
	echo "$1 is a file"
else
    if test -d $1
    then
        echo "$1 is a directory"
    fi
fi

if [ -r $1 ]
then
    echo "$1 is readable"
fi

if test -w $1
then
    echo "$1 is writable"
fi

if [ -x $1 ]
then
    echo "$1 is executable"
fi

if test -w $1 -o -r $1
then
    echo "$1 is readable. It's writable as well"
fi