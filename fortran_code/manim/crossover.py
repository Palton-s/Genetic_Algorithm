from manim import *
import random

config.background_color = "#fff"

def set_bits(n_bits):
    bits = VGroup()
    for i in range(len(n_bits)):
        # make a square with a number 1 inside
        square = Square(stroke_width=3, stroke_color=BLACK, side_length=1)
        randon = n_bits[i]
        bit_number = Text(str(randon), font="Courier",
                          font_size=50, color=BLACK)
        bit_number.move_to(square.get_center())
        # make group with square and number 1
        group = VGroup(square, bit_number)
        # move the left side for the right side of the previous square
        group.shift(RIGHT*i * square.get_width())
        # add group to the bits
        bits.add(group)
    bits.move_to(ORIGIN)
    bits.set_color(RED)
    return bits

def crossovers(cromossomo1, cromossomo2, crossover_points):
    # pega o numero de bits do cromossomo
    
    # gera com cromossomo 1 como uma lista de bits todos zerados
    cromossomo_filho_1 = cromossomo1.copy()
    # gera com cromossomo 2 como uma lista de bits todos zerados
    cromossomo_filho_2 = cromossomo2.copy()
    # executa o crossover
    for i in range(len(crossover_points)-1):
        # pega o número de cortes
        if i % 2 == 0:
            # como os filhos são clones dos respectivos pais, basta alterar os grupos pares de bits
            # assim se i for par, 
            # pega o bit do pai 2 e coloca no filho 1
            # e pega o bit do pai 1 e coloca no filho 2
            aux1 = cromossomo1[crossover_points[i]:crossover_points[i+1]].copy()
            aux2 = cromossomo2[crossover_points[i]:crossover_points[i+1]].copy()
            cromossomo_filho_1[crossover_points[i]:crossover_points[i+1]] = aux2
            cromossomo_filho_2[crossover_points[i]:crossover_points[i+1]] = aux1
    # retorna os cromossomos filhos
    return cromossomo_filho_1, cromossomo_filho_2

def crossovers_colors(cromossomo1, cromossomo2, crossover_points):
    # executa o crossover
    cromossomo1.set_color(BLUE)
    cromossomo2.set_color(RED)
    for i in range(len(crossover_points)-1):
        if i % 2 == 0:
            for i in range(crossover_points[i], crossover_points[i+1]):
                cromossomo1[i].set_color(RED)
                cromossomo2[i].set_color(BLUE)
        else:
            for i in range(crossover_points[i], crossover_points[i+1]):
                cromossomo1[i].set_color(BLUE)
                cromossomo2[i].set_color(RED)
    # retorna os cromossomos filhos
    return cromossomo1, cromossomo2




def set_bits_list(n_bits):
    bits = []
    for i in range(n_bits):
        bits.append(random.randint(0, 1))
    return bits

def binary_to_range(binary_list):
    decimal_list = []
    for i in range(len(binary_list)-1, 0, -1):
        decimal_list.append(binary_list[i]*(2**i))
    innt = sum(decimal_list)
    rangess = [-100,100]
    return round((innt/(2**len(binary_list)))*(rangess[1]-rangess[0]) + rangess[0], 2)

class crossover(Scene):
    def construct(self):
        n_bits = 20
        pai_bits = set_bits_list(n_bits)
        mae_bits = set_bits_list(n_bits)
        
        n_cortes = 1
        crossover_points = random.sample(range(0, n_bits), n_cortes)
        crossover_points.append(0)
        crossover_points.append(n_bits-1)
        crossover_points.sort()
        cromossomo_filho_1, cromossomo_filho_2 = crossovers(pai_bits, mae_bits, crossover_points)
        cromossomo1 = set_bits(cromossomo_filho_1)
        cromossomo2 = set_bits(cromossomo_filho_2)


        filho_1, filho_2 = crossovers_colors(cromossomo1, cromossomo2, crossover_points)
        filho_1_val = Tex("= "+str(binary_to_range(cromossomo_filho_1)), color=BLUE)
        filho_2_val = Tex("= "+str(binary_to_range(cromossomo_filho_2)), color=BLUE)
        filho_2.next_to(filho_1, DOWN)

        pai_val = Tex("= "+str(binary_to_range(pai_bits)), color=RED)
        mae_val = Tex("= "+str(binary_to_range(mae_bits)), color=RED)
        pai = set_bits(pai_bits)
        mae = set_bits(mae_bits)
        mae.next_to(pai, DOWN)

        
        
        pais = VGroup(pai, mae)
        filhos = VGroup(filho_1, filho_2)
        filhos.next_to(pais, DOWN)
        
        legenda = Text(str(n_cortes)+" cortes", color=RED)        

        filho_1_val.next_to(filho_1, RIGHT)
        filho_2_val.next_to(filho_2, RIGHT)
        pai_val.next_to(pai, RIGHT)
        mae_val.next_to(mae, RIGHT)

        grupo = VGroup(pais, filhos, filho_1_val, filho_2_val, pai_val, mae_val, legenda)
        grupo.move_to(ORIGIN)


        grupo.scale(0.5)
        legenda.next_to(grupo, UP)
        
        self.add(grupo, legenda, pai_val, mae_val, filho_1_val, filho_2_val)





