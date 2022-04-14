import random
from traceback import print_tb
import numpy as np
import colorsys
import math


# function for generating the population of a GA
def PopulationGenerator(NV, N):
    X = np.zeros((NV, N))
    for i in range(NV):
        #ValueI = [random.uniform(0, 10) for i in range(NV)]
        #ValueF = [random.uniform(0, 10) for i in range(NV)]
        for j in range(N):
            #W = random.random()
            X[i, j] = random.uniform(0, 10)
    return X


# function for evaluate the population X

def evaluate(X):
    Y = np.zeros(X.shape[1])
    individuos = X.shape[1]
    variaveis = X.shape[0]
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
        x = X[0, i]
        y = X[1, i]
        w = X[2, i]
        z = X[3, i]
        n = 9
        s2 = 0.15
        r = np.sqrt((x-0.5)**2 + (y-0.5)**2 + (w-0.5)**2 + (z-0.5)**2)
        f = (np.cos(n*math.pi*r)**2)*np.exp(-r**2/s2)

        Y[i] = f

    return Y


def order(X, Y):
    # order
    NV = X.shape[0]
    N = X.shape[1]
    for i in range(N):
        for j in range(N):
            if Y[i] < Y[j]:
                aux = Y[i]
                Y[i] = Y[j]
                Y[j] = aux
                for k in range(X.shape[0]):
                    aux = X[k, i]
                    X[k, i] = X[k, j]
                    X[k, j] = aux
    return X, Y


def Print(X, Y):
    # best
    best = np.argmax(Y)
    # worst
    worst = np.argmin(Y)
    # print best
    print("Best: ", Y[best], X[:, best])
    # print worst
    print("Worst: ", Y[worst], X[:, worst])
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
    ProbTrack[0] = 0.0
    for i in range(1, len(Y)):
        ProbTrack[i] = Auxiliary + Probability[i-1]
        Auxiliary = ProbTrack[i]
    return ProbTrack


def Selection(X, ProbTrack):
    N = X.shape[1]
    NV = X.shape[0]
    # sum of all probabilities
    Sum = 0.0
    for i in range(len(ProbTrack)):
        Sum = Sum + ProbTrack[i]

    # reproduction
    Reproducer = np.zeros((NV, N))
    # indices of the chosen individuals
    Indices = np.zeros(N)
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
                    Indices[k] = i
                    # add the individual
                    Reproducer[:, k] = X[:, i]
                    break
                else:
                    Indices[k] = i-1
                    Reproducer[:, k] = X[:, i-1]
                    break

    return Reproducer


def Deviation(X):
    # parameters
    NV = X.shape[0]
    N = X.shape[1]
    D = np.zeros(NV)
    # population
    for i in range(NV):
        # sum
        Sum1 = 0.0
        for j in range(N):
            Sum1 = Sum1 + X[i, j]
        # average
        AverageD = Sum1/N
        # sum
        Sum2 = 0.0
        for l in range(N):
            Sum2 = Sum2 + (X[i, l]-AverageD)**2
        # deviation
        D[i] = np.sqrt(Sum2/N)

    return D


def Mutation(X, percentage, intensity):
    # parameters
    NV = X.shape[0]
    N = X.shape[1]
    # read parameters
    M = int(N*percentage)
    # mutation
    for I in range(N-M, N):
        # for the variables
        for j in range(NV):
            W = np.random.uniform(0, 1)
            Auxiliary = W*N
            ChosenMutation = int(Auxiliary)
            R = (intensity)*(random.uniform(0, 1))
            aux = 0
            if W >= 0.5:
                aux = 1-R
            else:
                aux = 1+R
            X[j, I] = X[j, ChosenMutation]*aux
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


def Attribution(X, Son1, Son2, Elite, MM):
    # for the variables
    NV = X.shape[0]
    N = X.shape[1]
    # attribution
    for L in range(NV):
        # for the individuals
        for K in range(0, int(N/2)):
            X[L, K] = Son1[L, K]
        for K in range(int(N/2), N):
            X[L, K] = Son2[L, K-int(N/2)]

    for J in range(N-MM, N):
        for I in range(NV):
            X[I, J] = Elite[I, J]

    return X


def GA(NV, N):
    # population
    X = PopulationGenerator(NV, N)
    # number of Elite individuals
    MM = int(N*0.01)+1
    Elite = np.zeros((NV, N))
    n_geracoes = 250

    for i in range(n_geracoes):

        # evaluate
        Y = evaluate(X)
        # order
        X, Y = order(X, Y)
        # Elite is the last 0.01% of the population
        for I in range(N-MM, N):
            Elite[:, I] = X[:, I]
        # make all evaluations be positive
        Y = Y - np.min(Y)
        # probability track
        ProbTrack = Track(Y)
        D = Deviation(X)
        Reproducer = Selection(X, ProbTrack)
        Son1, Son2 = Gaussian(X, Reproducer, D)
        X = Attribution(X, Son1, Son2, Elite, MM)
        X = Mutation(X, 0.001, 0.001)

        # normalize all values of x from 0 to 1
        for i in range(N):
            for j in range(NV):
                X[j, i] = abs(X[j, i]/np.sum(X[:, i]))
        print(i)
        print("X")
        # print last Elite
        print(X[:, N-1])

    return X


GA(2, 100)

# elitismo de no máximo 10% da população