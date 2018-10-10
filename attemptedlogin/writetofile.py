#!/usr/bin/env python3


var1 = "Some text"
file1 = open('file.dat', 'w')

print('what I want to add to file', file=file1)
print('Here is some more text', file=file1)
print(var1, file=file1)

file1.close()   #if there is an open there needs to be a close

