#!/bin/bash
echo "Today is \033[34m `date`"
echo "Script name is $0"
echo "Number of arguments: $#"
echo "Argument 1 is $1"
echo "Argument 2 is $2"
echo "All arguments are $@"
echo "Or all arguments are $*"
if [ $1 > 0 ]
then
    echo "First argument is greater than zero"
else
    echo "First argument is not greater than zero"
fi
if [ $2 -ge 0 ]
then
    echo "Second argument is zero"
fi

if test $# -eq 0
then
    echo "None argument given"
elif [ $# -gt 0 ]; then
    echo "More than zero arguments given"
fi
#statements]
x=10
name=viet
email=nguyen.viet@dena.jp
echo $x
echo "name: $name"
echo "email: $email"
echo 6 + 3
expr 6 + 3
echo `expr 7 / 3`

