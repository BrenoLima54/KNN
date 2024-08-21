def calcular_distancia(carteira1, carteira2): #Função que calcula a distância euclidiana entre duas carteiras
    return ((carteira1[0] - carteira2[0]) ** 2 + (carteira1[1] - carteira2[1]) ** 2 + (carteira1[2] - carteira2[2]) ** 2 + (carteira1[3] - carteira2[3]) ** 2) ** 0.5

def knn(K, nao_classificada, classificada): #Função que classifica os clientes não classificados
    for sem_class in nao_classificada:
        distancias=[]
        for classif in classificada:
            distancia = calcular_distancia(sem_class[2], classif[2])
            distancias.append((distancia, classif[1]))
        distancias.sort()
        vizinhos = distancias[:K]
        classificacoes = [vizinho[1] for vizinho in vizinhos]
        classificacao_mais_freq = max(set(classificacoes), key=classificacoes.count)
        sem_class[1] = classificacao_mais_freq
    return nao_classificada

resultado = knn(9, no_class, data) 
for item in resultado:
    print(item)