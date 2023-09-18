import subprocess
import sys
from os import system
from time import sleep

try:
    import msvcrt
    import math
        
except ImportError:
    system('cls')

    g = "\033[92m"
    r = "\033[91m"
    end = "\033[0m"

    def install(packages):
        for package in packages:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"{g}{package} foi instalado com sucesso!{end}")
            except subprocess.CalledProcessError as err:
                print(f"{r}Erro ao instalar {package}.{end}")
                print(f"Erro: {err}")

    install(['math'])

wcmd = 55 # Largura terminal (width)
hcmd = 30 # Altura terminal (height)

wcmd2 = 75
hcmd2 = 33

wcmd3 = 40
hcmd3 = 5

wcmd4 = 33
hcmd4 = 10

def size(width=wcmd, height=hcmd):
    # Configura o tamanho do terminal
    cmd = f'mode {width}, {height}'
    system(cmd)
    
def size2(width=wcmd2, height=hcmd2):
    cmd = f'mode {width}, {height}'
    system(cmd)

def size3(width=wcmd3, height=hcmd3):
    cmd = f'mode {width}, {height}'
    system(cmd)
    
def size4(width=wcmd4, height=hcmd4):
    cmd = f'mode {width}, {height}'
    system(cmd)

def center(content, total_width=wcmd):
    #Centraliza o conteúdo baseado na largura fornecida.
    left_padding = (total_width - len(content)) // 2
    return " " * left_padding + content

def center2(content, total_width=wcmd2):
    left_padding = (total_width - len(content)) // 2
    return " " * left_padding + content

def center3(content, total_width=wcmd3):
    left_padding = (total_width - len(content)) // 2
    return " " * left_padding + content

def center4(content, total_width=wcmd4):
    left_padding = (total_width - len(content)) // 2
    return " " * left_padding + content

def header():
    # Exibe o cabeçalho da calculadora
    header_content = [
        "*"*39,
        "*"*11 + " CALCULADORA 2.0 " + "*"*11,
        "*"*11 + " --------------- " + "*"*11,
        "*"*11 + "    DS NOT 23    " + "*"*11,
        "*"*11 + "     COTUCA      " + "*"*11,
        "*"*11 + " --------------- " + "*"*11,
        "*"*11 + "   by Endrew     " + "*"*11,
        "*"*39
    ]
    for line in header_content:
        print(center(line))

def calculator():
    # Exibe a interface da calculadora
    calc_display = [
        center("-"*25),
        center("|" + " "*23 + "|"),
        center("|" + " "*23 + "|"),
        center("|" + " "*23 + "|"),
        center("-"*25),
        center("| ¹/× |  x² | ²√× |  ÷  |"),
        center("-"*25),
        center("|  7  |  8  |  9  |  ×  |"),
        center("-"*25),
        center("|  4  |  5  |  6  |  -  |"),
        center("-"*25),
        center("|  1  |  2  |  3  |  +  |"),
        center("-"*25),
        center("|  C  |  0  |  .  |  =  |"),
        center("-"*25)
    ]
    for line in calc_display:
        print(line)

def press():
    # Espera até que o usuário pressione 'Enter'
    while True:
        key = msvcrt.getch()
        if key == b'\r':
            break
        
def display(options, current_index):
    # Exibe o menu com as opções
    system('cls')
    print("\n")
    print(center3(f"{nome}, está correto?"))
    for index, option in enumerate(options):
        if index == current_index:
            print(center3(f"> {option} <"))  # Destaca a opção atual
        else:
            print(center3(option))

def YoN(options):
    # Permite ao usuário navegar pelo menu usando as setas do teclado
    current_index = 0
    while True:
        display(options, current_index)
        key = msvcrt.getch()
        
        # Setas para cima e para baixo
        if key == b'\xe0':
            arrow_key = msvcrt.getch()
            
            if arrow_key == b'H':
                current_index -= 1
                if current_index < 0:
                    current_index = len(options) - 1
            elif arrow_key == b'P':
                current_index += 1
                if current_index >= len(options):
                    current_index = 0
        
        # Tecla Enter
        elif key == b'\r':
            return current_index
        
options = ["Sim", "Não"]

def name():
    while True:
        system('cls')
        print("\n")
        print(center3("Digite seu nome, por favor"))
        n = input("\t> ").strip()
        if not n:
            system('cls')
            print("\n")
            print(center3("Seu nome não pode estar vazio!"))
            sleep(2)
            system('cls')
        else:
            break
    return n

def display2(options, current_index):
    system('cls')
    print("\n")
    print(center2("*"*59))
    print(center2(f"*** Olá {nome}! Seja bem-vindo(a) a minha calculadora :) ***"))
    print(center2("*"*59))
    print("\n")
    print(center2("Qual operação deseja fazer?"))
    for index, option in enumerate(options):
        print("\n")
        if index == current_index:
            print(center2(f"> {option} <"))
        else:
            print(center2(option))

def calc(options2):
    current_index = 0
    while True:
        display2(options2, current_index)
        key = msvcrt.getch()
        
        if key == b'\xe0':
            arrow_key = msvcrt.getch()
            
            if arrow_key == b'H':
                current_index -= 1
                if current_index < 0:
                    current_index = len(options2) - 1
            elif arrow_key == b'P':
                current_index += 1
                if current_index >= len(options2):
                    current_index = 0
        
        elif key == b'\r':
            return current_index
        
options2 = ["Adição (+)", "Subtração (-)","Multiplicação(×)", "Divisão (÷)","Porcentagem (%)", "Raiz quadrada (²√x)"]
    
def numbers():
    size4()
    while True:
        try:
            system('cls')
            print("\n"*2)
            print(center4("Digite um número"))
            print("\n")
            n1 = float (input("\t> "))
            
            system('cls')
            
            print("\n"*2)
            print(center4("Digite outro número"))
            print("\n")
            n2 = float (input("\t> "))
            return n1,n2
        except ValueError as err:
            print("\n"*2)
            print (center4("Digite um número válido!"))
            sleep(3)

if __name__ == "__main__":
    system('cls') # Chama o cls, para limpar a tela
    size() # chama a função size que define o tamanho da tela do cmd
    print("\n")# Insere uma quebra de linha
    header() # Chama a função header que mostra o cabeçalho
    
    # -------------------------------------------------------------- #
    
    print("\n")
    calculator() # Chama a função calculator que mostra a calculadora
    
    # -------------------------------------------------------------- #
    
    print("\n")
    print(center("Pressione Enter para continuar..."))
    press() # Chama a função press que espera o usuário pressionar a tecla enter para continuar

    # -------------------------------------------------------------- #
    size3()
    while True:
        nome = name() # Chama a função name que pergunta qual o nome
        selected = YoN(options) # Mostra o menu com as opções
        if options[selected] == "Sim":
            break # Se a resposta for 'Sim', sai do loop, se não continua perguntando
    
    # -------------------------------------------------------------- #
    
    system('cls')
    size2()
    print("\n")
    selected2 = calc(options2)
    print("\n")
    print(center2("*"*33))
    print(center2(f"* Você escolheu a {options2[selected2]} *"))
    print(center2("*"*33))
    sleep(2)

    # -------------------------------------------------------------- #
    
    if selected2 == 0:  # Adição
        n1, n2 = numbers()
        result = n1 + n2
        system('cls')
        print("\n"*2)
        print(center4("- Resultado da conta -"))
        print(center4(f"{n1} + {n2} = {result}"))
        print("\n"*2)
        
    elif selected2 == 1:  # Subtração
        n1, n2 = numbers()
        result = n1 - n2
        system('cls')
        print("\n"*2)
        print(center4("- Resultado da conta -"))
        print(center4(f"{n1} - {n2} = {result}"))
        print("\n"*2)

    elif selected2 == 2:  # Multiplicação
        n1, n2 = numbers()
        result = n1 * n2
        system('cls')
        print("\n"*2)
        print(center4("- Resultado da conta -"))
        print(center4(f"{n1} × {n2} = {result}"))
        print("\n"*2)

    elif selected2 == 3:  # Divisão
        n1, n2 = numbers()
        if n2 == 0:
            print(center4("Erro: Divisão por zero!"))
        else:
            result = n1 / n2
            system('cls')
            print("\n"*2)
            print(center4("- Resultado da conta -"))
            print(center4(f"{n1} ÷ {n2} = {result:.2f}"))
            print("\n"*2)

    elif selected2 == 4:  # Porcentagem
        n1, n2 = numbers()
        result = (n1 * n2) / 100
        system('cls')
        print("\n"*2)
        print(center4("- Resultado da conta -"))
        print(center4(f"{n2}% de {n1} é {result}"))
        print("\n"*2)

    elif selected2 == 5:  # Raiz quadrada
        size4()
        print("\n"*3)
        n1 = float(input(center4("Digite um número: ")))
        result = n1 ** 0.5
        system('cls')
        print("\n"*2)
        print(center4("- Resultado da conta -"))
        print(center4(f"Raiz quadrada de {n1} é {result:.2f}"))
        print("\n"*2)
