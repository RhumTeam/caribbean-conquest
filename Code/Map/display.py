# -*- coding: utf-8 -*-

#coding rules
import sys

char_display=['\033[96m█','\033[93m█', '\033[37mX']
#char_display=['\033[96m.','\033[93mo', '\033[37mX']


"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    
ESC [ 0 m       # reset all (colors and brightness)
ESC [ 1 m       # bright
ESC [ 2 m       # dim (looks same as normal brightness)
ESC [ 22 m      # normal brightness

# FOREGROUND:
ESC [ 30 m      # black
ESC [ 31 m      # red
ESC [ 32 m      # green
ESC [ 33 m      # yellow
ESC [ 34 m      # blue
ESC [ 35 m      # magenta
ESC [ 36 m      # cyan
ESC [ 37 m      # white
ESC [ 39 m      # reset

# BACKGROUND
ESC [ 40 m      # black
ESC [ 41 m      # red
ESC [ 42 m      # green
ESC [ 43 m      # yellow
ESC [ 44 m      # blue
ESC [ 45 m      # magenta
ESC [ 46 m      # cyan
ESC [ 47 m      # white
ESC [ 49 m      # reset
"""

WIDTH = 100
HEIGHT = 50

world=[x[:] for x in [[0]*WIDTH]*HEIGHT]


for i in range(5):
   for j in range(10):
      world[2+i][10+j]=1

world[5][12]=2 # line 6, column 13
 
posX=10
posY=8

while True:   
   sys.stdout.write('\033[0;0H') #goto 0,0
   sys.stdout.write('\033[0J')   #clear screen
   
   world[posX][posY]=2
   posY+=1
   
   for i in range(HEIGHT):
      for j in range(WIDTH):
         #sys.stdout.write(str(world[i][j]))
         sys.stdout.write(char_display[world[i][j]])
      sys.stdout.write('\033[39;49m\n')
   sys.stdout.flush()

   k=sys.stdin.read(1)
   if k=='q':
      break

