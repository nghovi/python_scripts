#!/bin/bash
if [ $# -ne 2 ]
then
   echo "Error : Number are not supplied" 1>&2
   echo "Usage : $0 number1 number2" 1>&2
   exit 1
fi
ans=`expr $1 + $2`
echo "Sum is $ans"
