


connectionsTable = db.connections
connectionsCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/connections.csv'
monitoringTable = db.monitoring
monitoringCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/monitoring.csv'
eventsTable = db.events
eventsCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/events.csv'
positionsTable = db.positions
positionsCsvFilePath = 'D:/Oteken/School/INF/Jaar 2/Periode 1/Project 5 6/positions.csv'

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
print("yay")
