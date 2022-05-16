import numpy as np
import funcoes_auxiliares as aux


def avaliacao(X, cor_1, cor_2, cor_alvo, precisao):
    n_individuos = len(X)
    Y = np.zeros(n_individuos)

    for i in range(n_individuos):
        # conta o número de bits iguais a 1
        percent_1 = X[i]
        percent_2 = precisao - percent_1
        # mistura as cores com base nos percentuais
        cor_final = aux.mistura_cores(cor_1, cor_2, percent_1, percent_2)
        # calcula a matiz da cor final
        h_final = aux.calcula_hsv(cor_final)[0]
        # calcula a matiz da cor alvo
        h_alvo = aux.calcula_hsv(cor_alvo)[0]
        #avaliacao é a distância circular entre h_final e h_alvo
        avaliacao = 1 - distancia_circular(h_final, h_alvo)

        Y[i] = avaliacao

    return Y

    

    
def distancia_circular(h_final, h_alvo):
    angle_1 = 2*np.pi*h_final
    angle_2 = 2*np.pi*h_alvo
    # calcular o menor angulo entre os dois angulos
    angle_min = min(abs(angle_1-angle_2), abs(angle_1-angle_2+2*np.pi), abs(angle_1-angle_2-2*np.pi))
    return angle_min/(2*np.pi)
