import pandas as pd
from models.lancamento import Lancamento

def inicio_extrato():
    # Obter todos os lançamentos
    lancamentos = Lancamento.listar_lancamentos()

    # Criar um DataFrame com os dados dos lançamentos
    data = [
        {
        'Data_Lancamento': lancamento.data_lancamento,
        'Tipo': lancamento.tipo_lancamento,
        'Conta': lancamento.conta.nome_conta,
        'Categoria': lancamento.categoria.nome_categoria,
        'Valor': lancamento.valor,
        'Descrição': lancamento.descricao,
        'Timestamp_Registro': lancamento._timestamp_registro
        } 
        for lancamento in lancamentos
        ]
    df = pd.DataFrame(data)
    # Ordenar o DataFrame por data de forma decrescente
    # df = df.sort_values(by='Data_Lancamento', ascending=False)
    
    # Exibir o DataFrame
    print("\nExtrato de Lançamentos:\n")
    print(df)
    
    # Pedir ao usuário para digitar qualquer coisa para retornar ao menu principal
    input("\nPressione qualquer tecla para voltar ao menu principal...")

