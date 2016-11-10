

# Create two empty dictionaries to store Longitude and Latitude
# Note: If I wished to store more than two elements I would definitely create a class for this.
# For two elements it isn't difficult to keep them synched.
LongitudeDict = {};
LatitudeDict = {};

#*************************************************************************************************
# Create a family of reusable functions for managing the creation of the JSON file.
#*************************************************************************************************

# Takes lat and lon and stores it in appropriate dictionary with key of droneID
def updateMapCoordinateData(droneID, lat, lon):
    LongitudeDict[droneID] = lon
    LatitudeDict[droneID] = lat

# Removes a coordinate from the dictionary
def removeMapCoordinateData(droneID):
    del LongitudeDict[droneID]
    del LatitudeDict[droneID]

# Generate a new file from the current content of LongitudeDict and LatitudeDict.  
# To avoid potential race conditions between Google Maps and writes to this file
# the function writes to a temporary file.  
# We then make an OS level call to copy the temporary file to the location read by Google Maps
def generateNewFile(fileName):
    dronesOnMap = len(LongitudeDict)
    open(fileName+".json", 'w').close()
    with open(fileName+".json", "a") as tempCoordFile:
        tempCoordFile.truncate()
        tempCoordFile.write('[')
        ctr = 0
        numDrones = len(LatitudeDict)
        for key, value in LatitudeDict.items():
            thisLat = value  # We can get this one automatically
            strLat = '%2.6f' % thisLat
            thisLon = LongitudeDict[key]  # We can use the Lat key to get this one
            strLon = '%2.6f' % thisLon
            tempCoordFile.write('{"droneID":"')
            tempCoordFile.write(key)
            tempCoordFile.write('","lat":"')
            tempCoordFile.write(strLat)
            tempCoordFile.write('","lon":"')
            tempCoordFile.write(strLon)
            tempCoordFile.write('"}')
            ctr=ctr+1
            if ctr == numDrones:
                tempCoordFile.write(']')
            else:
                tempCoordFile.write(',')
        #tempCoordFile.write('\n')
        #os.remove("currentPositions.json")
    