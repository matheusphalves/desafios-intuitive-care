# -*- coding: utf-8 -*-
import csv
from .operadora import Operadora


class QueryService:
    def __init__(self, items = []):
        self.items = items
        pass
    
    def readCSV(self,filePath, skipLines = 3):
        # reading csv file
        with open(filePath, 'r') as csvfile:
            #criação de objeto csvreader
            csvreader = csv.reader(csvfile)
            for row in csvreader: #lendo linha a linha
                self.items.append(row)
            self.items = self.items[skipLines:]

    def searchItems(self, queryText):
        returnItems = []
        if(len(self.items)):
            for item in self.items:
                currentText = ''.join(str(element.lower()) for element in item)
                if(currentText.find(queryText)!=-1): #algo foi encontrado
                    toSave = currentText.split(';')
                    returnItems.append(Operadora(toSave))
        print(returnItems)
        return returnItems


#teste = QueryService()
#teste.readCSV('../resources/Relatorio_cadop.csv')
#print(teste.searchItems('11828089000103')[0].toJSON())