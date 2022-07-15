
class Dados():    
    # define informações da população
    NV = 5 # número de variáveis
    N = 1000 # numero de individuos
    n_bits = 32 # número de bits por variável em cada indivíduo
    percent_elite = 0.1 # percentual dos melhores indivíduos que serão conservados para a próxima geração
    n_cortes_no_cruzamento = 5 # número de pontos de corte no cruzamento
    n_geracoes = 200 # número de gerações
    taxa_de_mutacao = 0.2 # taxa de mutação
    intensidade_da_mutacao = 0.1 # intensidade da mutação
    limites = [[100, 200], [-4, 0], [-40, 0], [0, 40], [15, -5]]
    for i in range(NV):
        limites.append([-100, 100])

    def change_limites(self, variable, range1, range2):
        self.limites[variable] = [range1, range2]
        return self.limites
    
    def get_limites(self):
        return self.limites

        