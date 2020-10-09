# Basic file handling

# File Reading
# read the whole file
with open('python.txt') as f:
    read_data = f.read()

print(read_data)

# read line by line
with open('python.txt') as f:
    for i in range(3):
        line = f.readline()
        print(line, end='')

# more simpler
with open('python.txt') as f:
    for line in f:
        print(line, end='')
        # or strip the newline
        print(line.strip())

# File Writing

# File opening modes

# r, w, a, r+

# text and binary mode 'b'

# Write to File
names = ['Alpha', 'Beta', 'Charlie', 'Delta', 'Echo']
with open('output.txt', 'w') as f:
    for name in names:
        f.write(name)

# Append to a file
names = ['Foxtrat', 'Golf', 'Hotel', 'India']
with open('output.txt', 'a') as f:
    for name in names:
        f.write(name)

# converting objects
t = ("John", 35)
with open('output.txt', 'w') as f:
    f.write(str(t))


# tell, seek and read
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)      # Go to the 6th byte in the file
f.read(1)
f.seek(-3, 2)  # Go to the 3rd byte before the end
f.read(1)

# writing json
import json
l = [1, 'simple', 'list']

with open('jsonfile', 'w') as f:
    json.dump(l, f)

# reading json
import json

with open('jsonfile', 'r') as f:
    x = json.load(f)
    print(x)

# CSV Handling

# Read CSV - https://realpython.com/python-csv/#reading-csv-files-with-csv

# Read CSV into dict - https://realpython.com/python-csv/#reading-csv-files-into-a-dictionary-with-csv

# working with Directories

import os

with os.scandir('.') as entries:
    for entry in entries:
        print(entry.name)

# Standard Libs https://docs.python.org/3/tutorial/stdlib.html

# More Standard Libs https://docs.python.org/3/tutorial/stdlib2.html

# VirtualEnvs and Packages https://docs.python.org/3/tutorial/venv.html