import colorsys

def decimal_to_binary(number, alcance, n):
    init = alcance[0]
    final = alcance[1]
    # convertendo o valor decimal para binario
    aux = ((number-init/2)*(2**n-1))/final
    aux_int = int(aux)
    binary = bin(aux_int)
    # remove o 0b da string
    binary = binary[2:]
    # completa com zeros a esquerda
    binary = binary.zfill(n)
    # retorna o cromossomo em binario
    return binary

def binary_to_decimal(binary, alcance, n):
    # converte o cromossomo de binario para decimal
    init = alcance[0]
    final = alcance[1]
    # converte uma lista de bits para decimal
    decimal = 0
    for i in range(n):
        decimal += int(binary[i])*(2**(n-i-1))    
    # converte o valor inteiro para o intervalo de valores do cromossomo
    decimal = (decimal*final)/(2**n-1)+init/2
    # retorna o valor decimal
    return decimal

def converte_individuo(individuo, alcance):
    # define o array com as variáveis
    variaveis = []
    # recupera o número de variáveis
    n_variaveis = len(individuo)
    # recupera o número de bits por variável
    n_bits = len(individuo[0])
    # para cada variável, converte seu valor de binário para decimal
    for i in range(n_variaveis):
        variavel = binary_to_decimal(individuo[i], alcance , n_bits)
        variaveis.append(variavel)
    # retorna o array com as variáveis
    return variaveis

def converte_populacao(populacao, alcance):
    # resgata o número de indivíduos
    n_individuos = len(populacao)
    # inicia o array com a população convertida
    X = []
    # para cada indivíduo
    for i in range(n_individuos):
        # converte o indivíduo
        individuo = converte_individuo(populacao[i], alcance)
        # adiciona o indivíduo na população convertida
        X.append(individuo)
    # retorna a população convertida
    return X

def ordena(X,Y):
    # ordena os valores de X e Y com base em Y do menos bem avaliado para o melhor avaliado
    X, Y = zip(*sorted(zip(X, Y), key=lambda x: x[1], reverse=False))
    # retorna os valores ordenados
    return X, Y

def atribui(X, filhos, elite):
    # atribui os filhos aos indivíduos da população
    X = filhos
    # resgata o número de indivíduos elite
    n_elite = len(elite)    
    #substitui os elite na população nos últimos n_elite indivíduos
    for i in range(n_elite):
        X[-i] = elite[i]

    return X

def conta_bits_iguais(individuo, val):
    # conta o número de bits iguais entre o indivíduo e o valor
    n_bits = len(individuo[0])
    cont = 0
    for i in range(n_bits):
        if individuo[0][i] == val:
            cont += 1
    return cont

def mistura_cores(cor_1, cor_2, percent_1, percent_2):
    # mistura as cores com base nos percentuais
    cor_final = [0,0,0]
    for i in range(3):
        cor_final[i] = int((cor_1[i]*percent_1 + cor_2[i]*percent_2)/(percent_1+percent_2+0.001))
    return cor_final

import random

def calcula_hls(cor_final):
    # transforma RGB para hsl
    hls_color = colorsys.rgb_to_hls(cor_final[0]/255, cor_final[1]/255, cor_final[2]/255)
    # retorna o valor do matiz
    return hls_color

def calcula_h(individuo, cor_1, cor_2, cor_alvo, precisao):
    cor_final = mistura_cores(cor_1, cor_2, individuo, precisao-individuo)
    h_final = calcula_hls(cor_final)[0]
    h_alvo = calcula_hls(cor_alvo)[0]
    return 1-abs(h_final - h_alvo)

def calcula_h_individuo(individuo, cor_1, cor_2, cor_alvo,precisao):
    # calcula o valor do matiz
    cor_final = mistura_cores(cor_1, cor_2, individuo, precisao-individuo)
    h_final = calcula_hls(cor_final)[0]
    h_alvo = calcula_hls(cor_alvo)[0]
    return 1-abs(h_final - h_alvo)

def proximidade_de_cores_RGB(cor, cor_alvo):
    # calcula a distância entre a cor e a cor alvo
    dist = 0
    for i in range(3):
        dist += (cor[i]-cor_alvo[i])**2
    dist = dist**(1/2)
    return 1-dist
