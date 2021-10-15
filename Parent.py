#!/usr/bin/python3

# Mokeeva Polina 11-902

import os
import sys
import random


if(len(sys.argv)<2):
   print("Error!");
   os._exit(1);

n=int(sys.argv[1]);
for i in range (0, n):
   child = os.fork(0);
   if (child > 0):
      print("The Parent process is PID = %d" % (os.getpid()));
      answer = os.wait();
      print('The Child process (PID = %d) finished with ststus (%d)' % (answer[0], answer[1] / 256))
   else:
      rand = random.randomint(5,10)
      sys.argv = ['Child.py', rand]
      exec(open('Child.py').read())