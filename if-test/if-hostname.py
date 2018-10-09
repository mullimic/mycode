#!/usr/bin/env python3

# Get user input of hostname
xhost = input('What is your hostname?').lower()
#Print out hostname from user input
print("your hostname is:" + xhost)
#Start if statement if user input matches expected output print out statement
if xhost == 'mtg':
  print('The hostname was found to be: ' + xhost) and print('hostname matches expected config')
else:
  print('hostname does not match expected config')
print('exiting the script')
