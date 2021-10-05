#criação do arquivo
from tabula.io import read_pdf
from zipfile import ZipFile
import glob, os


class TableExtractor:

    def __init__(self, tableList = []):
        pass

    def extractTables(self, tableNames = ['Tabela de Tipo do Demandante', 'Tabela de Categoria do Padrão TISS', 'Tabela de Tipo de Solicitação'], pagesDelimiter = '108-114'):
        #self.readPDFTables(tableNames=tableNames, pagesDelimiter=pagesDelimiter) #efetua a leitura e extração das tabelas do pdf, caso existam
        #self.convertToCSV(tableNames)
        self.zipData('Teste_Intuitive_Care_{matheus_phelipe_alves_pinto}','csv')

    def readPDFTables(self, tableNames, pagesDelimiter):
        self.tableList = read_pdf('padrao_tiss_componente_organizacional_202108.pdf', pages = pagesDelimiter)
        #passar link do pdf diretamente
        #filtrar tabelas
        for item in self.tableList:
            print(item)
        pass

    def convertToCSV(self, tableNames):
        if(len(self.tableList)):
            for number in range(len(self.tableList)):
                self.tableList[number].to_csv(tableNames[number]+ '.csv', sep='\t', na_rep = '   ', encoding='utf-8', index = False)

    def zipData(self, zipName, extensionType):
        zipObject = ZipFile(f'{zipName}.zip', 'w')
        files = glob.glob(os.getcwd() + f"/*.{extensionType}") #obtem diretório atual
        
        for file in files:#exibe arquivos .csv a serem zipados
            zipObject.write(file.split('\\')[-1])
            print(file.split('\\')[-1])
        zipObject.close()
        print('[Created zip file at]: ', os.getcwd())


tbExtractor = TableExtractor()

tbExtractor.extractTables()