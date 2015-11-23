import csv
from pymongo import MongoClient

uri = 'mongodb://oteken:lol123123@ds047484.mongolab.com:47484/citygis'
client = MongoClient(uri)
db = client.citygis
procent = 0

connectionsTable = db.connections
connectionsCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/connections.csv'
monitoringTable = db.monitoring
monitoringCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/monitoring.csv'
eventsTable = db.events
eventsCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/events.csv'
positionsTable = db.positions
positionsCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/positions.csv'



def readCsvFile(filePath, delimiter):
    with open(filePath) as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)

        columnOne = next(reader)
        csvDataList = []

        for row in reader:
            csvDataList.append(row)

    return csvDataList;

def readCsvHeader(filePath, delimiter):
    with open(filePath) as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)

        header = next(reader)

    return header;

def insertCsvFile(table, dataList, header):
    for i in range(0, len(dataList)):
        insertDict = {}
        for j in range(0, len(header)):
            insertDict[header[j]] = dataList[i][j]
        table.insert(insertDict)
        global procent
        procent = procent + 1
        if procent%5000 == 1:
            print(procent)

print("Reading Connections")
csvData = readCsvFile(connectionsCsvFilePath, ";")
print("Done Reading")
csvHeader = readCsvHeader(connectionsCsvFilePath, ";")
print("Inserting")
insertCsvFile(connectionsTable, csvData, csvHeader)
print("Done")

print("Reading Monitoring")
csvData = readCsvFile(monitoringCsvFilePath, ";")
print("Done Reading")
csvHeader = readCsvHeader(monitoringCsvFilePath, ";")
print("Inserting")
insertCsvFile(monitoringTable, csvData, csvHeader)
print("Done")

print("Reading Events")
csvData = readCsvFile(eventsCsvFilePath, ";")
print("Done Reading")
csvHeader = readCsvHeader(eventsCsvFilePath, ";")
print("Inserting")
insertCsvFile(eventsTable, csvData, csvHeader)
print("Done")

print("Reading Positions")
csvData = readCsvFile(positionsCsvFilePath, ";")
print("Done Reading")
csvHeader = readCsvHeader(positionsCsvFilePath, ";")
print("Inserting")
insertCsvFile(positionsTable, csvData, csvHeader)
print("Do")
