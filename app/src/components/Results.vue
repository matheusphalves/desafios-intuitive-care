<template>
  <div>
    <div v-if="items.length>0">
        <h3>Resultados encontrados</h3>
        <b-table striped hover :items="items"></b-table>
    </div>

    <div v-if="items.length==0">
        <h3>Desculpe, não existem resultados para o termo buscado.</h3>
    </div>
    
  </div>
</template>

<script>
export default {
    name: 'Results',
    props: [],
    data() {
      return {
        fields: ['registroANS', 'cnpj', 'razaoSocial', 'nomeFantasia', 'modalidade',
        'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep', 'ddd', 'telefone', 'fax',
        'enderecoEletronico', 'representante', 'cargoRepresentante', 'dataRegistroANS'],
        items: [
          { registroANS: true, age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { registroANS: false, age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { registroANS: false, age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { registroANS: true, age: 38, first_name: 'Jami', last_name: 'Carney' }
        ]
      }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

input[type=text]{
    -webkit-border-radius: 20px;
    -moz-border-radius: 20px;
     border-radius: 20px;
     border: 1px solid #2d9fd9;
     color: #a0d18c;
     width: 250px;
     height: 30px;
     padding-left: 10px;
    }
</style>
