
n_bits = 26
limites = [-10000, 10000]

n_bites = 2**n_bits
print(n_bites)


print(n_bites)

precisoes = []

for i in range(20):
    step = (limites[1]-limites[0])/n_bites
    precisoes.append([limites[1]-limites[0],+step])
    output = (str(limites[1]-limites[0])+" - "+str(step))
    # replace . for ,
    output = output.replace(".", ",")
    print(output)
    # get significative algarism of step
    algrism_significative = 0
    while step < 1:
        step = 10*step
        algrism_significative += 1
    limites = [limites[i]/2 for i in range(len(limites))]
    
