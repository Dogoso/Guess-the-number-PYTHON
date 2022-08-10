import game

def main():
    print("Menu: (1) Jogar")
    option = int(input("Digite a opção:"))
    if(option==1):
        game.start()


if(__name__ == "__main__"):
    main()