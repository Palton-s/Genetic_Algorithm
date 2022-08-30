import matplotlib.pyplot as plt

NV = 3

#readlines file dados_grafico_evolucao.csv
with open("dados_grafico_evolucao.csv", "r") as f:
    dados = f.readlines()

new_dados = []
for dado in dados:
    # remove [ and ] and \n
    dado = dado.replace("[", "")
    dado = dado.replace("]", "")
    dado = dado.replace("\n", "")    
    # cels
    values = dado.split(";")
    
    new_values = []
    for i in range(len(values)):
        new_values.append([])
        for j in range(len(values[i].split(","))):
            new_values[i].append(float(values[i].split(",")[j]))
    new_dados.append(new_values)
    domains = []
    for i in range(NV):
        min_domain = [x[i][0] for x in new_dados]
        max_domain = [x[i][1] for x in new_dados]
        domain = [min_domain, max_domain]
        domains.append(domain)
    individuals = []
    for i in range(NV):
        individuals.append([x[i][2:] for x in new_dados])

print("new_dados")

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
for i in range(NV):
    values_graph_lines = [individuals[i][j] for j in range(len(individuals[i]))]
    index = [x for x in range(len(values_graph_lines))]
    
    min_plot = [domains[i][0][j] for j in range(len(domains[i][0]))]
    max_plot = [domains[i][1][j] for j in range(len(domains[i][1]))]
    
    # plot line meanplot and minplot and maxplot
    plt.subplot(NV, 1, i+1)
    #plotlines
    for k in range(len(values_graph_lines[0])):
        valus_to_plot_line = [x[k] for x in values_graph_lines]
        plt.plot(index, valus_to_plot_line, color="blue", alpha=0.2)
    plt.plot(index, min_plot, label="Domínio mínimo", color="green")
    plt.plot(index, max_plot, label="Domínio máximo", color="red")
    plt.legend()
    plt.xlabel("Nº da geração")
    plt.ylabel("Valor do parâmetro")
    plt.title("Evolução do " + str(i+1)+ "º parâmetro")
plt.show()
print("jaja")
# plot line