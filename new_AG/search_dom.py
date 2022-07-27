from ga import GA
import numpy as np


limites = []
executions = 10
for i in range(executions):
    print("execução: ", i)
    ga = GA(100)
    limite = []
    limite = ga.limites.copy()
    limites.append(ga.limites.copy())
    #delete ga object
    del ga


new_limits = []
for k in range(len(limites[0])):
    # get all col of limites
    col = [limites[i][k] for i in range(len(limites))]
    # 
    mean_limit = np.mean([np.mean(col[i]) for i in range(len(col))])
    std_limit = np.std([np.std(col[i]) for i in range(len(col))])
    new_limit = [mean_limit-std_limit, mean_limit+std_limit]
    new_limits.append(new_limit)

ga__ = GA(100, new_limits)
    



print("jaja2")




    

