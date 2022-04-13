from cmath import polar
from operator import le
import random
from traceback import print_tb
import numpy as np
import colorsys
import math


# function for generating the population of a GA
def gera_populacao(n_variaveis, n_individuos, n_bits):
    # population
    X = []
    # population
    for i in range(n_individuos):
        individuo = gera_individuo(n_bits, n_variaveis)
        X.append(individuo)
    return X

def gera_individuo(n_bits, n_variaveis):
    individuo = []
    for i in range(n_variaveis):
        variavel = []
        for j in range(n_bits):
            variavel.append(random.randint(0, 1))
        individuo.append(variavel)
    return individuo

def traduz_individuo(individuo):
    # parameters
    n_bits = len(individuo[0])
    max_bits = 2**n_bits-1
    n_variaveis = len(individuo)
    variaveis = []
    # foreach variavel
    for i in range(n_variaveis):
        variavel = 0
        # foreach bit
        for j in range(n_bits):
            variavel = variavel + individuo[i][j]*(2**(n_bits-j-1))
        variaveis.append(variavel*10/max_bits)
    return variaveis

# function for evaluate the population X

def evaluate(X):
    Y = np.zeros(len(X))
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
        # traduz os valores de X
        X_traduz = traduz_individuo(X[int(i)])
        x = X_traduz[0]
        y = X_traduz[1]
        n = 9
        s2 = 0.15
        r = np.sqrt((x)**2 + (y)**2)
        #f = (np.cos(n*math.pi*r)**2)*np.exp(-r**2/s2)
        f = np.exp(-r**2)
        Y[i] = f
    Y = Y - np.min(Y)
    return Y

def order(X, Y):
    # order
    NV = len(X[0])
    N = len(X)
    for i in range(N):
        for j in range(N):
            if Y[i] < Y[j]:
                aux = Y[i]
                Y[i] = Y[j]
                Y[j] = aux
                aux = X[i]
                X[i] = X[j]
                X[j] = aux
    return X, Y

def Print(X, Y):
    # best
    best = np.argmax(Y)
    # worst
    worst = np.argmin(Y)
    # print best
    print("Melhor: ", Y[best], X[best])
    # print worst
    print("Pior: ", Y[worst], X[worst])
    # print population
    print(X)
    # print fitness
    print(Y)




def Track(Y):
    Probability = np.zeros(len(Y))
    ProbTrack = np.zeros(len(Y))
    Sum = 0.0
    for i in range(len(Y)):
        Sum = Sum + Y[i]
    for i in range(len(Y)):
        Probability[i] = Y[i]/Sum
    Auxiliary = 0.0
    ProbTrack[0] = 0.0
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
                    Indices.append(i)
                    Reproducer.append(X[i-1])
                    break

    return Reproducer

def Reproducao(selection):
    # get the number of individuos
    n_reprodutores = len(selection)
    n_variaveis = len(selection[0])
    n_bits = len(selection[0][0])
    # create the new population
    new_populacao = []
    # foreach individuo 0, 2, 4, 6 ...
    for i in range(0, n_reprodutores, 2):
        # get the parents
        p1 = selection[i]
        p2 = selection[i+1]
        # create the children
        c1 = []
        c2 = []
        for k in range(n_variaveis):
            # get the first half bits of the parents
            bits_1 = []
            bits_2 = []
            for j in range(int(n_bits/2)):
                bits_1.append(p1[k][j])
                bits_2.append(p2[k][j])
            # get the second half bits of the parents
            for j in range(int(n_bits/2), n_bits):
                bits_1.append(p2[k][j])
                bits_2.append(p1[k][j])

            c1.append(bits_1)
            c2.append(bits_2)
        new_populacao.append(c1)
        new_populacao.append(c2)

    return new_populacao


        
        

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


def Mutation(X, percentage):
    # parameters
    NV = len(X[0])
    N = len(X)
    n_bits = len(X[0][0])
    # read parameters
    M = int(N*percentage)
    # mutation
    for I in range(M):
        # for the variables
        for j in range(NV):
            W = np.random.uniform(0, 1)
            Auxiliary = W*N
            ChosenMutation = int(Auxiliary)
            R = random.randint(0,n_bits-1)
            if X[ChosenMutation][j][R] == 0:
                X[ChosenMutation][j][R] = 1
            else:
                X[ChosenMutation][j][R] = 0
    return X

def Gaussian(X, Reproducer, D):
    # for the variables
    NV = X.shape[0]
    N = X.shape[1]
    Son1 = np.zeros((NV, N))
    Son2 = np.zeros((NV, N))
    for L in range(NV):
        # for the individuals
        for K in range(0, int(N/2)):
            Walker1 = Reproducer[L, K+1]
            Walker2 = Reproducer[L, K]
            Step = D[L]/(2*np.sqrt(N))
            Nsteps = 100
            for I in range(Nsteps):
                W = random.uniform(0, 1)
                Q = random.uniform(0, Step)
                if W <= 0.5:
                    Walker1 = Walker1 + Q
                else:
                    Walker1 = Walker1 - Q
            for I in range(Nsteps):
                W = random.uniform(0, 1)
                Q = random.uniform(0, Step)
                if W <= 0.5:
                    Walker2 = Walker2 + Q
                else:
                    Walker2 = Walker2 - Q
            Son1[L, K] = Walker1
            Son2[L, K] = Walker2

    return Son1, Son2


def Attribution(X, Sons):
    # for the variables
    NV = len(X[0])
    N = len(X)
    # attribution
    New_X = []
    for i in range(len(Sons)):
        New_X.append(Sons[i])
    for i in range(len(Sons), N):
        New_X.append(X[i])
    return New_X


def GA(NV, N):
    # population
    n_bits = 9
    X = gera_populacao(NV, N, n_bits)
    n_geracoes = 250

    for i in range(n_geracoes):

        # evaluate
        Y = evaluate(X)
        # order
        X, Y = order(X, Y)
        # probability track
        ProbTrack = Track(Y)
        selection = Selection(X, ProbTrack)
        Sons = Reproducao(selection)

        X = Attribution(X, Sons)
        X = Mutation(X, 0)

        print(Y)

GA(2, 12)

# elitismo de no máximo 10% da população