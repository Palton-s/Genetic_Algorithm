# importa os modulos necessarios
import crossover as cross
import mutacao as m
import populacao
import avaliacao as av
import funcoes_auxiliares as aux
import numpy as np
import matplotlib.pyplot as plt

# define informações da população
NV = 2 # número de variáveis
N = 1000 # numero de individuos
n_bits = 16 # número de bits por variável em cada indivíduo
percent_elite = 0.25 # percentual dos melhores indivíduos
n_cortes_no_cruzamento = 2 # número de pontos de corte no cruzamento
n_geracoes = 50 # número de gerações
taxa_de_mutacao = 0.05 # taxa de mutação
intensidade_da_mutacao = 0.05 # intensidade da mutação

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
    # seleciona os indivíduos
    melhores = cross.roleta(X,Y,0.5)
    # realiza cruzamentos entre esses indivíduos, retornando os filhos
    filhos = cross.cruza_populacao(melhores, n_cortes_no_cruzamento)
    # atribui os filhos à população junto com os indivíduos elite
    X = aux.atribui(X, filhos, elite)
    # realiza mutações nos indivíduos
    X = m.mut_pop(X, taxa_de_mutacao, intensidade_da_mutacao)
    

dados = []
for i in range(50):

    dado = GA(NV, N, n_bits, percent_elite, n_cortes_no_cruzamento, n_geracoes, taxa_de_mutacao, intensidade_da_mutacao)
    dados.append(dado)
    print(i)


# plot all geracoes


# plot geracoes
for geracao in dados:
    plt.plot([x[0] for x in geracao], [x[1] for x in geracao], label='geracao', linewidth=0.5, alpha=0.7)

plt.xlabel("Geração")
plt.ylabel("Avaliação Média")

plt.show()