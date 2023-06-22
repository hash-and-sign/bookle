# extract.py: Extracts URLs from a PDF file
# Command line syntax: python extract.py file.pdf
# The extracted URLs are output to the file urls.txt, one per line

import sys
import re

if len(sys.argv) == 2:
    pdf_file = sys.argv[1]
else:
    sys.exit()

url_file = 'urls.txt'

with open(pdf_file, 'rb') as pdf:
    uris = sorted(set(re.findall(b'URI *\((.*?)\)', pdf.read())))
    # uris: sorted, unique list of URIs
    pdf.close()
    with open(url_file, 'w') as url:
        for uri in uris:
            url.write(uri.decode('ascii') + '\n')
        url.close()
