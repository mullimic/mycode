#!/usr/bin/env python

import shutil
import os
#set teh home directory it will run from
os.chdir('/home/student/mycode/')
#move file to othe folder
shutil.move('raynor.obj', 'ceph_storage/')
#get new file name from user
xname = input('What is the new name for kerrigan.obj?')
#use move command to change the name of this file using the user input
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
