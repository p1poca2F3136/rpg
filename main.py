import random

def menu():
    classes = ["1. Arqueiro", "2. Feiticeiro", "3. Cavaleiro"]
    for item in classes:
        print(item)

def escolher_arco():
    arcos = ["1. arco de fogo", "2. arco de gelo", "3. arco encantado"]
    for item in arcos:
        print(item)
    return arcos

def escolher_feitico():
    feiticos = ["1. atordoamento", "2. envenenamento", "3. invocar zumbies"]
    for item in feiticos:
        print(item)
    return feiticos

def escolher_cavalo():
    cavalos = ["1. cavalo zumbie", "2. cavalo sombrio", "3. cavalo nautico"]
    for item in cavalos:
        print(item)
    return cavalos

def batalha():
    jogador_vida = 100
    inimigo_vida = random.randint(50, 100)
    
    print("Batalha iniciada!")
    
    while jogador_vida > 0 and inimigo_vida > 0:
        print("Sua vida:", jogador_vida)
        print("Vida do inimigo:", inimigo_vida)
        print("1. Atacar")
        print("2. Fugir")
        escolha = int(input("Escolha sua ação: "))
        
        if escolha == 1:
            dano_jogador = random.randint(5, 20)
            dano_inimigo = random.randint(5, 15)
            
            jogador_vida -= dano_inimigo
            inimigo_vida -= dano_jogador
            
            print("Você causou {} de dano ao inimigo.".format(dano_jogador))
            print("O inimigo causou {} de dano a você.".format(dano_inimigo))
        elif escolha == 2:
            print("Você fugiu da batalha!")
            break
    
    if jogador_vida <= 0:
        print("Você foi derrotado!")
    elif inimigo_vida <= 0:
        print("Você venceu a batalha!")

print("----------------")
print("| RPG INICIADO |")
print("________________")
print()

print("Escolha uma das classes a seguir: ")
menu()
print()

escolher_classe = int(input("Escolher: "))

if escolher_classe == 1:
    print("Você escolheu a classe: Arqueiro")
    print("Escolha uma arma de arquearia:")
    arco_escolhido = escolher_arco()
    escolher_arco = int(input("Escolher: "))
    print("Você escolheu o arco de: {}".format(arco_escolhido[escolher_arco - 1]))
    batalha()
elif escolher_classe == 2:
    print("Você escolheu a classe: Feiticeiro")
    print("Escolha um tipo de feitiço:")
    feitico_escolhido = escolher_feitico()
    escolher_feitico = int(input("Escolher: "))
    print("Você escolheu o feitiço de: {}".format(feitico_escolhido[escolher_feitico - 1]))
    batalha()
elif escolher_classe == 3:
    print("Você escolheu a classe: Cavaleiro")
    print("Escolha um tipo de cavalo:")
    cavalo_escolhido = escolher_cavalo()
    escolher_cavalo = int(input("Escolher: "))
    print("Você escolheu o cavalo: {}".format(cavalo_escolhido[escolher_cavalo - 1]))
    batalha()
