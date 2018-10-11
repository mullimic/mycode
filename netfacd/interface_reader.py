#!/usr/bin/env python3

import netifaces
print(netifaces.interfaces())

for i in netifaces.interfaces():
  ## Readin file line by line 
  print('\n****************Details of Interface - ' + i + ' *********************')
  ##Try to find the following information
  try:
    print('MAC: ', end='') ## This print statement will always print the MAC without an end of line
    print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) ## Prints the MAC address
    print('IP: ', end='') ## This print statement will always pring the IP without an end of line
    print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) ## Print the IP address
  ##If you didn't find the information print the following to the screen
  except: 
    print('Could not collect adapter information')

