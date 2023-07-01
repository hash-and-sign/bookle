# merge.py: merges two specified files of the same number of lines
#  inserting ',sub-folder/' between them. Output to the console 
# Command line syntax: python merge.py urls.txt vids.txt sub_folder

import sys

if len(sys.argv) == 4:
    urls_file = sys.argv[1]
    vids_file = sys.argv[2]
    sub_folder = sys.argv[3]
else:
    sys.exit()

with open(urls_file, 'r') as urls:
    urls_lines = urls.readlines()
    urls.close()
    with open(vids_file, 'r') as vids:
        vids_lines = vids.readlines()
        vids.close()
        if len(urls_lines) != len(vids_lines):
            sys.exit()
        for i in range(0, len(urls_lines)):
            print(f'{urls_lines[i].rstrip()},{sub_folder}/{vids_lines[i].rstrip()}')
