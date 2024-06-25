from controller.lancamento_dao import LancamentoController
from controller.categoria_dao import CategoriaController
from controller.conta_dao import ContaController
from view import home as vw
from models.lancamento import Lancamento
from models.conta import Conta
from models.categoria import Categoria
import pandas as pd

contas = {
    1: 'Nubank',
    2: 'Nu Crédito',
    3: 'Bradesco',
    4: 'Ticket',
    5: 'Ágora',
    6: 'Bradesco Cartões',
    7: 'NovaDax'
}

categorias = {
    1: ('Transferência Entre Contas', 'Transferência'),
    2: ('Receita', 'Salário'),
    3: ('Receita', 'Bônus'),
    4: ('Receita', 'Vale Benefícios'),
    5: ('Receita', 'Devedores'),
    6: ('Receita', 'Presentes'),
    7: ('Despesa', 'Mercado'),
    8: ('Despesa', 'Refeições'),
    9: ('Despesa', 'Tabacaria'),
    10: ('Despesa', 'Estudo'),
    11: ('Despesa', 'Despesas com Carro'),
    12: ('Despesa', 'Viagens'),
    13: ('Despesa', 'Saúde'),
    14: ('Despesa', 'Compras'),
    15: ('Despesa', 'Assinaturas'),
    16: ('Despesa', 'Despesas Pessoais'),
    17: ('Despesas', 'Multas e Taxas'),
    18: ('Despesa', 'Uber'),
    19: ('Despesa', 'Outros')
}

########## Nubank Crédito ##########
lista_registros = [
    ['2024-05-28', 'Despesa', 6, 16, 65.0, 'Cabelereiro Sandro'],
    ['2024-05-03', 'Despesa', 6, 11, 374.56, 'Autoglass 2/3'],
    ['2024-05-12', 'Despesa', 6, 15, 19.9, 'Amazon Prime'],
    ['2024-05-30', 'Despesa', 6, 7, 25.6, 'Padoca'],
    ['2024-06-03', 'Despesa', 6, 17, 3, 'Adicional de atraso'],
    ['2024-06-08', 'Despesa', 6, 11, 52.9, 'Sem Parar'],
    ['2024-06-13', 'Despesa', 6, 10, 24.9, 'Kindle'],
    ['2024-06-15', 'Despesa', 6, 16, 65.0, 'Cabelereiro Sandro'],
    ['2024-06-17', 'Despesa', 6, 9, 45.5, 'Banca'],
    ['2024-06-18', 'Despesa', 6, 15, 16.99, 'Medium'],
    ['2024-06-19', 'Despesa', 6, 11, 264.42, 'Seguro 10/10'],
    ['2024-06-20', 'Despesa', 6, 19, 12.5, ''],

]

lancamento_dao = LancamentoController()

for r in lista_registros:
    lancamento_dao.criar_lancamento(
        data_lancamento=r[0],               #'2024-04-04'
        tipo_lancamento=r[1],               #'Receita', 'Despesa', 'Transferência Entre Contas'
        conta_id=r[2],                      # int      
        categoria_id=r[3],                  # int
        valor=-abs(r[4]) if r[1]=='Despesa' else r[4],                         # float
        descricao= r[5]                     # str
    )
    print("Registro criado com sucesso\n")


