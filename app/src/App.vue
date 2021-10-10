<template>
  <b-container>
    <b-row>
      <h1>Buscador</h1>
    </b-row>
    <b-row>
      <div style="margin:10px;">
        <input v-model="inputValue" style="margin-right:10px" type="text" placeholder="Digite alguma palavra chave">
        <b-button @click="search(inputValue)">Pesquisar</b-button>
        <p>
          Para visualizar a base de dados utilizada,
          <a href="http://www.ans.gov.br/externo/site_novo/informacoes_avaliacoes_oper/lista_cadop.asp" target="_blank" rel="noopener">clique aqui</a>.
        </p>
      </div>
    </b-row>
    <b-row>
    <div>
        <div v-if="items">
            <div v-if="items.length>0">
            <h3>Resultados encontrados ({{items.length}})</h3>
            <b-table striped hover :items="items"></b-table>
            </div>
        <div v-if="items.length==0">
            <h3>Desculpe, não existem resultados para o termo buscado.</h3>
        </div>
        </div>      
      </div>
    </b-row>
  </b-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  props: [],
  components: {
  },  
  data() {
      return {
        inputValue: '',
        fields: ['registroANS', 'cnpj', 'razaoSocial', 'nomeFantasia', 'modalidade',
        'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep', 'ddd', 'telefone', 'fax',
        'enderecoEletronico', 'representante', 'cargoRepresentante', 'dataRegistroANS'],
        items: null
      }
    },   
  methods:{
    search(text){
      if(text && text.length>=3){
        axios.post(`http://127.0.0.1:5100/query_items`, {query: text})
         .then((res) => {
           this.items = res.data
         })
         .catch((error) => {
           this.items = []
           console.log(error);
         });
      }   
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
