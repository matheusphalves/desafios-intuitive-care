import csv


class QueryService:
    def __init__(self, items = []):
        self.items = items
        pass
    
    def readCSV(self,filePath):
        # reading csv file
        with open(filePath, 'r') as csvfile:
            #criação de objeto csvreader
            csvreader = csv.reader(csvfile)
            for row in csvreader: #lendo linha a linha
                self.items.append(row)

    def searchItems(self, queryText):
        returnItems = []
        if(len(self.items)):
            for item in self.items:
                currentText = ''.join(str(element.lower()) for element in item)
                if(currentText.find(queryText)!=-1): #algo foi encontrado
                    returnItems.append(item)
        return returnItems


#teste = QueryService()
#teste.readCSV()
#print(teste.searchItems('90747908000156'))