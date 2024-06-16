from controller.lancamento_dao import LancamentoController
from controller.categoria_dao import CategoriaController
from controller.conta_dao import ContaController
from view import home as vw
from models.lancamento import Lancamento
from models.conta import Conta
from models.categoria import Categoria
import pandas as pd


dao = LancamentoController()
lancamentos = dao.listar_lancamentos()
print(pd.DataFrame(lancamentos))