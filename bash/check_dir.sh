#!/bin/bash

dir=`pwd`

#Test comment, $?
echo
if [ $? -eq 0 ]
then
    echo "Command pwd is successfully executed!"
fi

if test "$1" != ""
then
	dir=$1
fi
echo
echo "dir=$dir"
echo
file_list=`ls -1 $dir`

echo "========================= Example 1 ====================================="
for i in $file_list
do
    echo "File: $i"
done
echo "========================= Example 1 for i in do done ===================="
for i in  in 1 2 3 4 5 6
do
    echo "Square of $i is `expr $i \* $i`"
done
echo "========================= Example 3: Chessboard ========================="
for ((i=1; i<=9; i++))
do
    for ((j=1; j<=9; j++))
    do
        #echo "i+j=`expr $i \+ $j`"
        tot=`expr $i + $j`
        tmp=`expr $tot % 2`
        if [ $tmp -eq 0 ]; then
            echo -e -n "\033[47m "
        else
            echo -e -n "\033[40m "
        fi
    done
    echo -e -n "\033[40m" #### set back background colour to black
    echo "" #### print the new line ###
done
echo "========================= Example 4: while [  ] do done ================"
j=1
while test $j -lt 10
do
    echo "j=$j"
    j=`expr $j + 1`
done

echo
echo "exit 0 is successfully exit :o"
exit 0