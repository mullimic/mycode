#!/usr/bin/env python3

ipchk = input('Apply an IP address: ') #this line now prompts the user for input

if ipchk == '192.168.70.1': #if a matchon this IP 
    print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.') #indent 
elif ipchk: # if any data is provided, this test true
    print('Looks like the IP address was set: ' +ipchk) #indented under if
else: #if data is not provided
    print('You did not provide data. ')
