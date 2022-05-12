import numpy as np
import random

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
    aux = int(binary, 2)
    # converte o valor inteiro para o intervalo de valores do cromossomo
    decimal = (aux*final)/(2**n-1)+init/2
    # retorna o valor decimal
    return decimal

def mutacao_cromossomo_binario(binario, intensidade):
    # percorre cada bit do cromossomo
    for j in range(len(binario)):
        # dada a probabilidade de mutação, altera o bit de 0 para 1 ou de 1 para 0
        if random.uniform(0, 1) < intensidade:
            if binario[j] == '1':
                binario = binario[:j] + '0' + binario[j+1:]
            else:
                binario = binario[:j] + '1' + binario[j+1:]
    # retorna o cromossomo binário mutado
    return binario

def crossover(cromossomo1, cromossomo2, n_cortes):
    # pega o numero de bits do cromossomo
    n_bits = len(cromossomo1)
    # escolhe aleatoriamente os cortes
    crossover_points = random.sample(range(0, n_bits), n_cortes+1)
    # ordena os cortes
    crossover_points.sort()
    # transforma cromossomos em um list de bits
    arr_cromossomo1 = list(cromossomo1)
    arr_cromossomo2 = list(cromossomo2)
    # executa o crossover
    for i in range(len(crossover_points)-1):
        # pega os bits do ponto de corte
        if i % 2 == 0:
            # se for par, pega o bit do pai 1
            # e coloca no filho 1
            # e pega o bit do pai 2
            # e coloca no filho 2
            aux = arr_cromossomo1[crossover_points[i]:crossover_points[i+1]]
            arr_cromossomo1[crossover_points[i]:crossover_points[i+1]] = arr_cromossomo2[crossover_points[i]:crossover_points[i+1]]
            arr_cromossomo2[crossover_points[i]:crossover_points[i+1]] = aux
    # une a lista de bits em uma string
    cromossomo1 = ''.join(arr_cromossomo1)
    cromossomo2 = ''.join(arr_cromossomo2)
    # retorna os cromossomos filhos
    return cromossomo1, cromossomo2

cromossomo1 = "11111111111111111111111111111111"
cromossomo2 = "00000000000000000000000000000000"

mutado = mutacao_cromossomo_binario(cromossomo1, 0.1)
print(cromossomo1)
print(mutado)

