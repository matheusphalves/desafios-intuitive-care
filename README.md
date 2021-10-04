# desafios-intuitive-care
Resolução dos desafios propostos pelo processo seletivo da IntuitiveCare

# Test 01 - Web Scraping

Neste teste o candidato deverá criar um código (em uma das linguagens mencionadas no fim desse email) que execute as tarefas de código abaixo.
Tarefas de código:
- 1.1 - Acessar o site: http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar;
- 1.2 - Buscar a versão mais recente do Padrão TISS (arquivo - padrao_tiss_componente_organizacional_201902.pdf);
- 1.3 - Baixar o componente organizacional;


# How to run

Antes de executar, é preciso instalar o gerenciador de pacotes pip ou qualquer outro de sua preferência. Uma vez instalado, execute os seguintes comandos listados abaixo. Para o ambiente Windows, simplesmente remova o ``` sudo ``` da linha de comando.

```
sudo pip install requests
sudo pip install beautifulsoup4
```

# Docs

## Classe
```WebScrapingPadraoTISS```: classe responsável por efetuar o download do Padrão TISS mais recente.

## Métodos

```accessUrl```: método recebe uma URL como parâmetro e atualiza o valor do objeto do tipo BeautifulSoup. 

```getLastestPadraoTISS```: método recebe a URL da versão do padrão TISS e procura o link de download do pdf do componente organizacional. O método pode receber o nome do recurso em específico no qual se deseja ser obtido.

```downloadFile```: método efetua o download (URL recebida como parâmetro) do recurso e realiza a gravação dos seus bits em um arquivo, armazenando-o na raiz de execução do script.

```getHTMLContent```: método efetua o acesso inicial à página, obtendo a página da versão do padrão TISS mais recente. 



