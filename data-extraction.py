#criação do arquivo
from tabula.io import read_pdf
from zipfile import ZipFile
import glob, os
import csv


class TableExtractor:

    def __init__(self, tableList = []):
        pass

    def extractTables(self, tableNames = ['Tabela de Tipo do Demandante', 'Tabela de Categoria do Padrão TISS', 'Tabela de Tipo de Solicitação'], pagesDelimiter = '108-114'):
        self.readPDFTables(tableNames=tableNames, pagesDelimiter=pagesDelimiter) #efetua a leitura e extração das tabelas do pdf, caso existam
        self.convertToCSV(tableNames)
        self.zipData('Teste_Intuitive_Care_{matheus_phelipe_alves_pinto}','csv')

    def readPDFTables(self, tableNames,  pagesDelimiter, columns = ['Código', 'Descrição da Categoria'],):
        self.tableList = read_pdf('padrao_tiss_componente_organizacional_202108.pdf', pages = pagesDelimiter)
        #passar link do pdf diretamente
        #filtrar tabelas

    def convertToCSV(self, tableNames):
        tableNumber = -1
        if(len(self.tableList)):
            for table in self.tableList:
                if('Tabela' in table.iloc[0].to_string()):
                    tableNumber += 1
                    table.to_csv(tableNames[tableNumber]+ '.csv', sep=';', encoding='utf-8', index = False)
                else:
                    table.to_csv(tableNames[tableNumber]+ '.csv', mode='a', sep=';', encoding='utf-8', index = False, header=False)

    def zipData(self, zipName, extensionType):
        files = glob.glob(os.getcwd() + f"/*.{extensionType}") #obtem diretório atual
        print(files)
        if(len(files)>0):
            zipObject = ZipFile(f'{zipName}.zip', 'w')
            for file in files:#exibe arquivos .csv a serem zipados
                zipObject.write(file.split('\\')[-1])
            zipObject.close()
            print(f'[Created zip file ({len(files)} files) at]: ', os.getcwd())


tbExtractor = TableExtractor()

tbExtractor.extractTables()