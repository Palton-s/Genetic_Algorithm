import numpy as np
import random
import colorsys


def decimal_to_binary(number, alcance, n):
    init = alcance[0]
    final = alcance[1]
    # convert decimal to binary
    aux = ((number-init/2)*(2**n-1))/final
    aux_int = int(aux)
    # convert to binary
    binary = bin(aux_int)
    # remove the '0b'
    binary = binary[2:]
    # complete with n zeros
    binary = binary.zfill(n)
    return binary

# make the reverse process


def binary_to_decimal(binary, alcance, n):
    init = alcance[0]
    final = alcance[1]
    # convert binary to decimal
    aux = int(binary, 2)
    # convert to decimal
    decimal = (aux*final)/(2**n-1)+init/2
    return decimal

def mutacao_cromossomo(individuo, intensidade,alcance, n_bits):
    binario = decimal_to_binary(individuo, alcance, n_bits)
    for j in range(len(binario)):
        if random.uniform(0, 1) < intensidade:
            if binario[j] == '1':
                binario = binario[:j] + '0' + binario[j+1:]
            else:
                binario = binario[:j] + '1' + binario[j+1:]
    individuo = binary_to_decimal(binario, alcance, n_bits)
    return binario, individuo


val_1 = -2
val_2 = 5
n_bits = 16

alcance = 1000
bin_1 = decimal_to_binary(val_1, [-50, 50], n_bits)
bin_2 = decimal_to_binary(val_2, [-50, 50], n_bits)
print(bin_1)
print(val_1)
print(bin_2)
print(val_2)

part_1_1 = bin_1[0:4]
part_1_2 = bin_1[4:8]
part_1_3 = bin_1[8:12]
part_1_4 = bin_1[12:16]
part_2_1 = bin_2[0:4]
part_2_2 = bin_2[4:8]
part_2_3 = bin_2[8:12]
part_2_4 = bin_2[12:16]

son_1 = part_1_1 + part_2_2 + part_1_3 + part_2_4
son_2 = part_2_1 + part_1_2 + part_2_3 + part_1_4
son_1_decimal = binary_to_decimal(son_1, [-50, 50], n_bits)
son_2_decimal = binary_to_decimal(son_2, [-50, 50], n_bits)
print("son_1: ", son_1, "son_1_decimal: ", son_1_decimal)
print("son_2: ", son_2, "son_2_decimal: ", son_2_decimal)

son1_binario_mutado, son1_mutado = mutacao_cromossomo(son_1_decimal, 0.1, [-50, 50], n_bits)
print("son1_mutado: ", son1_binario_mutado, "son1_mutado: ", son1_mutado)
son2_binario_mutado, son2_mutado = mutacao_cromossomo(son_2_decimal, 0.1, [-50, 50], n_bits)
print("son2_mutado: ", son2_binario_mutado, "son2_mutado: ", son2_mutado)


