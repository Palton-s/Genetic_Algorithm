from turtle import color
import crossover
import mutacao
import populacao
import avaliacao as av
import funcoes_auxiliares as aux
import numpy as np
import matplotlib.pyplot as plt

# define informações da população
NV = 2 # número de variáveis
N = 50 # numero de individuos
n_bits = 32 # número de bits por variável em cada indivíduo
percent_elite = 0.1 # percentual dos melhores indivíduos que serão conservados para a próxima geração
n_cortes_no_cruzamento = 5 # número de pontos de corte no cruzamento
n_geracoes = 50 # número de gerações
taxa_de_mutacao = 0.2 # taxa de mutação
intensidade_da_mutacao = 0.3 # intensidade da mutação

def GA(NV, N, n_bits, percent_elite, n_cortes_no_cruzamento, n_geracoes, taxa_de_mutacao, intensidade_da_mutacao):

    # inicia a população
    X = populacao.cria_populacao(NV, N, n_bits)
    # variavel com dados estatísticos de cada geração
    dados_geracao = []
    avaliacoes = []
    for i in range(n_geracoes):
        # avalia a população
        Y = av.avaliacao(X)
        # ordena a população
        X,Y = aux.ordena(X,Y)
        # seleciona os indivíduos elite
        elite = X[-int(N*percent_elite):]
        # seleciona melhores indivíduos
        melhores = crossover.roleta(X,Y,0.5)
        # realiza cruzamentos entre esses indivíduos
        filhos = crossover.cruza_populacao(melhores, n_cortes_no_cruzamento)
        if i != n_geracoes-1:
            #realiza mutação nos filhos
            filhos = mutacao.mutacao_populacao(filhos, taxa_de_mutacao, intensidade_da_mutacao)
        # atribui os filhos à população
        X = aux.atribui(X, filhos, elite)
        #print(i, Y[-1])
        # geração / avaliação média dos indivíduos / melhor avaliação
        #dados_geracao.append([i, np.mean(Y)])
        dados_geracao.append([i,np.mean(Y[-150:])])
    X, Y = aux.ordena(X, Y)
    return aux.converte_populacao(X[-int(N*0.3):], [-2, 2])




def plot_dados(dados_geracao):
    x = [i[0] for i in dados_geracao]
    y = [i[1] for i in dados_geracao]
    
    theta = np.linspace(0, 2*np.pi, 100)
    #radius = [0.33, 0.66, 0.98, 1.31, 1.64, 1.97]
    radius = []

    for i in range(len(radius)):
        plt.plot(radius[i]*np.cos(theta), radius[i]*np.sin(theta), label=str(i), color='black', linewidth=0.5)

    for i in range(len(x)):
        plt.scatter(x[i], y[i], s=5, c='black', alpha=0.2)


    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)

    plt.xlabel('x')
    plt.ylabel('y')


    plt.show()

dados__ = []
for i in range(100):
    dados_geracao = GA(NV, N, n_bits, percent_elite, n_cortes_no_cruzamento, n_geracoes, taxa_de_mutacao, intensidade_da_mutacao)
    for j in range(len(dados_geracao)):
        dados__.append(dados_geracao[j])
    print(i)
    

plot_dados(dados__)

