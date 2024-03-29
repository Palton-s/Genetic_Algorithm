
class Dados():    
    # define informações da população
    mudanca_limites = 10
    NV = 4  # número de variáveis
    N = 200 # numero de individuos
    n_bits = 12 # número de bits por variável em cada indivíduo
    percent_elite = 0.1 # percentual dos melhores indivíduos que serão conservados para a próxima geração
    n_cortes_no_cruzamento = int(n_bits/3) # número de pontos de corte no cruzamento
    n_geracoes = 800 # número de gerações
    taxa_de_mutacao = 0.5 # taxa de mutação
    intensidade_da_mutacao = 0.5  # intensidade da mutação
    """limites = [[-20,0]]
    for i in range(NV-1):
        limites.append([-10, 10])"""
    #limites = [[-3741232873392.582, -1408710845147.9106], [0.34088866438433585, 1.1948414699027416], [-255392917639.78745, -93539110053.27234]]
    #limites = [[-5, 0], [-4, 0], [-40, 0], [0, 40], [15, -5]]
    #limites = [[-1000, 1000],[-1000, 1000],[-1000, 1000],[-1000, 1000],[-1000, 1000]]
    #limites = [[13.148469220847417, 29.668025099939697], [-5.048801705719397, -2.019050955766024], [-40.2675376485014, -16.07143717117349], [14.973431900140957, 53.95690912629257], [101.40806390842977, 193.48988251962226]]
    #limites = [[-10, 10],[-10, 10],[-10, 10],[-10, 10],[-10, 10]]
    #limites = [[44, 46], [0.4, 0.6], [2.9, 3.1]]
    #limites = [[1,3],[-10,10],[-10,10],[-10,10],[1.44,1.46]]
    #limites = [[-100, 100],[-100, 100],[-100, 100],[-100, 100],[1.44,1.46]]
    #[3.061415, 0.727714, -0.795586, 0.438308, 1.448591]
    #limites = [[2.7, 2.9],[0, 1.5],[-1.5, 0.5],[0, 1],[1.44, 1.449]]
    #limites = [[2.3731778425655974, 3.4927113702623904], [0.16034985422740516, 0.9475218658892128], [-1.3265306122448979, 1.1224489795918364], [-0.49562682215743403, 0.3790087463556855], [1.44, 1.46]]
    #limites = [[2.0, 4.239067055393585], [-0.10204081632653073, 1.4723032069970845], [-2.5510204081632653, 2.3469387755102042], [-0.49562682215743403, 2.1282798833819245], [1.44, 1.46]]
    limites = [[0, 10], [-2.5,2.5], [-2.5,2.5], [0,5]]


    def change_limites(self, variable, range1, range2):
        self.limites[variable] = [range1, range2]
        return self.limites
    
    def get_limites(self):
        return self.limites
    def set_limites(self, limites):
        self.limites = limites
        return self.limites

        