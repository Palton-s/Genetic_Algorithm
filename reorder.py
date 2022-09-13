# read file count.csv

def get_best_limits():
    

    import csv
    import sys

    # read file with delimiter " ---- "
    with open("count.csv", "r") as f:
        # read data as array
        testes = f.readlines()
        # remove \n from each element of array
        testes = [testes[i].replace("\n", "") for i in range(len(testes))]
        # split each element of array by " -------- "
        testes = [testes[i].split(" ---- ") for i in range(len(testes))]
        # sort array by second element of each element
        testes.sort(key=lambda x: float(x[1]), reverse=False)
        # print array

    testes = testes[0:100]
    limites = []
    for values in testes:
        
        limite = values[2]
        #remove first [ and last ]
        limite = limite[2:-2]
        #split by ,
        limite = limite.split("], [")
        limites_float = []
        for i in limite:
            #split by ,
            i = i.split(", ")
            #convert to float
            i = [float(j) for j in i]
            limites_float.append(i)
        # list of list of float
        limites.append(limites_float)

    new_limites = []
    for i in range(limites[0].__len__()):
        new_lim = [min([j[i][0] for j in limites]), max([j[i][1] for j in limites])]
        new_limites.append(new_lim)

    print(testes[0][1])
    print(testes[0][2])
    print(testes[1][1])
    print(testes[1][2])
    print(testes[2][1])
    print(testes[2][2])
    print(testes[3][1])
    print(testes[3][2])




    return new_limites
    #[[2.0, 6.571428571428571], [-0.7142857142857144, 3.571428571428571], [-5.0, 5.0], [-4.285714285714286, 10.0], [1.3, 1.6]]
    #[[2.0, 6.571428571428571], [-0.10204081632653073, 3.571428571428571], [-5.0, 5.0], [-4.285714285714286, 10.0], [1.3, 1.6]]
    #[[2.0, 4.612244897959183], [-0.10204081632653073, 1.7346938775510203], [-5.0, 3.571428571428571], [-2.2448979591836733, 3.8775510204081636], [1.3, 1.6]]

print(get_best_limits())