#! /bin/bash

# requirements: backup tool
# in command line arguments: a path will be provided to copy backup files from in the first argument ($1)

# expected output: create another dir with same name but _BACKUP and all files are copied but added with extension .bak


# example command: 

#  ./backup.sh ~/imt-linux

# output:

#  imt-linux_BACKUP / file1.txt.bak 

file_list=$(ls $1)

if [ -a $1_BACKUP ]; then

echo "directory exists"

else

mkdir $1_BACKUP

for f in $file_list
do 

cp $1/$f  $1_BACKUP/$f.bak

done

fi

