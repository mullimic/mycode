#!/usr/bin/env python3

import os


while(True):
   varfile = input("What is the name of the file? " )

   vardir = input("What directory is the file in? " )

   if os.path.isfile(vardir + varfile):
      break

