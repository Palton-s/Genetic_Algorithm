import random

def crossover(cromossomo1, cromossomo2, n_cortes):
    # pega o numero de bits do cromossomo
    n_bits = len(cromossomo1)
    # escolhe aleatoriamente os cortes
    crossover_points = random.sample(range(0, n_bits), n_cortes)
    # ordena os cortes
    crossover_points.sort()
    # gera com cromossomo 1 como uma lista de bits todos zerados
    cromossomo_filho_1 = cromossomo1.copy()
    # gera com cromossomo 2 como uma lista de bits todos zerados
    cromossomo_filho_2 = cromossomo2.copy()
    # executa o crossover
    for i in range(len(crossover_points)-1):
        # pega o número de cortes
        if i % 2 == 0:
            # como os filhos são clones dos respectivos pais, basta alterar os grupos pares de bits
            # assim se i for par, 
            # pega o bit do pai 2 e coloca no filho 1
            # e pega o bit do pai 1 e coloca no filho 2
            aux1 = cromossomo1[crossover_points[i]:crossover_points[i+1]].copy()
            aux2 = cromossomo2[crossover_points[i]:crossover_points[i+1]].copy()
            cromossomo_filho_1[crossover_points[i]:crossover_points[i+1]] = aux2
            cromossomo_filho_2[crossover_points[i]:crossover_points[i+1]] = aux1
    # retorna os cromossomos filhos
    return cromossomo_filho_1, cromossomo_filho_2

def seleciona_pares(melhores):
    # seleciona os pares de indivíduos
    # para a próxima geração
    # seleciona aleatoriamente
    # os indivíduos
    pares = random.sample(melhores, 2)
    # retorna os pares
    return pares

def cruza_populacao(melhores, n_cortes):
    # resgata o número de cruzamentos
    n_cruzamentos = len(melhores)
    # inicia a população de filhos
    filhos = []
    # para cada cruzamento
    for i in range(n_cruzamentos):
        # seleciona os pares de indivíduos
        pares = seleciona_pares(melhores)
        n_variaveis = len(pares[0])
        variaveis = []
        # para cada variavel
        filho_1 = []
        filho_2 = []
        for j in range(n_variaveis):
            variavel_filho1 = []
            variavel_filho2 = []
            # realiza o crossover das suas variáveis
            variavel_filho1, variavel_filho2 = crossover(pares[0][j], pares[1][j], n_cortes)
            # adiciona a variavel ao novo indivíduo
            filho_1.append(variavel_filho1)
            filho_2.append(variavel_filho2)
        # adiciona os filhos na população de filhos
        filhos.append(filho_1)
        filhos.append(filho_2)
    # retorna a população de filhos
    return filhos

populacao = [[[1,1,1,1,1,1,1,1]], [[0,0,0,0,0,0,0,0]]]
cruzamento = cruza_populacao(populacao, 2)

print(cruzamento)