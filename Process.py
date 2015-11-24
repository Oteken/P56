import DBInteractions
import CsvInteractions
from pymongo import MongoClient

DB = DBInteractions.DBInteractions()
CSV = CsvInteractions.CsvInteractions()

uri = ('mongodb://oteken:lol123123@ds047484.mongolab.com:47484/citygis')
client = MongoClient(uri)
db = client.citygis

connectionsTable = db.connections
connectionsCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/connections.csv'
monitoringTable = db.monitoring
monitoringCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/monitoring.csv'
eventsTable = db.events
eventsCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/events.csv'
positionsTable = db.positions
positionsCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/positions.csv'

def readAndInsert(filePath, table):
    csvData = CSV.readCsvFile(filePath, ";")
    csvHeader = CSV.readCsvHeader(filePath, ";")
    DB.insertList(table, csvData, csvHeader)

readAndInsert(connectionsCsvFilePath, connectionsTable)
readAndInsert(monitoringCsvFilePath, monitoringTable)
readAndInsert(eventsCsvFilePath, eventsTable)
readAndInsert(positionsCsvFilePath, positionsTable)


