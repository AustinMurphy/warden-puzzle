#!/usr/bin/python

import sys

explain=False
if len(sys.argv) > 1:
  myarg=sys.argv[1]
  if myarg=='-x':
    explain = True


# [0] -- [63] are the coins, [64] is the location with the key
grid=[]

for line in sys.stdin:
    for i in line.rstrip().split() :
      grid.append(int(i))


def printboard():
  for i in range(0,64):
    print grid[i], 
    if (i%8 == 7):
      print ""

def printboard_err():
  for i in range(0,64):
    sys.stderr.write(str(grid[i]) + " ")
    if (i%8 == 7):
      sys.stderr.write("\n")
  sys.stderr.write("\n")


def numin6bits(num):
  # 6 bits  
  bits=""
  for b in (32, 16, 8, 4, 2, 1):
    if num & b:
      bits+="1 "
    else:
      bits+="0 "
  return bits


def boardparity():

   # check parity of set of numbers that have the ones bit set, twos bit, 4s bit, 8s bit, ..
   # the number we want is in the sets that have odd parity
   
   target=0
   for j in (1, 2, 4, 8, 16, 32):
     x=0
     for i in range(0,64):
       if i & j:
         x += grid[i]
     if (x%2 == 1):
       target+=j

   return target




keyloc=grid[64]

target = boardparity()


printboard_err()
sys.stderr.write("\n")
sys.stderr.write("PRISONER 1 sees that the board points to location " + str(target) + "\n")


# bitwise XOR of the board's current target and what we want the target to be
fliploc = keyloc ^ target

if explain:
  tgtbits = numin6bits(target)
  keybits = numin6bits(keyloc)
  flipbits = numin6bits(fliploc)

  sys.stderr.write("\n")
  sys.stderr.write( tgtbits + " == " + str(target) + " The current target \n")
  sys.stderr.write( keybits + " == " + str(keyloc) + " The desired target \n")
  sys.stderr.write( flipbits + " == " + str(fliploc) + " The difference  (bitwise XOR) \n")
  sys.stderr.write("\n")


sys.stderr.write("PRISONER 1 FLIPS location " + str(fliploc) + "\n")
sys.stderr.write("\n")
if grid[fliploc] == 0:
  grid[fliploc] = 1
else:
  grid[fliploc] = 0
 

printboard()


