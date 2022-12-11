#! /bin/bash

my_global_var=10


printHello ()
{

my_global_var=20

local my_local_var=50
echo $my_local_var


echo "Hello  $1 !!"

}

modify_local()
{
 my_local_var=60
}


# commnd line arguments
# echo $0 $1 $2 $3 $4

#for a in $@
#do

# echo $a

#done

modify_local
printHello "Mazen" "Osama"
echo $my_global_var
echo $my_local_var


# arrays

arr1=(10 "twenty" 30 "forty four" 50 "sixty")
arr_chars=('a' 'b' 'c' 'd')

for i in ${arr1[@]}
do

echo $i

done

# variables

var1=11

# echo "$var1"
#read -p "enter a value" var1


if [ $var1 -eq 10 ]; then

echo "var1 is $var1"


elif [ $var1 -lt 10 ]; then

echo "$var1 < 10 "

else

echo "var1 is not 10"


fi

numbers=$(python3 -c "import random
for _ in range(10): print(int(random.random()*10), end=' ')
print()")

#i=0
#while [ $i -lt 10 ] 
#do
	#echo ${numbers[$i]}
#i=$[$i+1]
#done

#for n in $numbers
#do

#echo $n

#done
