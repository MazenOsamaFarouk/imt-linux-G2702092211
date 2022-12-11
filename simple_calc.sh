#! /bin/bash


# requirements: simple calulator using only two operands
# and one operator for the following {+-*/}




read -p "Enter first value " val1
read -p "Enter second value " val2
read -p "Enter operation(+-/x) " op

case $op in

+)

	echo "$val1+$val2=$[$val1+$val2]"
	;;
	

-)

	echo "$val1-$val2=$[$val1-$val2]"
	;;
	
x)

	echo "$val1 x $val2=$[$val1*$val2]"
	;;
	
"/")

	echo "$val1/$val2=$[$val1/$val2]"
	;;

*)
	echo "wrong operation"
	;;

esac

