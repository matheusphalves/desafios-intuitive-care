#criação do arquivo
from tabula.io import read_pdf
from zipfile import ZipFile
import glob, os
import csv


class TableExtractor:

    def __init__(self, tableList = []):
        pass

    def extractTables(self, tableNames = ['Tabela de Tipo do Demandante', 'Tabela de Categoria do Padrão TISS', 'Tabela de Tipo de Solicitação'], pagesDelimiter = '108-114'):
        status = self.readPDFTables(tableNames, pagesDelimiter=pagesDelimiter) #efetua a leitura e extração das tabelas do pdf, caso existam
        if(status):
            print('[Tables found. Carrying to next steps]')
            self.convertToCSV(tableNames)
            self.zipData('Teste_Intuitive_Care_{matheus_phelipe_alves_pinto}','csv')
        else:
            print('[Some tables was not found]')

    def readPDFTables(self, tableNames,  pagesDelimiter):
        print('[Loading PDF file]')
        self.tableList = read_pdf('https://www.gov.br/ans/pt-br/arquivos/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-tiss/padrao-tiss/padrao_tiss_componente_organizacional_202108.pdf', pages = pagesDelimiter)
        print('[PDF loaded]')
        if(self.checkTableNames(tableNames, self.tableList)):
            return True #tabelas foram encontradas, prosseguir com demais etapas
        else:
            return False#alguma das tabelas não foi encontrada
        
    def checkTableNames(self, tableNames, tablesFound):
        strContent = ''
        auxTableNames = []
        for items in tablesFound:
            strContent += items.iloc[0].to_string()
        for item in tableNames:
            if(strContent.find(item) != -1):
                auxTableNames.append(item)

        if(len(tableNames) != len(auxTableNames)):
            return False
        else:
            return True

    def convertToCSV(self, tableNames):
        tableNumber = -1
        if(len(self.tableList)):
            print('[Creating CSV files]')
            for table in self.tableList:
                if('Tabela' in table.iloc[0].to_string()):
                    tableNumber += 1
                    table.dropna(inplace=True)#remoção de linhas vazias ou com valor NaN
                    table.to_csv(tableNames[tableNumber] + '.csv', sep=';', encoding='utf-8', index = False, header = True)
                else:
                    table.to_csv(tableNames[tableNumber] + '.csv', mode='a', sep=';', encoding='utf-8', index = False, header=False)

    def zipData(self, zipName, extensionType):
        files = glob.glob(os.getcwd() + f"/*.{extensionType}") #obtem diretório atual
        if(len(files)>0):
            zipObject = ZipFile(f'{zipName}.zip', 'w')
            for file in files:#exibe arquivos .csv a serem zipados
                zipObject.write(file.split('\\')[-1])
            zipObject.close()
            print(f'[Created zip file ({len(files)} files) at]: ', os.getcwd())


tbExtractor = TableExtractor()

tbExtractor.extractTables()