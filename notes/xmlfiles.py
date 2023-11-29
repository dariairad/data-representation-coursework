# for files

from xml.dom.minidom import parse
filename = "employees.xml"

doc = parse(filename)

# or

with open(filename) as fp:
    doc = parse(fp)

# check if it works
print (doc.toprettyxml(), end="")