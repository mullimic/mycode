#!/usr/bin/env python3

#Create list
my_list = [ "192.168.0.5", 5060, "UP" ]

#Show first utem with is a string
print("The first item in the list (IP): " + my_list[0] )

#Show the second item which is an interger, change the item to a string so you can concatenate 
print("the second item in the list (port): " + str(my_list[1]) )

#Print the last value which is a string
print("The last item in the list (state): " + my_list[2] )

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]


port1 = new_list[0]
port2 = new_list[1]
port3 = new_list[2]
ip1 = new_list[3]
ip2 = new_list[4]
conn = new_list[5]

print("When I " + conn + " into IP addresses " + ip1 + " or " + ip2 + " I am unable to ping ports " + str(port1) + " , " + port2 + " or " + str(port3) )
