from tokenize import group
from manim import *
import random


config.background_color = "#fff"

def set_box(my_arr):
    bits = VGroup()
    for i in range(len(my_arr)):
        # make a square with a number 1 inside
        square = Square(stroke_width=3, stroke_color=BLACK, side_length=1)
        bit_number = Text(str(my_arr[i]), font="Courier",
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


class individuo(Scene):
    def construct(self):
        n_bits = 10
        pai = set_box([0,1,2,3,4,5,6,7,8,9])
        pai.move_to(ORIGIN)
        text = Text("Cromossomo", font="Courier", font_size=50, color=RED)
        text.next_to(pai, DOWN)
        cromos = VGroup(pai, text)
        container = Rectangle(height=cromos.get_height()+0.8, width=cromos.get_width()+0.8, stroke_width=3, stroke_color=RED)
        container.move_to(cromos.get_center())
        text_2 = Text("Individuo", font="Courier", font_size=50, color=RED)
        text_2.next_to(container, DOWN)
        seta = Arrow(pai[3].get_top(), pai[3].get_top() + UP,color=RED, buff=0)
        text_3 = Text("Alelo", font="Courier", font_size=50, color=RED)
        text_3.next_to(seta, UP)
        self.add(container, cromos, text_2, seta, text_3)

class individuo_2(Scene):
    def construct(self):
        pai = set_box([0,2,3,4,9,10,5,6,7,11,15,18,17,14,16,13,8,12])
        pai.move_to(ORIGIN)
        pai.scale(0.7)
        
        self.add(pai)





class individuo_3(Scene):
    def construct(self):
        x = set_box([1,0,1,0,1,0,1,0,1,0,1,0,1])
        y = set_box([0,1,0,1,0,1,0,1,0,1,0,1,0])
        y.next_to(x, DOWN)
        coords = VGroup(x, y)
        container = Rectangle(height=coords.get_height()+0.8, width=coords.get_width()+0.8, stroke_width=3, stroke_color=RED)
        container.move_to(coords.get_center())
        groipss = VGroup(container, coords)
        groipss.move_to(ORIGIN)
        self.add(groipss)

class filho(Scene):
    def construct(self):
        text = Text("Filho 2", font="Courier", font_size=50, color=BLACK)
        text.move_to(ORIGIN)
        self.add(text)

class mutacao(Scene):
    def construct(self):

        inds_filhos = VGroup()
        inds_mutados = VGroup()
        val_inds_filhos = VGroup()
        val_inds_mutados = VGroup()
        n_inds = 5
        for i in range(n_inds):
            ind_arr = []
            ind_mutado_arr = []
            for i in range(10):
                randss = random.randint(0,1)
                ind_arr.append(randss)
                ind_mutado_arr.append(randss)
            for i in range(len(ind_arr)):
                if random.random() < 0.1:
                    if ind_arr[i] == 0:
                        ind_mutado_arr[i] = 1
                    else:
                        ind_mutado_arr[i] = 0
            ins_val = binary_to_range(ind_arr)
            ins_val_mutado = binary_to_range(ind_mutado_arr)
            ind = set_box(ind_arr)
            ind_mutado = set_box(ind_mutado_arr)
            for i in range(len(ind_mutado_arr)):
                if ind_mutado_arr[i] == ind_arr[i]:
                    ind_mutado[i].set_color(RED)
                else:
                    ind_mutado[i].set_color(BLUE)
            ind.move_to(ORIGIN)
            ind_mutado.next_to(ind, DOWN)

            inds_filhos.add(ind)
            inds_mutados.add(ind_mutado)
            color_muted = RED if ind_mutado_arr == ind_arr else BLUE
            val_inds_filhos.add(Text("= "+str(ins_val), font="Courier", font_size=50, color=RED))
            val_inds_mutados.add(Text("= "+str(ins_val_mutado), font="Courier", font_size=50, color=color_muted))
        
        for i in range(n_inds-1):
            inds_filhos[i+1].next_to(inds_filhos[i], DOWN)
            inds_mutados[i+1].next_to(inds_mutados[i], DOWN)
            val_inds_filhos[i+1].next_to(inds_filhos[i], DOWN)
            val_inds_mutados[i+1].next_to(inds_mutados[i], DOWN)

        val_inds_filhos.next_to(inds_filhos, RIGHT)
        
        inds_mutados.next_to(val_inds_filhos, RIGHT, buff=4)
        val_inds_mutados.next_to(inds_mutados, RIGHT)

        seta = Arrow(val_inds_filhos.get_right(), inds_mutados.get_left(), color=RED, buff=0.5)

        grupo = VGroup(inds_filhos, inds_mutados, val_inds_filhos, val_inds_mutados, seta)
        grupo.move_to(ORIGIN)
        grupo.scale(0.4)
        self.add(grupo)



def binary_to_range(binary_list):
    decimal_list = []
    for i in range(len(binary_list)-1, 0, -1):
        decimal_list.append(binary_list[i]*(2**i))
    innt = sum(decimal_list)
    rangess = [-2,2]
    return round((innt/(2**len(binary_list)))*(rangess[1]-rangess[0]) + rangess[0], 2)
