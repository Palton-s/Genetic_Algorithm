import random
import numpy as np

setss = []

for i in range(16):
    setss.append([np.round(random.uniform(-1, 1), 2),np.round(random.uniform(-1, 1), 2)])

avaliacoes = []
for i in range(16):
    avaliacoes.append(np.round(np.exp(-np.linalg.norm(setss[i])), 2))

print(setss)
print(avaliacoes)

    