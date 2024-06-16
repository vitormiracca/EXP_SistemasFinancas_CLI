from controller.conta_dao import ContaController


class Conta:

    _contas = {} # {'Conta Corrente':[object1, object2]}

    def __init__(self, nome_conta:str, tipo_conta:str, dia_fechamento=None, dia_vencimento=None):
        self._nome_conta = nome_conta
        self._tipo_conta = tipo_conta
        self._dia_fechamentoo = dia_fechamento
        self._dia_vencimento = dia_vencimento
        if tipo_conta not in Conta._contas:
            Conta._contas[tipo_conta] = []
        Conta._contas[tipo_conta].append(self)        

    @property
    def nome_conta(self):
        return self._nome_conta
    @nome_conta.setter
    def nome_conta(self, nome_conta):
        self._nome_conta = nome_conta

    @property
    def tipo_conta(self):
        return self._tipo_conta

    @property
    def dia_fechamento(self):
        return self._dia_fechamento
    @dia_fechamento.setter
    def dia_fechamento(self, dia_fechamento):
        self._dia_fechamento = dia_fechamento

    @property
    def dia_vencimento(self):
        return self._dia_vencimento
    @dia_vencimento.setter
    def dia_vencimento(self, dia_vencimento):
        self._dia_vencimento = dia_vencimento

    # @classmethod  
    # def listar_contas(cls, tipo_conta=None):
    #     if (tipo_conta):
    #         return cls._contas[tipo_conta]
    #     else:
    #         lista_unica = [conta for sublista_conta in cls._contas.values() for conta in sublista_conta]
    #         return lista_unica
        
    @staticmethod
    def listar_contas():
        conta_controller = ContaController()
        return conta_controller.listar_contas()

    def __str__(self):
        return self._nome_conta

    def __repr__(self):
        return self.__str__()