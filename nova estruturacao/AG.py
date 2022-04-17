import crossover
import mutacao
import populacao
import avaliacao as av
import funcoes_auxiliares as aux

# define informações da população
NV = 3
N = 40
n_bits = 1024
percent_elite = 0.25
n_cortes_no_cruzamento = 8
n_geracoes = 100
taxa_de_mutacao = 0.1
intensidade_da_mutacao = 0.1

# inicia a população
X = populacao.cria_populacao(NV, N, n_bits)
for i in range(n_geracoes):
    # avalia a população
    Y = av.avaliacao(X)
    # ordena a população
    X,Y = aux.ordena(X,Y)
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

#print(X)
print(Y)
#print(elite)


