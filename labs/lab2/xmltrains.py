# Lab 2: Trains

import requests
import csv
from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
    'TrainLatitude',
    'TrainLongitude',
    'TrainCode',
    'TrainDate',
    'PublicMessage',
    'Direction'
    ]       

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

# print (doc.toprettyxml(), end="") 

# with open("trainxml.xml","w") as xmlfp:
#   doc.writexml(xmlfp)

# store into a CSV
with open('d_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        # print (traincode)
        if traincode.startswith('D'): #if traincode starts with D append to the list
            dataList = []
            for retrieveTag in retrieveTags:
                datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
                dataList.append(datanode.firstChild.nodeValue.strip())
            train_writer.writerow(dataList)

