import random

random_spaces = random.sample(range(0, 16), 2)
mutation_form = []
# random_spaces = [0, 4, 8]
# mutation form = [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0]
for k in random_spaces:
    val = 0
    aux = 0
    for i in range(aux, k):
        mutation_form.append(val)
    val = val + 1
    aux += i
    

        

print(mutation_form)