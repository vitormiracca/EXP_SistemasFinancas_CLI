from datetime import date, datetime
from models.categoria import Categoria
from models.conta import Conta

class Lancamento:
    _lancamentos = []

    def __init__(self, data_lancamento:date, tipo_lancamento, conta:Conta, categoria:Categoria, valor, descricao):
        self._data_lancamento = data_lancamento
        self._tipo_lancamento = tipo_lancamento
        self._conta = conta
        self.categoria = categoria
        self._valor = valor
        self._descricao = descricao
        self._timestamp_registro = datetime.now()
        Lancamento._lancamentos.append(self)

    @property
    def data_lancamento(self):
        return self._data_lancamento
    
    @property
    def tipo_lancamento(self):
        return self._tipo_lancamento

    @property
    def conta(self):
        return self._conta
    @conta.setter
    def conta(self, conta:Conta):
        self._conta = conta

    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, categoria:Categoria):
        self._categoria = categoria

    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def descricao(self):
        return self._descricao
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @classmethod
    def listar_lancamentos(cls):
        return cls._lancamentos

    def __str__(self):
        return f"{self.data} - {self.tipo_lancamento} - {self.valor} - {self.conta} - {self.categoria} - {self.descricao}"