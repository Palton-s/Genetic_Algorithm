from ga import GA
import datetime

def limites_espalhamento(step_range):
    range_min = -step_range
    range_max = step_range
    mean_range = (range_min + range_max) / 2

    ranges = []
    # ranges = [[[-1000,0,],[-1000,0,],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]],[[-1000,0],[-1000,0],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]],[[-1000,0],[-1000,0],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        size_range = (range_max-range_min)/2
                        ranges.append([[range_min+i*size_range,range_min+(i+1)*size_range],[range_min+j*size_range,range_min+(j+1)*size_range],[range_min+k*size_range,range_min+(k+1)*size_range],[range_min+l*size_range,range_min+(l+1)*size_range],[range_min+m*size_range,range_min+(m+1)*size_range]])

    return ranges

limites = limites_espalhamento(1000)
#print(limites)

count = 0
avaliacoes = []
for limite in limites:
    count += 1
    # raio n pode ser negativo
    limite[-1] = [0,4]
    limite[1] = [0,10]
    ga = GA(3, limite)
    print(count,"melhor individuo: ", ga.best_evaluation, "limite: ", limite)
    avaliacoes.append([ga.best_evaluation, limite])
    # write in file esp_dom.log
    

# order avaliacoes by index 0
avaliacoes = sorted(avaliacoes, key=lambda x: x[0])
print("jaja")

with open("esp_dom.log", "a") as f:
    # datetime format date and hour
    datetime_now = datetime.datetime.now()
    datetime_now = datetime_now.strftime("%Y-%m-%d %H:%M:%S")
    f.write(" ----------------- "+datetime_now+" ----------------- ")
    for avaliacao in avaliacoes:
        f.write(str(avaliacao[0]) + " " + str(avaliacao[1]) + "\n")
    f.write(" ----------------- "+datetime_now+" ----------------- ")