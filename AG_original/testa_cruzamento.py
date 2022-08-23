import populacao
import funcoes_auxiliares as aux
import matplotlib.pyplot as plt
import crossover    
#cria populacao
NV = 1
N = 2
n_bits = 16
X = populacao.cria_populacao(NV, N, n_bits)
limites = [[-100, 100], [-100, 100]]
valores = aux.converte_populacao(X, limites)
n_cortes = int(3)


#n of childrensss
n_children = 300
filhos = []

for j in range(30):
    for i in range(n_children):
        value = crossover.cruza_individuos(X[0], X[1], n_cortes)
        filhos.append(value[0])
        filhos.append(value[1])

childreans = aux.converte_populacao(filhos, limites)
filhos = []


#plot scarter from -100 to 100
plt.scatter([individuo[0] for individuo in childreans], [0 for individuo in childreans])
#plot scarter as red
plt.scatter([individuo[0] for individuo in valores], [0 for individuo in valores], color='red')
"""plt.xlim(limites[0])
plt.ylim(limites[1])"""

plt.show()

print(X)