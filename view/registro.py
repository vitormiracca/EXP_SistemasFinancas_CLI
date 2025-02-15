from datetime import date
from controller.categoria_dao import CategoriaController
from controller.conta_dao import ContaController
from controller.lancamento_dao import LancamentoController
from models.categoria import Categoria
from models.conta import Conta
from models.lancamento import Lancamento
from view.clear import clear_terminal

def display_registro_lancamento():
    mensagem = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━              
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        _                                                _        
       | |                                              | |       
       | |     __ _ _ __   ___ __ _ _ __ ___   ___ _ __ | |_ ___  
       | |    / _` | '_ \ / __/ _` | '_ ` _ \ / _ \ '_ \| __/ _ \ 
       | |___| (_| | | | | (_| (_| | | | | | |  __/ | | | || (_) |       
       |______\__,_|_| |_|\___\__,_|_| |_| |_|\___|_| |_|\__\___/ 
                           )_)                                    
                                                                                                             
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                              

Por favor, insira as informações do lançamento...
            """
    print(mensagem)

def display_registro_conta():
    mensagem = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━           
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         _____            _        
        / ____|          | |       
       | |     ___  _ __ | |_ __ _ 
       | |    / _ \| '_ \| __/ _` |
       | |___| (_) | | | | || (_| |
        \_____\___/|_| |_|\__\__,_|
                                   
                                                                                                              
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      

Por favor, insira as informações da Conta...
            """
    print(mensagem)

def display_registro_categoria():
    mensagem = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━            
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         _____      _                        _       
        / ____|    | |                      (_)      
       | |     __ _| |_ ___  __ _  ___  _ __ _  __ _ 
       | |    / _` | __/ _ \/ _` |/ _ \| '__| |/ _` |
       | |___| (_| | ||  __/ (_| | (_) | |  | | (_| |
        \_____\__,_|\__\___|\__, |\___/|_|  |_|\__,_|
                             __/ |                   
                            |___/                                                                                                 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    

Por favor, insira as informações da Categoria...
            """
    print(mensagem)

def listar_opcoes(opcoes, exclude:list = None):
    '''
    Função para enumerar uma lista de opções e printá-las na tela, inciando com 1.
    '''
    if (exclude):
        for idx, opcao in enumerate(opcoes, 1):
            if (idx in exclude):
                pass
            else:
                print(f"{idx} - {opcao}")
    else:
        for idx, opcao in enumerate(opcoes, 1):
            print(f"{idx} - {opcao}")

def registrar_lancamento():
    '''
    Descrição:
        - Função para o registro de lançamentos de Receitas e Despesas, guiando o usuário.
    
    '''
    clear_terminal()
    display_registro_lancamento()    
    # Perguntar a data do lançamento
    while True:
        data_input = input("# Data do Lançamento (YYYY-MM-DD): ")
        try:
            data_lancamento = date.fromisoformat(data_input)
            break
        except ValueError:
            print("Data inválida. Por favor, insira no formato YYYY-MM-DD.")

    # Perguntar o tipo de lançamento
    while True:
        print("\n# Tipo de Lançamento:")
        tipos_lancamento = ['Receita', 'Despesa', 'Transferência Entre Contas']
        listar_opcoes(tipos_lancamento)
        try:
            tipo_lancamento_idx = int(input()) -1
            if tipo_lancamento_idx not in range(len(tipos_lancamento)):
                raise IndexError
            tipo_lancamento = tipos_lancamento[tipo_lancamento_idx]
            break
        except (ValueError, IndexError):
            print("Opção inválida. Por favor, escolha um número da lista.")

    # Perguntar a conta
    while True:
        print("\n# Contas Disponíveis:")
        contas = Conta.listar_contas()
        listar_opcoes([conta['nome_conta'] for conta in contas])
        try:
            conta_idx = int(input()) - 1
            if conta_idx not in range(len(contas)):
                raise IndexError
            conta = contas[conta_idx]
            break
        except (ValueError, IndexError):
            print("Opção inválida. Por favor, escolha um número da lista.")

    # Perguntar a categoria
    while True:
        print("\n# Categorias Disponíveis:")
        categorias = Categoria.listar_categorias(tipo_lancamento=tipo_lancamento)
        listar_opcoes([categoria['nome_categoria'] for categoria in categorias])
        try:
            categoria_idx = int(input()) -1
            if categoria_idx not in range(len(categorias)):
                raise IndexError
            categoria = categorias[categoria_idx]
            break
        except (ValueError, IndexError):
            print("Opção inválida. Por favor, escolha um número da lista.")

    # Perguntar o valor
    while True:
        try:
            valor = float(input("\nValor: "))
            break
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")

    # Perguntar a descrição
    descricao = input("\nDescrição: ")

    if tipo_lancamento == 'Transferência Entre Contas':
        # Perguntar a conta de destino
        while True:
            print("\n# Contas Destino Disponíveis:")
            contas_destino = Conta.listar_contas()
            listar_opcoes([conta['nome_conta'] for conta in contas_destino], exclude=[conta_idx+1])
            try:
                conta_destino_idx = int(input()) - 1
                if conta_destino_idx not in range(len(contas_destino)):
                    raise IndexError
                conta_destino = contas_destino[conta_destino_idx]
                break
            except (ValueError, IndexError):
                print("Opção inválida. Por favor, escolha um número da lista.")

        lancamento_controller = LancamentoController()
        # Registrar lançamento negativo na conta de origem
        lancamento_controller.criar_lancamento(
            data_lancamento=data_lancamento,
            tipo_lancamento=tipo_lancamento,
            conta_id=conta['id'],
            categoria_id=categoria['id'],
            valor=-abs(valor),
            descricao=f"Transferência enviada de {conta['nome_conta']} para {conta_destino['nome_conta']}: {descricao}"
        )

        # Registrar lançamento positivo na conta de destino
        lancamento_controller.criar_lancamento(
            data_lancamento=data_lancamento,
            tipo_lancamento=tipo_lancamento,
            conta_id=conta_destino['id'],
            categoria_id=categoria['id'],
            valor=abs(valor),
            descricao=f"Transferência enviada de {conta['nome_conta']} para {conta_destino['nome_conta']}: {descricao}"
        )

        # # Registrar lançamento negativo na conta de origem
        # Lancamento(
        #     data_lancamento=data_lancamento,
        #     tipo_lancamento=tipo_lancamento,
        #     conta=conta,
        #     categoria=categoria,
        #     valor=-abs(valor),
        #     descricao=f"Transferência enviada de {conta} para {conta_destino }: {descricao}"
        # )

        # # Registrar lançamento positivo na conta de destino
        # Lancamento(
        #     data_lancamento=data_lancamento,
        #     tipo_lancamento=tipo_lancamento,
        #     conta=conta_destino,
        #     categoria=categoria,
        #     valor=abs(valor),
        #     descricao=f"Transferência enviada de {conta} para {conta_destino }: {descricao}"
        # )

        print("\nTransferência registrada com sucesso!")
    else:
        lancamento_controller = LancamentoController()
        lancamento_controller.criar_lancamento(
            data_lancamento=data_lancamento, 
            tipo_lancamento=tipo_lancamento, 
            conta_id=conta['id'], 
            categoria_id=categoria['id'], 
            valor= abs(valor) if tipo_lancamento=='Receita' else -abs(valor), 
            descricao=descricao
            )
        # Lancamento(
        #     data_lancamento=data_lancamento,
        #     tipo_lancamento=tipo_lancamento,
        #     conta=conta,
        #     categoria=categoria,
        #     valor=valor,
        #     descricao=descricao
        # )

        print("\nLançamento registrado com sucesso!")

def registrar_conta():
    '''
    Descrição:
        - Função para registrar uma nova conta.
    '''
    clear_terminal()
    display_registro_conta()
    nome_conta = input("# Nome da Conta: ")
    tipos_conta = ['Conta Corrente', 'Conta de Crédito', 'Conta de Investimento', 'Vale Benefícios']
    listar_opcoes(tipos_conta)
    while True:
        try:
            tipo_conta_idx = int(input()) - 1
            if tipo_conta_idx not in range(len(tipos_conta)):
                raise IndexError
            tipo_conta = tipos_conta[tipo_conta_idx]
            if (tipo_conta == 'Conta de Crédito'):
                dia_vencimento = int(input('\n# Dia Vencimento da Fatura: '))
                dia_fechamento = int(input('\n# Dia Fechamento da Fatura: '))
            else:
                dia_vencimento = None
                dia_fechamento = None
            break
        except (ValueError, IndexError):
            print("Opção inválida. Por favor, escolha um número da lista.")

    conta_controller = ContaController()
    conta_controller.criar_conta(nome_conta=nome_conta, tipo_conta=tipo_conta, dia_vencimento=dia_vencimento, dia_fechamento=dia_fechamento)
    # ContaController.criar_conta(nome_conta, tipo_conta, dia_fechamento or None, dia_vencimento or None)
    # Conta(nome_conta, tipo_conta)
    print("\nConta registrada com sucesso!")

def registrar_categoria():
    '''
    Descrição:
        - Função para registrar uma nova categoria.
    '''
    clear_terminal()
    display_registro_categoria()
    tipos_lancamento = ['Receita', 'Despesa', 'Transferência Entre Contas']
    listar_opcoes(tipos_lancamento)
    while True:
        try:
            tipo_lancamento_idx = int(input()) -1
            # if tipo_lancamento_idx == 0:
            #     break
            if tipo_lancamento_idx not in range(len(tipos_lancamento)):
                raise IndexError
            tipo_lancamento = tipos_lancamento[tipo_lancamento_idx]
            break
        except (ValueError, IndexError):
            print("Opção inválida. Por favor, escolha um número da lista.")
    nome_categoria = input("# Nome da Categoria: ")
    categoria_controller = CategoriaController()
    categoria_controller.criar_categoria(tipo_lancamento, nome_categoria)
    # Categoria(tipo_lancamento, nome_categoria)
    print("\nCategoria registrada com sucesso!")

def inicio_registro():
    print("\n\n# Que tipo de registro você pretende fazer?")
    opcoes = ['Registrar Lançamento', 'Registrar Conta', 'Registrar Categoria']
    listar_opcoes(opcoes)
    opcoes_func = {
        1: registrar_lancamento,
        2: registrar_conta,
        3: registrar_categoria
    }
    while True:
        try:
            opcao_idx = int(input())
            if opcao_idx in opcoes_func:
                opcoes_func[opcao_idx]()
                break
            else:
                print("Opção inválida. Por favor, escolha um número da lista.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
