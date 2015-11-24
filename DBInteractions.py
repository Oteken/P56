
class DBInteractions:

    def insertList(self, table, dataList, header):
        for i in range(0, len(dataList)):
            insertDict = {}
            for j in range(0, len(header)):
                insertDict[header[j]] = dataList[i][j]
            table.insert(insertDict)