import os

def clear_terminal():
    # Verifica o sistema operacional e executa o comando correspondente
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')