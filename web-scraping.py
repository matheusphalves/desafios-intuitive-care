from bs4 import BeautifulSoup
import requests
import os

#classe responsável por realizar o Web Scraping para obter a versão mais recente do Padrão TISS
class WebScrapingPadraoTISS:
    def __init__(self, soupObject = None, html = None):
        pass
    def accessUrl(self, url):
        try:
            self.html = requests.get(url).content
            self.soupObject = BeautifulSoup(self.html, 'html.parser')
        except Exception as e:
            print(e)

    def getLastestPadraoTISS(self, url, fileName = 'Componente Organizacional'):
        self.accessUrl(url)
        urlToDownload = None
        for row in self.soupObject.find_all('tr')[1:]: #obter todas as linhas da tabela
            if(fileName == row.text.split('\n')[1]):#obter link para download do nome do arquivo informado
                urlToDownload = row.find_all('a', href = True)[0]['href']
                break
        if(urlToDownload):
            self.downloadFile(urlToDownload) #url é enviada para download do recurso
        else:
            print("[There's no route to download with file name]: ", fileName)

    def downloadFile(self, urlToDownload):
        try:
            filename = f"arquivo - {urlToDownload.split('/')[-1]}"
            print('[Downloading file]: ', filename)
            pdfFile = open(filename, 'wb')
            pdfFile.write(requests.get(urlToDownload).content)
            pdfFile.close()
            print('[Downloaded file at]: ', os.getcwd())
            pass
        except Exception as e:
            print(e)

    def getHTMLContent(self, url = 'https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss'):
        try:
            self.accessUrl(url)
            alertLinkList = self.soupObject.find_all("a", class_="alert-link", href = True)
            #analisando a estrutura do site, percebe-se que as versões mais atuais são adicionadas no topo da página
            urlToRequest = alertLinkList[0]['href'] #obtido link para acesso à versão mais recente
            print('[Requesting content from]: ', urlToRequest)
            self.getLastestPadraoTISS(urlToRequest)
        except Exception as e:
            print(e)


webScraping = WebScrapingPadraoTISS()

webScraping.getHTMLContent()