#! /bin/bash

function print_usage()
{
	echo " Usage:"
	echo " use -v to view phonebook entries"
	echo " use -i to insert an new entry, give it a name and a number"
	echo " use -e to erase whole phonebook"
	echo " use -d to delete one entry, give it a name and a number"
	echo " use -s to search for an entry by name"
	echo
}


# if no command line arguments were given -> usage message should be printed

if [ -a $1 ]; then

print_usage


else

case $1 in


# to view file we need to read the file and print it
"-v") records=($(cat phonebook.txt | cut -d "," -f 1-2 --output-delimiter=":"))
	  
	  for r in ${records[@]} 
	  do 
	  echo "$r" 
	  done
	;;
	
# name=Mazen number=1234567
"-i") 

	if [ -a $2 ]; then
	
	print_usage
	exit -1
	else
	
		if [ -a $3 ]; then
			
			print_usage
			exit -1
		
		fi
	
	echo $2,$3 >> phonebook.txt
	echo "record inserted successfully... "
	
	fi

	;;


*)
print_usage
;;

esac

fi





