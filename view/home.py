import sys
from view.clear import clear_terminal
from view.resumo_financeiro import Resumo_Financeiro
from view.extrato import inicio_extrato
from view.registro import inicio_registro



def sair():
    print("""
# Obrigado por utilziar o MyCashFlow APP...
# Em breve, novidades...
          """)
    clear_terminal()
    sys.exit()

def gera_logo() -> str:
    # o traço - é Tmplr
    # o MyCash é o Big
    mensagem = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━              
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  __  __            _____                 _       ______   _                    
 |  \/  |          / ____|               | |     |  ____| | |                   
 | \  / |  _   _  | |        __ _   ___  | |__   | |__    | |   ___   __      __
 | |\/| | | | | | | |       / _` | / __| | '_ \  |  __|   | |  / _ \  \ \ /\ / /
 | |  | | | |_| | | |____  | (_| | \__ \ | | | | | |      | | | (_) |  \ V  V / 
 |_|  |_|  \__, |  \_____|  \__,_| |___/ |_| |_| |_|      |_|  \___/    \_/\_/  
            __/ |              _____    _____       _                           
           |___/       /\     |  __ \  |  __ \     | |                          
                      /  \    | |__) | | |__) |   / __)                         
                     / /\ \   |  ___/  |  ___/    \__ \                         
                    / ____ \  | |      | |        (   /                         
                   /_/    \_\ |_|      |_|         |_|                          
                                                                                
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                   
            """
    return mensagem

def gera_funcionalidades() -> str:
    mensagem = """# FUNCIONALIDADES DISPONÍVEIS:

    1- RESUMO FINANCEIRO (DASHBOARD)

    2- REGISTRO (REGISTRAR LANÇAMENTOS, CONTAS E CATEGORIAS)

    3- EXTRATO

    4- SAIR DO APP

            """
    return mensagem
    
def display_home():
    clear_terminal()
    print(gera_logo())
    print(gera_funcionalidades())

def display_escolha_funcionalidade():
    mensagem = """# O que você quer fazer agora?: """
    print(mensagem, end=" ")

def funcoes() -> dict:
    return {
        1: Resumo_Financeiro.inicio_resumo,
        2: inicio_registro,
        3: inicio_extrato,
        4: sair
    }