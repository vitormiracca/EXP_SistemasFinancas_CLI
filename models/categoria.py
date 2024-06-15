
class Categoria:

    _categorias = {}

    def __init__(self, tipo_lancamento, nome_categoria):
        self._tipo_lancamento = tipo_lancamento
        self._nome_categoria = nome_categoria
        if tipo_lancamento not in Categoria._categorias:
            Categoria._categorias[tipo_lancamento] = []
        Categoria._categorias[tipo_lancamento].append(self)

    @property
    def nome_categoria(self):
        return self._nome_categoria.title()
    @nome_categoria.setter
    def nome_categoria(self, nome: str):
        self._nome_categoria = nome

    @property
    def tipo_lancamento(self):
        return self._tipo_lancamento.title()
    @tipo_lancamento.setter
    def tipo_lancamento(self, nome: str):
        self._tipo_lancamento = nome

    @classmethod
    def listar_categorias(cls, tipo_lancamento=None):
        if tipo_lancamento:
            return cls._categorias.get(tipo_lancamento, [])
        else:
            return cls._categorias

    def __str__(self):
        return f"{self.nome_categoria}"

    def __repr__(self):
        return self.__str__()