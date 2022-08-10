import random

def start():
    print("************")
    print("Hello world!")
    print("************")
    numero_sorteado = random.randrange(0, 11)
    max_cont = 3
    for cont in range(0, max_cont):
        print("Rodada | {}".format(cont + 1))
        valor = input("Escolha um número (0-10): ")
        if int(valor) > 10 or int(valor) < 0:
            print("Número inválido!")
            continue
        if int(valor) == numero_sorteado:
            print("Parabénsssssss você acertou!")
            break
        else:
            print("Errado!")
    print("Fim do programa")

if(__name__ == "__main__"):
    start()