import random

categorias = ["Mago", "Guerreiro", "Paladino", "Elfo", "Bardo"]
prefixos = ["Zan", "Mor", "El", "Thar", "Gal","No","As","Gin"]
sufixos = ["dor", "ion", "mir", "thas", "wyn","guerian","dotrix","deon"]

def gerar_nome():
    return random.choice(prefixos) + random.choice(sufixos)

def escolher_categoria():
    return random.choice(categorias)

def main():
    print("Seu nome fantástico é:", gerar_nome())
    print("você pertence a categoria:", escolher_categoria())

if __name__ == "__main__":
    main()