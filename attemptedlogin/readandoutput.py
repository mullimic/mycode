#!/usr/bin/env python3

tcounter = 0 # intialize the counter variable

var1 = "Some text i added" #just a variable
file1 = open('file.dat', 'w') # Opening the file we want to work on or creatig if it doesn't exist

print('what I want to add to file', file=file1) #adding some text
print('Here is some more text to add', file=file1) #adding some text again
print(var1, file=file1) #writing from the variable to the file

file1.close()   #if there is an open there needs to be a close

varfileread = open('file.dat', 'r') #Open file for reading
varfilewrite = open('file2.dat', 'w') # Open file for writing

templist = varfileread.readlines() #this will put everything in this file into a list, each line is an object in the list

for x in templist: # start going through the list we created line by line
   if "to" in x.lower(): #find all lines with 'to' in them and make them lower case
     print(x)
     print(x, file=varfilewrite) # write the ifnormation to the file
     tcounter = tcounter + 1 # counter for number of time line was found
print("\n ***** \nto was found: ", tcounter) # print to screen the number of times it was found

varfileread.close() # close file
varfilewrite.close() #close file
