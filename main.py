
def menu():
    clases = ["1. Arqueiro", "2. Feiticeiro", "3. Cavaleiro"]
    for item in clases:
        print(item)

def escolher_arco():
    arcos = ["1. arco de fogo", "2. arco de gelo", "3. arco encantado"]
    for item in arcos:
        print(item)

def escolher_feitico():
    feiticos = ["1. atordoamento", "2. envenenamento", "3. invocar zumbies"]
    for item in feiticos:
        print(item)

def escolher_cavalo():
    cavalos = ["1. cavalo zumbie", "2. cavalo sombrio", "3. cavalo nautico"]
    for item in cavalos:
        print(item)


print("----------------")
print("| RPG INICIADO |")
print("________________")
print()



print("Escolha uma das clases a seguir: ")

menu()

print()

escolher_clase = int(input("Escolher: "))

clases_printar = ["1. Arqueiro", "2. Feiticeiro", "3. Cavaleiro"]

if escolher_clase == 1:
    print("Voce escolheu a clase: {}".format(clases_printar[0]))
    print()

    print("Escolha uma arma de arquearia:")
    arcos_printar = ["1. arco de fogo", "2. arco de gelo", "3. arco encantado"]
    escolher_arco()
    print()
    escolher_arco = int(input("Escolher: "))

    if escolher_arco == 1:
        print("Voce escolheu o arco de: {} ".format(arcos_printar[0]))

    elif escolher_arco == 2:
        print("Voce escolheu o arco de: {}".format(arcos_printar[1]))

    elif escolher_arco == 3:
        print("Voce escolheu o arco de: {}".format(arcos_printar[2]))




elif escolher_clase == 2:
    print("Voce escolheu a clase: {}".format(clases_printar[1]))
    print()

    print("Escolha um tipo de feitico:")
    feiticos_printar = ["1. atordoamento", "2. envenenamento", "3. invocar zumbies"]
    escolher_feitico()
    print()
    escolher_feitico = int(input("Escolher: "))

    if  escolher_feitico == 1:
        print("Voce escolheu o feitico de: {}".format(feiticos_printar[0]))

    elif escolher_feitico == 2:
        print("Voce escolheu o feitico de: {}".format(feiticos_printar[1]))

    elif escolher_feitico == 3:
        print("Voce escolheu o feitico de: {}".format(feiticos_printar[2]))




elif escolher_clase == 3:
    print("Voce escolheu a clase: {}".format(clases_printar[2]))
    print()

    print("Escolha um tipo de cavalo:")
    cavalos_printar = ["1. cavalo zumbie", "2. cavalo sombrio", "3. cavalo nautico"]
    escolher_cavalo()
    print()
    escolher_cavalo = int(input("Escolher: "))

    if escolher_cavalo == 1:
        print("Voce escolheu o cavalo: {}".format(cavalos_printar[0]))

    elif escolher_cavalo == 2:
        print("Voce escolheu o cavalo: {}".format(cavalos_printar[1]))

    elif escolher_cavalo == 3:
        print("Voce escolheu o cavalo: {}".format(cavalos_printar[2]))

