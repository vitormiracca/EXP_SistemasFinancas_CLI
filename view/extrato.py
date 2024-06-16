import pandas as pd

from controller.lancamento_dao import LancamentoController

def inicio_extrato():
    dao = LancamentoController()
    lancamentos = dao.listar_lancamentos()
    df = pd.DataFrame(lancamentos)
    # Ordenar o DataFrame por data de forma decrescente
    df = df.sort_values(by='timestamp_registro', ascending=False)
    # Exibir o DataFrame
    print("\nExtrato de Lançamentos:\n")
    print(df)
    
    # Pedir ao usuário para digitar qualquer coisa para retornar ao menu principal
    input("\nPressione qualquer tecla para voltar ao menu principal...")

