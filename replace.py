# replace.py: replaces URLs in a PDF file according to the text file urls.txt.
# Command line syntax: python replace.py file.pdf
# urls.txt file format, one replacement per line: old_url,new_local_filepath
# new_local_filepath is relative to the server folder; example: videos/clip.mp4

import sys

if len(sys.argv) == 2:
    pdf_file = sys.argv[1]
else:
    sys.exit()

dict_file = 'urls.txt'
dict = {}

with open(dict_file, 'r') as map:
    lines = map.readlines()
    for line in lines:
        line = line.split(',')
        if len(line) != 2:
            continue
        dict[line[0]] = line[1]
    map.close()

if len(dict) == 0:
    sys.exit()

with open(pdf_file, 'rb') as pdf:
    file = pdf.read()
    pdf.close()
    with open(pdf_file, 'wb') as pdf:
        for key in dict:
            file = file.replace(bytes(key, 'utf-8'), bytes('http://localhost/' + dict[key], 'utf-8'))
        pdf.write(file)
        pdf.close()
