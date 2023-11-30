# get elements
from xml.dom.minidom import parse
filename = "employees.xml"

doc = parse(filename)

employeeNodeList = doc.getElementsByTagName("Employee")
print (len(employeeNodeList))
for employeeNode in employeeNodeList:
    # get first child - first name
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    # get Text node from the First Name Node
    firstName = firstNameNode.firstChild.nodeValue.strip() #strip to remove blank spaces
    print(firstName)