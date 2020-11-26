#!/bin/bash
# 
#  print out a random board for the puzzle
#   no labels 
#   0 means coin is heads up in that location
#   1 means coin is tails up in that location

# a random location, where the key is hidden
k=$(((RANDOM%64)))

echoerr() { echo "$@" 1>&2; }

echoerr "WARDEN PRESENTS THE FOLLOWING GAME BOARD"
echoerr "  AND HAS HIDDEN THE KEY UNDER LOCATION  $k"
echoerr "  "


# a randomly generated board
for j in $(seq 0 7) 
do 
  line=""
  for i in $(seq 0 7) 
  do 
    line="$line $(((RANDOM%2)))" 
  done 
  echo "$line"
done 

# the key location
echo "$k "

