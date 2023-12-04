from lec4valoff import getAll

data = getAll()
totalArea = 0

for entry in data:
    valuationReports = entry["ValuationReport"]
    for valuationReport in valuationReports:
        #print(valuationReport)
        if valuationReport["FloorUse"] == "HAIR SALON":
            totalArea += valuationReport["Area"]

print (totalArea)