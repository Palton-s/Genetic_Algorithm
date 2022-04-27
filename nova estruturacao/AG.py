# importa os modulos necessarios
import crossover as cross
import mutacao as m
import populacao
import avaliacao as av
import funcoes_auxiliares as aux
import numpy as np

# define informações da população
NV = 2 # número de variáveis
N = 1000 # numero de individuos
n_bits = 16 # número de bits por variável em cada indivíduo
percent_elite = 0.25 # percentual dos melhores indivíduos
n_cortes_no_cruzamento = 2 # número de pontos de corte no cruzamento
n_geracoes = 100 # número de gerações
taxa_de_mutacao = 0.1 # taxa de mutação
intensidade_da_mutacao = 0.3 # intensidade da mutação

# inicia a população
X = populacao.cria_populacao(NV, N, n_bits)
for i in range(n_geracoes):
    # avalia a população
    Y = av.avaliacao(X)
    # ordena a população e as avaliações
    X,Y = aux.ordena(X,Y)
    # imprime a avaliação do melhor indivíduo
    print(i, Y[-1])

    ## inicia o processo de seleção
    # seleciona os indivíduos elite
    elite = X[-int(N*percent_elite):]
    # seleciona melhores indivíduos (50%)
    melhores = X[-int(N*0.5):]
    # realiza cruzamentos entre esses indivíduos, retornando os filhos
    filhos = cross.cruza_populacao(melhores, n_cortes_no_cruzamento)
    # atribui os filhos à população junto com os indivíduos elite
    X = aux.atribui(X, filhos, elite)
    # realiza mutações nos indivíduos
    X = m.mut_pop(X, taxa_de_mutacao, intensidade_da_mutacao)
    


