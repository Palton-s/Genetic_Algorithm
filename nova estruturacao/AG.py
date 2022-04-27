import crossover
import mutacao
import populacao
import avaliacao as av
import funcoes_auxiliares as aux
import numpy as np

# define informações da população
NV = 2 # número de variáveis
N = 1000 # numero de individuos
n_bits = 16 # número de bits por variável em cada indivíduo
percent_elite = 0.25 # percentual dos melhores indivíduos que serão conservados para a próxima geração
n_cortes_no_cruzamento = 2 # número de pontos de corte no cruzamento
n_geracoes = 100 # número de gerações
taxa_de_mutacao = 0.1 # taxa de mutação
intensidade_da_mutacao = 0.3 # intensidade da mutação

def GA(NV, N, n_bits, percent_elite, n_cortes_no_cruzamento, n_geracoes, taxa_de_mutacao, intensidade_da_mutacao):

    # inicia a população
    X = populacao.cria_populacao(NV, N, n_bits)
    # variavel com dados estatísticos de cada geração
    dados_geracao = []
    for i in range(n_geracoes):
        # avalia a população
        Y = av.avaliacao(X)
        # ordena a população
        X,Y = aux.ordena(X,Y)

        # se não estiver na última geração
        if i < n_geracoes-1:
            # seleciona os indivíduos elite
            elite = X[-int(N*percent_elite):]
            # seleciona melhores indivíduos (50%)
            melhores = X[-int(N*0.5):]
            # realiza cruzamentos entre esses indivíduos
            filhos = crossover.cruza_populacao(melhores, n_cortes_no_cruzamento)
            # atribui os filhos à população
            X = aux.atribui(X, filhos, elite)
            # realiza mutações nos indivíduos
            X = mutacao.mutacao_populacao(X, taxa_de_mutacao, intensidade_da_mutacao)

        print(i, Y[-1])
        # geração / avaliação média dos indivíduos / melhor avaliação
        dados_geracao.append([i, np.mean(Y)])

    #print(X)
    #print(Y)
    return dados_geracao

print(GA(NV, N, n_bits, percent_elite, n_cortes_no_cruzamento, n_geracoes, taxa_de_mutacao, intensidade_da_mutacao))


