import DBInteractions
import CsvInteractions
from pymongo import MongoClient
import csv
import datetime

DB = DBInteractions.DBInteractions()
CSV = CsvInteractions.CsvInteractions()

uri = ('mongodb://oteken:lol123123@ds047484.mongolab.com:47484/citygis')
client = MongoClient(uri)
db = client.citygis


connectionsTable = db.datetest
connectionsCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/connections.csv'
connectionsDataTypes = ["date", "string", "string", "int"]
monitoringTable = db.monitoring
monitoringCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/monitoring.csv'
monitoringDataTypes = ["string", "date", "date", "string", "float", "float", "float"]
eventsTable = db.events
eventsCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/events.csv'
eventsDataTypes = ["date", "string", "string", "string", "int"]
positionsTable = db.positions
positionsCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/positions.csv'
positionsDataTypes = ["date", "string", "float", "float", "int", "int", "int", "int", "string"]

def fastInsert(filePath, delimiter, table, dataTypes):
    with open(filePath) as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        header = next(reader)
        i = 0
        insertDict = {}
        for row in reader:
            i = 0
            insertDict = {}
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

fastInsert(connectionsCsvFilePath, ";", connectionsTable, connectionsDataTypes)
fastInsert(monitoringCsvFilePath, ";", monitoringTable, monitoringDataTypes)
fastInsert(eventsCsvFilePath, ";", eventsTable, eventsDataTypes)
fastInsert(positionsCsvFilePath, ";", positionsTable, positionsDataTypes)
