#Description: Parses a line of ARGOS tracking data
# 

#Load in the selected file in read-only mode:
fileObj = open('data/SaraNoHeaders.txt','r')

#read in all lines:
lineslist = fileObj.readlines()

#Close the file:
fileObj.close()

# Create empty dictionaries
dateDict = {}
locationDict = {}

#Use a for loop to iterate all of the lines:
for line in lineslist:
    #split line
    LineData=line.split("\t")

    #assign each element to a proper variable:
    record_id = LineData[0]
    tag_id = LineData[1]
    datetime_utc = LineData[2]
    obs_lc = LineData[3]
    obs_iq = LineData[4]
    obslat = LineData[5]
    obslong = LineData[6]

    #split date/time even further:
    obsDate = datetime_utc.split()[0]
    obsTime = datetime_utc.split()[1]

    #Filter records that get added to the dictionary
    if obs_lc in ("1","2","3"):
        #Add values to dictionary:
        dateDict[record_id] = (obsDate, obsTime)
        locationDict[record_id] = (obslat, obslong)

#Write that you're done
print("done")

# Ask the user for a date, specifying the format
userDate = input("Enter a date (M/D/YYYY)")

#Create an empty key list
keyList = []

values = dateDict.items()

# Loop through all key, value pairs in the dateDictionary
for k, v in values:
    #See if the date (the value) matches the user date
    if v[0] == userDate:
        keyList.append(k)
    
length = len(keyList)
if length < 1:
    print("No entries for this date.")

# Loop through each key and report the associated date location
for k in keyList:
    theDate = dateDict[k]
    theLocation = locationDict[k]
    theLat = theLocation[0]
    theLon = theLocation[1]
    print("Record {0}: Sara was seen at {1}N-{2}W, on {3}".format(k,theLat,theLon,theDate))
