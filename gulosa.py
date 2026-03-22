mapa={
    'A':{'B': 5, 'C': 8},
    'B':{'D': 6, 'E': 10},
    'C':{'D': 6, 'G': 9, 'F': 12},
    'D':{'B': 6, 'C': 6},
    'E':{'H': 7, 'B': 10},
    'F':{'H': 5},
    'G':{'H': 5},
    'H':{}
    

}

estimativa={
    'A': 20,
    'B': 16,
    'C': 14,
    'D': 12,
    'E': 8,
    'F': 4,
    'G': 6,
    'H': 0
}
def gulosa(inicio, objetivo):
    atual = inicio
    caminho=[atual]

    while atual != objetivo:
        vizinhos = mapa[atual]
        if not vizinhos:
            return "Sem caminho"
        proximo = min(vizinhos, key=lambda x: estimativa[x])
        caminho.append(proximo)
        atual=proximo

    return caminho
print ("Gulosa: ", gulosa ('A', 'H'))