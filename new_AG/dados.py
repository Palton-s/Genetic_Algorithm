
class Dados():    
    # define informações da população
    NV = 3 # número de variáveis
    N = 100 # numero de individuos
    n_bits = 256 # número de bits por variável em cada indivíduo
    percent_elite = 0.1 # percentual dos melhores indivíduos que serão conservados para a próxima geração
    n_cortes_no_cruzamento = 5 # número de pontos de corte no cruzamento
    n_geracoes = 50 # número de gerações
    taxa_de_mutacao = 0.1 # taxa de mutação
    intensidade_da_mutacao = 0.1 # intensidade da mutação
    limites = [[100, 200], [-4, 0], [-40, 0], [0, 40], [15, -5]]
    #limites = [[-1000, 1000],[-1000, 1000],[-1000, 1000],[-1000, 1000],[-1000, 1000]]
    #limites = [[13.148469220847417, 29.668025099939697], [-5.048801705719397, -2.019050955766024], [-40.2675376485014, -16.07143717117349], [14.973431900140957, 53.95690912629257], [101.40806390842977, 193.48988251962226]]
    #limites = [[-10, 10],[-10, 10],[-10, 10],[-10, 10],[-10, 10]]

    def change_limites(self, variable, range1, range2):
        self.limites[variable] = [range1, range2]
        return self.limites
    
    def get_limites(self):
        return self.limites
    def set_limites(self, limites):
        self.limites = limites
        return self.limites

        