import random

prefixos = ["Zan", "Mor", "El", "Thar", "Gal",]
sufixos = ["dor", "ion", "mir", "thas", "wyn",]

def gerar_nome():

    return random.choice(prefixos) + random.choice(sufixos)

def main():
    print("Seu nome fantástico é:", gerar_nome())

if __name__ == "__main__":
    main()