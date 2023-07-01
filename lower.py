# lower.py: converts all filenames in a specified folder to be URL compatible.
# Command line syntax: python lower.py folder-name
# The program should be run in the same directory as the folder
# Algorithm: convert to lowercase, replace spaces with underscores,
#   remove all non-(period | hyphen) punctuation.
# Not recommended for non-ascii character sets. Use urlencoder.org instead.

import os
import sys
import re

if len(sys.argv) == 2:
    folder = sys.argv[1]
else:
    sys.exit()

files = os.listdir(folder)

for old in files:
    print(old, end = ' -> ')
    new = old.lower()
    new = re.sub(' ', '_', new)
    new = re.sub('[^a-zA-Z0-9_\.\-]', '', new)
    new = re.sub('_*\-+_*', '-', new)
    if len(new) == 0:
        continue
    print(new)
    os.rename(folder+'/'+old, folder+'/'+new)
