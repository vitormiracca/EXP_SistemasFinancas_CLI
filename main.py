from view import home as vw
from models.lancamento import Lancamento
from models.conta import Conta
from models.categoria import Categoria
import pandas as pd

#region Variaveis de Teste
tipos_lancamento = ['Receita', 'Despesa', 'Transferência Entre Contas']
categorias = {
    'Receita': ['Salário', 'Bônus', 'Vale Benefícios', 'Devedores', 'Resgates Investimento', 'Presentes'],
    'Despesa': ['Alimentação Fora', 'Supermercado', 'Tabacaria', 'Despesas com Carro', 'Saúde', 'Viagens', 'Estudo', 'Compras Pessoais'],
    'Transferência Entre Contas': ['Transferência']
}

contas = {'Nubank': 'Conta Corrente', 'NuCredito': 'Conta de Crédito', 'Ticket':'Vale Benefícios', 'Bradesco':'Conta Corrente', 'Bradesco Cartões': 'Conta de Crédito', 'NovaDax': 'Conta de Investimento','Ágora': 'Conta de Investimento'}
#endregion

# Instanciar Contas
for nome, tipo in contas.items():
    Conta(nome, tipo)

# Instanciar Categorias
for tipo, cats in categorias.items():
    for cat in cats:
        Categoria(tipo, cat)

def main():

    funcoes = vw.funcoes()

    while True:
        vw.display_home()
        vw.display_escolha_funcionalidade()
        try:
            escolha_user = int(input())
            if escolha_user in funcoes:
                funcoes[escolha_user]()
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()
