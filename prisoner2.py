#!/usr/bin/python
#
#  this is the algorithm that prisoner 2 uses to read the board to determine where the key is
#
#  run with argument -x for an explaination

import sys

explain=False
if len(sys.argv) > 1:
  myarg=sys.argv[1]
  if myarg=='-x':
    explain = True


grid=[]
# read in gameboard
for line in sys.stdin:
    for i in line.rstrip().split() :
      grid.append(int(i))


def printboard():
  print "The board:"
  for i in range(0,64):
    print grid[i], 
    if (i%8 == 7):
      print ""


def printboard_group(bit):
  print "group with bit:", bit
  grp_sum=0
  for i in range(0,64):
    if i & bit :
      print grid[i], 
      grp_sum+=grid[i]
    else:
      print "_", 
    if (i%8 == 7):
      print ""
  print "     group sum:", grp_sum, " parity:", grp_sum % 2
  print ""


def boardparity():

   # check parity of sets of numbers that have the ones bit set, twos bit, 4s bit, 8s bit, ..
   # the number we want is in the sets that have odd parity
   
   target=0
   for j in (1, 2, 4, 8, 16, 32):
     if explain:
       printboard_group(j)
     x=0
     for i in range(0,64):
       if i & j:
         x += grid[i]
     if (x%2 == 1):
       target+=j

   return target


#
###
#

print ""
printboard()
print ""

target = boardparity()

sys.stderr.write("PRISONER 2 sees that the board points to location " + str(target) + "\n\n")



