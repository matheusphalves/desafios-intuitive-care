<template>
  <b-container>
    <b-row>
      <h1>Buscador</h1>
    </b-row>
    <b-row>
      <div style="margin:10px;">
        <input v-model="searchText" style="margin-right:10px" type="text" placeholder="Digite alguma palavra chave">
        <b-button @click="search(searchText)">Pesquisar</b-button>
        <p>
          Para visualizar a base de dados utilizada,
          <a href="http://www.ans.gov.br/externo/site_novo/informacoes_avaliacoes_oper/lista_cadop.asp" target="_blank" rel="noopener">clique aqui</a>.
        </p>
      </div>
    </b-row>
    <b-row>
      <Results></Results>
    </b-row>
  </b-container>
</template>

<script>
import Results from './components/Results.vue'
import axios from 'axios';

export default {
  name: 'App',
  components: {
    Results
  },     
  methods:{
    search(text){
      if(text){
        axios.post(`http://127.0.0.1:5100/query_items`, {query: text})
         .then((res) => {
           console.log(res.data)
         })
         .catch((error) => {
           console.log(error);
         });
        console.log(text)
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
