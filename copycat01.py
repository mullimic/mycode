#!/usr.bin/env python3

import shutil
import os

#force python to start in this directory
os.chdir('/home/student/mycode/')

#Cory file to a new file
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

#Copy this while directory to another location
shutil.copytree('5g_research/', '5g_research_backup/')

