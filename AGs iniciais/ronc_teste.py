import random
from traceback import print_tb
import numpy as np
import colorsys
import math

import matplotlib.pyplot as plt


# function for generating the population of a GA
def PopulationGenerator(NV, N):
    X = []

    for i in range(N):
        variaveis = []
        for j in range(NV):
            variaveis.append(random.uniform(-1, 1))
        X.append(variaveis)
    return X


# function for evaluate the population X

def evaluate(X):
    Y = []
    individuos = len(X)
    variaveis = len(X[0])
    # foreach individuo
    for i in range(individuos):
        sum = 0
        # Teste P1

        """n = 9
        x = X[0, i]
        y = X[1, i]
        s2 = 0.15
        r = np.sqrt((X[0, i]-0.5)**2 + (X[1, i]-0.5)**2)
        f = (np.cos(n*math.pi*r)**2)*np.exp(-r**2/s2)
        Y[i] = f"""
        # teste P2

        """x = X[0, i]
        y = X[1, i]
        r1 = np.sqrt((X[0, i]-0.5)**2 + (X[1, i]-0.5)**2)
        r2 = np.sqrt((X[0, i]-0.6)**2 + (X[1, i]-0.1)**2)
        f = 0.8*np.exp(-(r1**2)/(0.3**2))+0.879008*np.exp(-(r2**2)/(0.03**2))"""
        # teste P3
        x = X[i][0]
        y = X[i][1]
        #y = X[i][1]
        #z = X[i][2]
        #w = X[i][3]

        n = 9
        s2 = 0.15
        r = (x-0.5)**2 + (y-0.5)**2
        #f = (np.cos(n*math.pi*r)**2)*np.exp(-r**2/s2)
        f = np.exp(-r)

        Y.append(f)

    return Y


def order(X, Y):
    # join X and Y in an array
    x_ev = []
    for i in range(len(X)):
        x_ev.append([Y[i], X[i]])
    # order x_env by fitness
    x_ev.sort(key=lambda x: x[0], reverse=False)
    # split x_env in X and Y
    Y = []
    X = []
    for i in range(len(x_ev)):
        Y.append(x_ev[i][0])
        X.append(x_ev[i][1])

    return X, Y


def Print(X, Y):
    # best
    best = np.argmax(Y)
    # worst
    worst = np.argmin(Y)
    # print best
    print("Best: ", Y[best], X[best])
    # print worst
    print("Worst: ", Y[worst], X[worst])
    # print population
    print(X)
    # print fitness
    print(Y)


def Aline(T):
    AL = np.zeros(len(T))
    Sum = 0.0
    for i in range(len(T)):
        Sum = Sum+T[i]
    AverageT = Sum/(len(T)*1.0)
    A = ((0.2)*AverageT)/(T[-1]-AverageT)
    B = (1.0-A)*AverageT
    for i in range(len(T)):
        AL[i] = A*T[i]+B
    return AL


def Track(Y):
    Probability = np.zeros(len(Y))
    ProbTrack = np.zeros(len(Y))
    Sum = 0.0
    for i in range(len(Y)):
        Sum = Sum + Y[i]
    for i in range(len(Y)):
        Probability[i] = Y[i]/Sum
    Auxiliary = 0.0
    ProbTrack[0] = 0
    for i in range(1, len(Y)):
        ProbTrack[i] = Auxiliary + Probability[i-1]
        Auxiliary = ProbTrack[i]
    return ProbTrack


def Selection(X, ProbTrack):
    N = len(X)
    NV = len(X[0])
    # sum of all probabilities
    Sum = 0.0
    for i in range(len(ProbTrack)):
        Sum = Sum + ProbTrack[i]

    # reproduction
    Reproducer = []
    # indices of the chosen individuals
    Indices = []
    # sum the probabilities into the value of R

    for k in range(int(N/2)):
        # random number from 0 to Sum
        R = random.uniform(0, Sum)
        # auxiliar for sum
        Aux = 0.0
        for i in range(len(ProbTrack)):
            Aux = Aux + ProbTrack[i]
            if R < Aux:
                # if the index is not already in the array
                if i not in Indices:
                    # add the index
                    Indices.append(i)
                    # add the individual
                    Reproducer.append(X[i])
                    break
                else:
                    Indices.append(i-1)
                    Reproducer.append(X[i-1])
                    break
    return Reproducer


def Deviation(X):
    # parameters
    NV = len(X[0])
    N = len(X)
    D = np.zeros(NV)
    # population
    for i in range(NV):
        # sum
        Sum1 = 0.0
        for j in range(N):
            Sum1 = Sum1 + X[j][i]
        # average
        AverageD = Sum1/N
        # sum
        Sum2 = 0.0
        for l in range(N):
            Sum2 = Sum2 + (X[l][i]-AverageD)**2
        # deviation
        D[i] = np.sqrt(Sum2/N)

    return D


def Mutation(X, percentage, intensity):
    # parameters
    NV = len(X[0])
    N = len(X)
    # read parameters
    M = int(N*percentage)
    # mutation
    for I in range(M):
        # for the variables
        W = np.random.uniform(0, 1)
        Auxiliary = W*N
        ChosenMutation = int(Auxiliary)
        #print("test de mutação")
        for j in range(NV):
            P = np.random.uniform(0, 1)
            R = (intensity)
            aux = 0
            if P >= 0.5:
                aux = 1-R
            else:
                aux = 1+R
            X[ChosenMutation][j] = X[ChosenMutation][j]*aux
            #print("test de mutação")
    return X


def Gaussian_fail(X, Reproducer, D):
    # for the variables
    NV = len(X[0])
    N = len(X)
    Son1 = []
    Son2 = []
    for K in range(0, int(N/2)):
        Walker1 = Reproducer[K]
        Walker2 = Reproducer[K]
        # for the individuals
        for L in range(NV):
            Step = D[L]/(2*np.sqrt(N))
            Nsteps = 100
            for I in range(Nsteps):
                W = random.uniform(0, 1)
                Q = random.uniform(0, Step)
                if W <= 0.5:
                    Walker1[L] = Walker1[L] + Q
                else:
                    Walker1[L] = Walker1[L] - Q
            for I in range(Nsteps):
                W = random.uniform(0, 1)
                Q = random.uniform(0, Step)
                if W <= 0.5:
                    Walker2[L] = Walker2[L] + Q
                else:
                    Walker2[L] = Walker2[L] - Q
            Son1.append(Walker1)
            Son2.append(Walker2)

    return Son1, Son2

def decimal_to_binary(number, range, n):
    # convert decimal to binary
    aux = ((number + range/2)*(2**n))/range
    aux_int = int(aux)
    #convert to binary
    binary = bin(aux_int)
    # remove the '0b'
    binary = binary[2:]
    print(binary)



def Gaussian(X):
    # for the variables
    NV = len(X[0])
    N = len(X)
    Son1 = []
    Son2 = []
    for K in range(0, int(N/2)):

def Attribution(X, Son1, Son2, Elite, MM):
    # for the variables
    NV = len(X[0])
    N = len(X)
    # attribution
    # for the individuals
    for K in range(0, int(N/2)):
        X[K] = Son1[K]
    for K in range(int(N/2), N):
        X[K] = Son2[K]

    for J in range(N-MM, N):

        X[J] = Elite[J-N+MM]

    return X


def GA(NV, N):
    # population
    X = PopulationGenerator(NV, N)
    # number of Elite individuals
    MM = int(N*0.5)+1
    Elite = []
    n_geracoes = 100

    dados_relatorio = []

    dado_relatorio = []
    dado_relatorio.append("Geração")
    dado_relatorio.append("Média das avaliações")
    dado_relatorio.append("Avaliação do melhor indivíduo")
    dado_relatorio.append("Avaliação do pior indivíduo")
    dado_relatorio.append("Valor do pior indivíduo")

    dados_relatorio.append(dado_relatorio)

    for geracao in range(n_geracoes):
        dado_relatorio = []

        # evaluate
        Y = evaluate(X)
        # order
        X, Y = order(X, Y)

        result = []
        for i in range(len(X)):
            result.append([X[i][0], X[i][1], Y[i]])
        print("X")
        print(result)
        print("------------------")

        # Elite is the last 0.01% of the population
        for I in range(N-MM, N):
            Elite.append(X[I])
        # make all evaluations be positive
        Y = Y/max(Y)

        # probability track
        ProbTrack = Track(Y)
        D = Deviation(X)
        Reproducer = Selection(X, ProbTrack)
        Son1, Son2 = Gaussian(X, Reproducer, D)
        X = Attribution(X, Son1, Son2, Elite, MM)
        #X = Mutation(X, 0, 0)

        #print(geracao)
        #print("X")
        # print last Elite
        #print(Elite[MM-1], " ", Y[N-MM])
        #print(Elite[MM-2], " ", Y[N-MM-1])
        #print(Elite[MM-3],  " ", Y[N-MM-2])
        # generation
        dado_relatorio.append(geracao)
        # mean of evaluates
        dado_relatorio.append(np.mean(Y))
        # bigger value of evaluate
        dado_relatorio.append(np.max(Y))
        dado_relatorio.append(np.min(Y))
        dado_relatorio.append(Elite[MM-1])
        dados_relatorio.append(dado_relatorio)
        print(geracao)
        
        

    return dados_relatorio




dados = GA(2, 30)

for i in range(len(dados)):
    print(dados[i])

# plot dados
