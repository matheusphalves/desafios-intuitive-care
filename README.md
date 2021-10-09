# desafios-intuitive-care
Resolução dos desafios propostos pelo processo seletivo da IntuitiveCare

# Test 04 - Front-end

Neste teste o candidato deverá criar uma interface web (usando o framework Vue.js) que se comunicará com um servidor em uma das linguagens mencionadas no fim desse email para realizar as tarefas de código abaixo.
Tarefas de Preparação:    
- Baixar csv do link: http://www.ans.gov.br/externo/site_novo/informacoes_avaliacoes_oper/lista_cadop.asp

Tarefas de código:
- Criar servidor com rota que realiza uma busca textual na lista de cadastro de operadoras (obtido na tarefa de prepação) e retorne as linhas que mais se assemelham
- Criar uma interface usando o framework Vue.js que permita a um usuário fazer essa pesquisa pelo browser



# How to run

Antes de executar, é preciso instalar o gerenciador de pacotes pip ou qualquer outro de sua preferência. Uma vez instalado (pip), execute os seguintes comandos listados abaixo. Para o ambiente Windows, simplesmente remova o ``` sudo ``` da linha de comando.

# BACK-END
```
sudo pip install flask
sudo pip install flask_cors
```

Serving on port 5100.


# API route

``` URL_API/query_items ```: retornará uma lista com as linhas que de certa forma mais se assemelham com o texto informado.

```
{
    "query": "your query text"
} 
```

Até o momento, estou tendo dificuldades na serialização do objeto Operadora para o formato JSON.

# FRONT-END

Esta é a minha primeira vez utiizando o Vue.js, então ainda estou amadurecendo o compreendimento de sua arquitetura e como utilizar as suas boas práticas. De qualquer forma, peço perdão - estou estudando o framework!

# NPM packages

axios
bootstrap (UI library)









