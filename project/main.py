import random
import os

erros = 0
valores_sorteados = random.randrange(1, 100)
valores_jogador = int(input("Insira um valor de 1 até 100: "))
while (valores_sorteados != valores_jogador):
    os.system('cls')
    if (valores_jogador < valores_sorteados):
        print("Seu valor é menor")
    elif (valores_jogador > valores_sorteados):
        print("Seu valor é maior")
    erros += 1
    valores_jogador = int(input("Insira mais um valor de 1 até 100: "))
print(f"Seu numero {valores_jogador} está certo em tentativas {erros+1}")
