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
<<<<<<< Updated upstream
N = 1000 # numero de individuos
n_bits = 16 # número de bits por variável em cada indivíduo
percent_elite = 0.25 # percentual dos melhores indivíduos
=======
N = 200 # numero de individuos
n_bits = 32 # número de bits por variável em cada indivíduo
percent_elite = 0.1 # percentual dos melhores indivíduos que serão conservados para a próxima geração
>>>>>>> Stashed changes
n_cortes_no_cruzamento = 2 # número de pontos de corte no cruzamento
n_geracoes = 50 # número de gerações
taxa_de_mutacao = 0.05 # taxa de mutação
intensidade_da_mutacao = 0.05 # intensidade da mutação

<<<<<<< Updated upstream
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
    
=======
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
        #realiza mutação nos filhos
        filhos = mutacao.mutacao_populacao(filhos, taxa_de_mutacao, intensidade_da_mutacao)
        # atribui os filhos à população
        X = aux.atribui(X, filhos, elite)
        #print(i, Y[-1])
        # geração / avaliação média dos indivíduos / melhor avaliação
        #dados_geracao.append([i, np.mean(Y)])
        dados_geracao.append([i,np.mean(Y[-50:])])
   



    return dados_geracao

>>>>>>> Stashed changes

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