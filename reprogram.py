import random
from traceback import print_tb
from turtle import color
import numpy as np
import colorsys


# function for generating the population of a GA
def PopulationGenerator(NV, N):
    X = np.zeros((NV, N))
    for i in range(NV):
        # ValueI = [random.uniform(0, 10) for i in range(NV)]
        # ValueF = [random.uniform(0, 10) for i in range(NV)]
        for j in range(N):
            # W = random.random()
            X[i, j] = random.uniform(0, 1)
    return X


# function for evaluate the population X
"""def evaluate(X):
    Y = np.zeros(X.shape[1])
    individuos = X.shape[1]
    variaveis = X.shape[0]
    # foreach individuo
    for i in range(individuos):
        sum = 0
        # foreach variable
        for j in range(variaveis):
            sum += X[j, i]**2
        Y[i] = np.exp(-sum)
    return Y"""


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


def evaluate(X, cores, cor_alvo):

    hls_alvo = colorsys.rgb_to_hls(cor_alvo[0], cor_alvo[1], cor_alvo[2])
    h_alvo = hls_alvo[0]*360
    l_alvo = hls_alvo[1]
    s_alvo = hls_alvo[2]*-1

    Y = np.zeros(X.shape[1])
    individuos = X.shape[1]
    variaveis = X.shape[0]

    # foreach individuo
    for i in range(individuos):
        sum_of_weights = 0
        for j in range(variaveis):
            sum_of_weights += X[j, i]

        color = np.array([0, 0, 0])
        for j in range(variaveis):
            color = color + [X[j, i]*cores[j][0], X[j, i]
                             * cores[j][1], X[j, i]*cores[j][2]]

        color = color/sum_of_weights

        hls_individuo = colorsys.rgb_to_hls(
            int(color[0]), int(color[1]), int(color[2]))
        h_individuo = hls_individuo[0]*360
        l_individuo = hls_individuo[1]
        s_individuo = hls_individuo[2]*-1
        # evaluate is the module of distance between two angles in degrees
        mod_dist_angle = abs(h_alvo - h_individuo)
        angle = 0
        if mod_dist_angle > 180:
            angle = 360 - mod_dist_angle
        else:
            angle = mod_dist_angle

        angle = (180 - angle)/180  # from zero to 1

        angle = angle * 100

        number_of_colors_useds = 0
        for j in range(variaveis):
            if(X[j, i]>0.1):
                number_of_colors_useds += 1


        light = 0
        saturation = 0

        if(angle >= 70):
            light = 100*((255-abs(l_individuo - l_alvo))/255)
            saturation = 100*(1-abs(s_individuo - s_alvo))

        Y[i] = (angle+ light + saturation)/(2*number_of_colors_useds)

    return Y

# function to make all the first column of X as 0.5


def fix_first_color(X, percent_fixed):
    for i in range(X.shape[1]):
        X[0, i] = percent_fixed
    # normalize other columns to sum percent_fixed
    for j in range(X.shape[1]):
        sum_of_columns = 0
        for i in range(1, X.shape[0]):
            sum_of_columns += X[i, j]
        for i in range(1, X.shape[0]):
            X[i, j] = X[i, j]/(sum_of_columns)
        for i in range(1, X.shape[0]):
            X[i, j] = X[i, j]*(1-percent_fixed)

    return X


def GA(cores, cor_alvo, N, fixed_first_color=False, percent_fixed=0.5):
    NV = len(cores)
    # population
    X = PopulationGenerator(NV, N)
    # number of Elite individuals
    MM = int(N*0.01)+1
    Elite = np.zeros((NV, N))
    n_geracoes = 250
    # if fixed first color is true, fix the first color of the population
    if fixed_first_color:
        X = fix_first_color(X, percent_fixed)

    for I in range(n_geracoes):
        if(I != 0):
            X = Mutation(X, 0.001, 0.0001)
            # make all X values be abs
            X = np.abs(X)
            # order
            X, Y = order(X, Y)
            # Elite is the last 0.01% of the population
            for i in range(N-MM, N):
                Elite[:, i] = X[:, i]
            # make all evaluations be positive
            Y = Y - np.min(Y)
            # probability track
            ProbTrack = Track(Y)
            D = Deviation(X)
            Reproducer = Selection(X, ProbTrack)
            Son1, Son2 = Gaussian(X, Reproducer, D)
            X = Attribution(X, Son1, Son2, Elite, MM)

            # normalize all values of x from 0 to 1
            for i in range(N):
                sum_ind = np.sum(X[:, i])
                for j in range(NV):
                    X[j, i] = abs(X[j, i]/sum_ind)

        # if fixed first color is true, fix the first color of the population
        if fixed_first_color:
            X = fix_first_color(X, percent_fixed)
        # evaluate
        Y = evaluate(X, cores, cor_alvo)

        print(I)
        print("X")
        # if fixed first color is true, fix the first color of the population
        if fixed_first_color:
            X = fix_first_color(X, percent_fixed)
        # print last Elite

        final_color = np.array([0, 0, 0])

        for i in range(NV):
            final_color = final_color + cores[i]*X[i, N-1]

        percents_colors = []
        for i in range(NV):
            percents_colors.append(int(X[i, N-1] * 100))

        for i in range(NV):
            print("Percentual de cor " + str(i+1) +
                  ": " + str(percents_colors[i])+"%")

        print(str([int(final_color[0]), int(final_color[1]), int(final_color[2])]))
        Hf = colorsys.rgb_to_hls(
            int(final_color[0]), int(final_color[1]), int(final_color[2]))
        Ha = colorsys.rgb_to_hls(
            int(cor_alvo[0]), int(cor_alvo[1]), int(cor_alvo[2]))

        nota_matiz = np.round((1-abs(Hf[0] - Ha[0]))*100, 0)
        nota_saturacao = np.round((1-abs((Hf[1] - Ha[1])/255))*100, 0)
        nota_luminosidade = np.round((1-abs((Hf[2] - Ha[2])))*100, 0)
        print("matiz:" + str(nota_matiz)+"%")
        print("saturacao:" + str(nota_saturacao)+"%")
        print("luminosidade:" + str(nota_luminosidade)+"%")
        print(str([cor_alvo[0], cor_alvo[1], cor_alvo[2]]))

        percent_app = (nota_matiz + 3*nota_saturacao + 3*nota_luminosidade)/7
        print("Percentual de aproximacao: " +
              str(np.round(percent_app, 0))+"%")

        if(percent_app >= 99):  # if the percentual of approximation is greater than 98%
            break
    # return the last X
    return X[:, N-1]


paleta_de_cores = [
    np.array([255, 0, 0]),
    np.array([0, 255, 0]),
    np.array([0, 0, 255]),
    np.array([0, 0, 0]),
    np.array([255, 255, 255]),
]

cor_alvo = np.array([50, 50, 50])


def procura_2melhores_cores(cor_alvo, paleta_de_cores, fixed_color):
    individuos = 1000
    a = GA(paleta_de_cores, cor_alvo, individuos,
           fixed_color, percent_fixed=0.16)
    print(a)
    first = [np.argmax(a), np.max(a)]
    # set the max value as 0
    a[np.argmax(a)] = 0
    second = [np.argmax(a), np.max(a)]
    return [first, second]


def procura_cor(cor_alvo, paleta_de_cores, fixed_color):
    individuos = 1000
    a = GA(paleta_de_cores, cor_alvo, individuos,
           fixed_color, percent_fixed=0.8)
    # print(a)
    if(fixed_color == False):
        # return the bigger value of a and the index
        return np.argmax(a), np.max(a)
    else:
        # return the second bigger value of a and the index
        return np.argmax(a[1:])+1, np.max(a[1:])


def color_mixer(cor_alvo, paleta_de_cores):
    primeiras_melhores_cores = procura_2melhores_cores(
        cor_alvo, paleta_de_cores, False)
    first_color = primeiras_melhores_cores[0]
    first_color_prorpotion = first_color[1]
    first_color_color = paleta_de_cores[first_color[0]]
    second_color = primeiras_melhores_cores[1]
    second_color_prorpotion = second_color[1]
    second_color_color = paleta_de_cores[second_color[0]]

    # mix the two colors
    first_mix = (first_color_color*first_color_prorpotion +
                 second_color_color*second_color_prorpotion)/(first_color_prorpotion+second_color_prorpotion)
    # now add this color to the first position of the paleta_de_cores array
    #paleta_de_cores = np.insert(paleta_de_cores, 0, first_mix, axis=0)
    # and search for the best color fixing the fist color
    #third_color = procura_cor(cor_alvo, paleta_de_cores, False)
    #third_color_color = paleta_de_cores[third_color[0]]
    #third_color_prorpotion = third_color[1]
    #first_mix_prorpotion = 0.5
    # mix the first_mid and the third_color
    #final_color = (first_mix*first_mix_prorpotion +third_color_color*third_color_prorpotion)/(first_mix_prorpotion+third_color_prorpotion)

    print("Primeira mistura:")
    print(str(round(first_color_prorpotion*100, 0)) +
          "%"+" da cor "+str(first_color_color))
    print("com")
    print(str(round(second_color_prorpotion*100, 0)) +
            "%"+" da cor "+str(second_color_color))
    print("resultando na cor:")
    print(str(first_mix))


color_mixer(cor_alvo, paleta_de_cores)
