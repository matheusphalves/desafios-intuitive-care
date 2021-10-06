# desafios-intuitive-care
Resolução dos desafios propostos pelo processo seletivo da IntuitiveCare

# Test 02 - Data Extraction

Neste teste o candidato deverá criar um código (em uma das linguagens mencionadas no fim desse email) que execute as tarefas de código abaixo.
Tarefas de código:
- Extrair do pdf do teste 1 acima os dados dos Quadros 30,31,32 (Tabela de categoria do Padrão TISS);
- Salvar dados em tabelas estruturadas, em csvs;
- Zipar todos os csvs num arquivo "Teste_Intuitive_Care_{seu_nome}.zip".



# How to run

Antes de executar, é preciso instalar o gerenciador de pacotes pip ou qualquer outro de sua preferência. Uma vez instalado (pip), execute os seguintes comandos listados abaixo. Para o ambiente Windows, simplesmente remova o ``` sudo ``` da linha de comando.

```
sudo pip install tabula-py
```


# Docs

``` extractTables ``` método responsável pela execução do fluxo proposto pelo desafio.

``` readPDFTables ``` método efetua a leitura do PDF. Podendo ser informado um delimitador de páginas e os nomes das tabelas de interesse de serem extraídas. O delimitador pode ser inserido nos seguintes formatos, por exemplo:
```
all
1-2
```

``` checkTableNames ``` método irá verificar se as tabelas extraídas combinam com os nomes informados pelo usuário. Em caso contrário, o fluxo de execução é encerrado. 

``` convertToCSV ``` método efetua o salvamento dos data frames extraídos. 

``` zipData ``` método realiza o salvamento dos arquivos de uma dada extensão (nesse caso, os arquivos em .csv)






