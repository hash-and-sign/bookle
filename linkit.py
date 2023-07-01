# linkit.py: converts URLs the specified file to links, outputs to html file.
# Command line syntax: python linkit.py urls.txt

import sys

if len(sys.argv) == 2:
    urls_file = sys.argv[1]
else:
    sys.exit()

linked_file = urls_file + '.html'

with open(linked_file, 'w') as linked:
    with open(urls_file, 'r') as urls:
        lines = urls.readlines()
        for line in lines:
            line = line.rstrip()
            print(f"<a href='{line}'>{line}</a><br>\n")
            linked.write(f"<a href='{line}'>{line}</a><br>\n")
        urls.close()
    linked.close()

