import os
import time

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def carregando():
    print("Carregando próxima operação", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    time.sleep(0.5)
    print()  # pula linha

while True:
    try:
        primeiro_numero = int(input("Digite o primeiro número: "))
        operador = input("Digite o operador: ")
        segundo_numero = int(input("Digite o segundo número: "))

        if operador == "+":
            resultado = primeiro_numero + segundo_numero
            print(f"{primeiro_numero} + {segundo_numero} = {resultado}")

        elif operador == "-":
            resultado = primeiro_numero - segundo_numero
            print(f"{primeiro_numero} - {segundo_numero} = {resultado}")

        elif operador == "*":
            resultado = primeiro_numero * segundo_numero
            print(f"{primeiro_numero} * {segundo_numero} = {resultado}")

        elif operador == "/":
            if segundo_numero == 0:
                print("Erro: divisão por zero, paizão!")
            else:
                resultado = primeiro_numero / segundo_numero
                print(f"{primeiro_numero} / {segundo_numero} = {resultado}")

        else:
            print("Erro pappi, operador inválido!")

    except ValueError:
        print("É só número, paizão. Tenta de novo aí.")

    deseja_continuar = input("Deseja continuar? (S/N): ").strip().upper()
    if deseja_continuar == "S":
        carregando()
        limpar_terminal()
    else:
        print("Encerrando...")
        break
