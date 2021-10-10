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
            queryText = queryText.upper()
            for item in self.items:
                currentText = ''.join(str(element.upper()) for element in item)
                if(currentText.find(queryText)!=-1): #algo foi encontrado
                    content = currentText.split(';')
                    returnItems.append(
                        Operadora(content[0], content[1], content[2], content[3], content[4], content[5],
                        content[6], content[7], content[8], content[9], content[10], content[11], content[12], content[13], content[14],
                        content[15], content[16], content[17], content[18])
                    )
        return returnItems