#!/usr/bin/python3

# Mokeeva Polina 11-902

import os
import time
import sys
import random

if(len(sys.argv) < 2):
   print("ERROR!");
   os._exit(1);
print('Child programm is running in process with (PID = %d) with arg = %d' % (os.getpid(), sys.argv[1]))
time.sleep(int(sys.argv[1]))
print("Child process ended (PID  = %d)" % (os.getpid()));
os._exit(random.randint(0, 1))

