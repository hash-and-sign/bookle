# sort.py: reads a specified folder, prints a numbered list, appends each
#  selected file (number entered from console) to sorted.txt.
# Command line syntax: python sort.py folder-name

import os
import sys

if len(sys.argv) == 2:
    folder = sys.argv[1]
else:
    sys.exit()

sorted_file = 'sorted.txt'
files = os.listdir(folder)
last = ''

with open(sorted_file, 'a') as sorted:
    while 1:
        i = 1
        for file in files:
            print(i, file)
            i = i + 1
        print(f'last: {last}')
        i = int(input())
        if i == 0:
            break
        if i < 1 or i > len(files):
            print('out of range')
            continue
        last = files[i - 1]
        sorted.write(files[i - 1] + '\n')
        sorted.flush()
        files.pop(i - 1)
    sorted.close()
