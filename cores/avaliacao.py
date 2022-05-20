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
        h_final, l_final, s_final = aux.calcula_hls(cor_final)
        # calcula a matiz da cor alvo
        h_alvo, l_alvo, s_alvo = aux.calcula_hls(cor_alvo)
        #avaliacao é a distância circular entre h_final e h_alvo
        h_avaliacao = 2*(1 - distancia_circular(h_final, h_alvo))
        s_avaliacao =  1*(0.2*s_final + (1 - abs(s_final - s_alvo)))
        l_avaliacao = (1 - abs(l_final - l_alvo))
        l_avaliacao = 0

        Y[i] = h_avaliacao**2 + s_avaliacao**2 + l_avaliacao**2

    return Y

    

    
def distancia_circular(h_final, h_alvo):
    angle_1 = 2*np.pi*h_final
    angle_2 = 2*np.pi*h_alvo
    # calcular o menor angulo entre os dois angulos
    angle_min = min(abs(angle_1-angle_2), abs(angle_1-angle_2+2*np.pi), abs(angle_1-angle_2-2*np.pi))
    return angle_min/(2*np.pi)
