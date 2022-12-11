#! /bin/bash


# fake recyclebin

# requirements: create fake recycle bin folder
# will contain hardlinks for files that once existed in other locations

# Questions:
# 1. how to restore recycled files ?
# 2. how to reduce file size in recycle bin ?

RECYCLE_BIN_PATH=/home/mof/FakeRecycleBin

# steps: 

# 1. create the hard link in the fake recycle bin
ln $1 $RECYCLE_BIN_PATH


# 2. rm the file from original location
rm $1



