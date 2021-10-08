import json
class Operadora:
    def __init__(self, arrayData):
        self.registroANS = arrayData[0]
        self.cnpj = arrayData[1]
        self.razaoSocial = arrayData[2]
        self.nomeFantasia = arrayData[3]
        self.modalidade = arrayData[4]
        self.logradouro = arrayData[5]
        self.numero = arrayData[6]
        self.complemento = arrayData[7]
        self.bairro = arrayData[8]
        self.cidade = arrayData[9]
        self.uf = arrayData[10]
        self.cep = arrayData[11]
        self.ddd = arrayData[12]
        self.telefone = arrayData[13]
        self.fax = arrayData[14]
        self.enderecoEletronico = arrayData[15]
        self.representante = arrayData[16]
        self.cargoRepresentante = arrayData[17]
        self.dataRegistroANS = arrayData[18]
        pass