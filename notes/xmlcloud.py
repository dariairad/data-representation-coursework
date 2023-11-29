import requests
from xml.dom.minidom import parseString
url = "URL"


page = requests.get(url)
doc = parseString(page.content)


print (doc.toprettyxml(), end="")