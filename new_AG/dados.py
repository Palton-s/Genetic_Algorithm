
class Dados():    
    # define informações da população
    mudanca_limites = 10
    n_a = 3
    NV = 2+n_a  # número de variáveis
    N = 1000 # numero de individuos
    n_bits = 16 # número de bits por variável em cada indivíduo
    percent_elite = 0.010 # percentual dos melhores indivíduos que serão conservados para a próxima geração
    n_cortes_no_cruzamento = int(n_bits/3) # número de pontos de corte no cruzamento
    n_geracoes = 3000 # número de gerações
    taxa_de_mutacao = 0.2 # taxa de mutação
    intensidade_da_mutacao = 0.2 # intensidade da mutação
    """limites = [[-20,0]]
    for i in range(NV-1):
        limites.append([-10, 10])"""
    #limites = [[-3741232873392.582, -1408710845147.9106], [0.34088866438433585, 1.1948414699027416], [-255392917639.78745, -93539110053.27234]]
    #limites = [[-5, 0], [-4, 0], [-40, 0], [0, 40], [15, -5]]
    #limites = [[-1000, 1000],[-1000, 1000],[-1000, 1000],[-1000, 1000],[-1000, 1000]]
    #limites = [[13.148469220847417, 29.668025099939697], [-5.048801705719397, -2.019050955766024], [-40.2675376485014, -16.07143717117349], [14.973431900140957, 53.95690912629257], [101.40806390842977, 193.48988251962226]]
    #limites = [[-10, 10],[-10, 10],[-10, 10],[-10, 10],[-10, 10]]
    limites = [[-1000, 1000],[-1000, 1000],[-1000, 1000],[-1000, 1000],[-1000, 1000]]

    def change_limites(self, variable, range1, range2):
        self.limites[variable] = [range1, range2]
        return self.limites
    
    def get_limites(self):
        return self.limites
    def set_limites(self, limites):
        self.limites = limites
        return self.limites

        