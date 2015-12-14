import csv

class CsvInteractions:

    def readCsvFile(self, filePath, delimiter):
        with open(filePath) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)

            columnOne = next(reader)
            csvDataList = []

            for row in reader:
                csvDataList.append(row)

        return csvDataList;

    def readCsvHeader(self, filePath, delimiter):
        with open(filePath) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)

            header = next(reader)

        return header;
