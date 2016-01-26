import csv
import datetime

from pymongo import MongoClient

uri = ('mongodb://localhost:27017/')
client = MongoClient(uri)
db = client.citygis

# Path to all csv files
connectionsCsvFilePath = 'C:/Users/0895642/Downloads/CSV Files/connections.csv'
monitoringCsvFilePath = 'C:/Users/0895642/Downloads/CSV Files/monitoring.csv'
eventsCsvFilePath = 'C:/Users/0895642/Downloads/CSV Files/events.csv'
positionsCsvFilePath = 'C:/Users/0895642/Downloads/CSV Files/positions.csv'

# Predefined the data types of the csv tables, because casting the data types would take longer.
connectionsDataTypes = ["date", "string", "string", "int"]
monitoringDataTypes = ["string", "date", "date", "string", "float", "float", "float"]
eventsDataTypes = ["date", "string", "string", "string", "int"]
positionsDataTypes = ["date", "string", "float", "float", "int", "int", "int", "int", "string"]

connectionsTable = db.connections
monitoringTable = db.monitoring
eventsTable = db.events
positionsTable = db.positions

# Inserts every row right after reading.
def fastInsert(filePath, delimiter, table, dataTypes):
    with open(filePath) as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        header = next(reader)
        i = 0
        j = 1
        insertDict = {}
        for row in reader:
            insertDict["_id"] = j
            i = 0
            for x in row:

                if dataTypes[i] == "string":
                    insertDict[header[i]] = x
                elif dataTypes[i] == "int":
                    insertDict[header[i]] = int(x)
                elif dataTypes[i] == "float":
                    insertDict[header[i]] = float(x)
                elif dataTypes[i] == "date":
                    insertDict[header[i]] = stringToDate(x)
                i += 1
            j += 1
            table.insert(insertDict)

def stringToDate(string):
    i = 0
    char = string[i]

    year = ""
    month = ""
    day = ""
    hour = ""
    minute = ""
    second = ""
    while(char!= "-"):
        year = year + char
        i += 1
        char = string[i]
    i += 1
    char = string[i]
    while(char!= "-"):
        month = month + char
        i += 1
        char = string[i]
    i += 1
    char = string[i]
    while(char!= " "):
        day = day + string[i]
        i += 1
        char = string [i]
    i += 1
    char = string[i]
    while(char!= ":"):
        hour = hour + string[i]
        i += 1
        char = string [i]
    i += 1
    char = string[i]
    while(char!= ":"):
        minute = minute + string[i]
        i += 1
        char = string [i]
    i += 1
    char = string[i]
    while(i < string.__len__()):
        second = second + string[i]
        i += 1
        if i < string.__len__():
            char = string [i]
    date = datetime.datetime(int(year), int(month), int(day),
                             int(hour), int(minute), int(second))
    return date

def insertCommand():
    print('connections')
    fastInsert(connectionsCsvFilePath, ";", connectionsTable, connectionsDataTypes)
    print('monitoring')
    fastInsert(monitoringCsvFilePath, ";", monitoringTable, monitoringDataTypes)
    print('events')
    fastInsert(eventsCsvFilePath, ";", eventsTable, eventsDataTypes)
    print('positions')
    fastInsert(positionsCsvFilePath, ";", positionsTable, positionsDataTypes)
    print('done')

insertCommand()