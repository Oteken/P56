from pymongo import MongoClient

class DBInteractions:
    uri = 'mongodb://oteken:lol123123@ds047484.mongolab.com:47484/citygis'
    client = MongoClient(uri)
    db = client.citygis

    def set_uri(self, uri):
        self.uri = uri
        self.client = MongoClient(uri)

    def get_uri(self):
        return self.uri

    def set_db(self, db):
        newDb = db
        self.db = self.client.newDb

    def get_db(self):
        return self.db

    def insertList(table, dataList, header):
        for i in range(0, len(dataList)):
            insertDict = {}
            for j in range(0, len(header)):
                insertDict[header[j]] = dataList[i][j]
            table.insert(insertDict)