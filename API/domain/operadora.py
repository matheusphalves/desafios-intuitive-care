import json
class Operadora:
    def __init__(self, registroANS, cnpj, razaoSocial, nomeFantasia,
      modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone,
      fax, enderecoEletronico, representante, cargoRepresentante, dataRegistroANS  ):
        self.registroANS = registroANS
        self.cnpj = cnpj
        self.razaoSocial = razaoSocial
        self.nomeFantasia = nomeFantasia
        self.modalidade = modalidade
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.ddd = ddd
        self.telefone = telefone
        self.fax = fax
        self.enderecoEletronico = enderecoEletronico
        self.representante = representante
        self.cargoRepresentante = cargoRepresentante
        self.dataRegistroANS = dataRegistroANS
        pass