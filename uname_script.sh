#! /bin/bash


options=( "s" "n" "r" "v" "m" "p" "i" "o" )
#options="snrvmpio"



for c in ${options[@]}
do

echo -e "\t" $(uname -$c)

done
