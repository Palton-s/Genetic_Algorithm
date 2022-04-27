from distutils.dep_util import newer_group
import math
from operator import le
from re import X
from tkinter import font
from manim import *
from numpy import size
import random

config.background_color = "#fff"

def set_bits(n_bits):
    bits = VGroup()
    for i in range(n_bits):
        # make a square with a number 1 inside
        square = Square(stroke_width=3, stroke_color=BLACK, side_length=1)
        randon = random.randint(0, 1)
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

def set_especific_bits(sequ_bits):
    bits = VGroup()
    for i in range(len(sequ_bits)):
        # make a square with a number 1 inside
        square = Square(stroke_width=3, stroke_color=BLACK, side_length=1)
        randon = sequ_bits[i]
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

def set_especific_bits_colors(sequ_bits, mutation_form, mutation_color):
    bits = VGroup()
    for i in range(len(sequ_bits)):
        # make a square with a number 1 inside
        square = Square(stroke_width=3, stroke_color=BLACK, side_length=1)
        randon = sequ_bits[i]
        bit_number = Text(str(randon), font="Courier",
                          font_size=50, color=BLACK)
        bit_number.move_to(square.get_center())
        # make group with square and number 1
        group = VGroup(square, bit_number)
        # move the left side for the right side of the previous square
        group.shift(RIGHT*i * square.get_width())
        # add group to the bits
        bits.add(group)
    for i in range(len(mutation_form)):
        bits[i].set_color(mutation_color[mutation_form[i]])


    bits.move_to(ORIGIN)
    return bits




def cromossomo():
    n_bits = 8

    pai = set_bits(n_bits)
    pai.set_color(RED)
    pai.move_to(UP*2)
    mae = set_bits(n_bits)
    mae.set_color(BLUE)
    mae.move_to(0.5*UP)

    pais = VGroup(pai, mae)
    pais.set_color(RED)

    return pais

class pais(Scene):
    def construct(self):
        string_pai = "1001001110011000"
        string_mae = "1011100010001100"
        pai = set_especific_bits(string_pai)
        mae = set_especific_bits(string_mae)
        pai.move_to(UP)
        mae.move_to(DOWN)
        
        text_individuo_1 = Text("Indivíduo 1", font="Courier", color=BLACK, font_size=50)
        text_individuo_1.move_to(pai.get_right() + text_individuo_1.get_width()*RIGHT/2 + 0.3*RIGHT)
        text_individuo_2 = Text("Indivíduo 2", font="Courier", color=BLACK, font_size=50)
        text_individuo_2.move_to(mae.get_right() + text_individuo_2.get_width()*RIGHT/2 + 0.3*RIGHT)
        pais = VGroup(pai, mae, text_individuo_1, text_individuo_2)
        pais.move_to(ORIGIN)
        pais.scale(0.5)

        self.add(pais)

class cromossomo_(Scene):
    def construct(self):
        n_bits = 16
        cromo = set_bits(n_bits)
        cromo.scale(0.9)
        
        #cut the camera to fit the screen
        self.camera.set_frame_width(n_bits*0.9)
        self.camera.set_frame_height(0.9)







        self.add(cromo)



class individuo(Scene):
    def construct(self):
        individuos = cromossomo()
        # elvolve individuos with a box
        width_individuo = individuos.get_width()
        height_individuo = individuos.get_height()
        box = Rectangle(width=width_individuo+1, height=height_individuo+1, stroke_width=3, stroke_color=BLACK,fill_opacity=0)
        box.move_to(individuos)
        individuo_box = VGroup(box, individuos)
        individuo_box.set_color(RED)
        individuo_box.move_to(ORIGIN)
        individuo_box.scale(1.5)

        self.add(individuo_box)

class cromossomo_especifico(Scene):
    def construct(self):
        sequ_bits_1 = []
        sequ_bits_2 = []
        bits = 16
        # select 4 diferente numbers between 0 and 16
        random_list = random.sample(range(0, bits), 4)
        
        for i in range(bits):
            sequ_bits_1.append(random.randint(0, 1))
            sequ_bits_2.append(random.randint(0, 1))
        
        bits_str_1 = ''.join(str(e) for e in sequ_bits_1)
        bits_str_2 = ''.join(str(e) for e in sequ_bits_2)

        mutation_form = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

        cromo_1 = set_especific_bits_colors(sequ_bits_1, mutation_form, [RED, BLUE])
        decimal_bits_1 = (int(bits_str_1, 2)*10)/(2**bits-1) - 5
        # to fixed 2
        decimal_bits_1 = round(decimal_bits_1, 2)
        decimal_bits_1_text = Text(" = "+str(decimal_bits_1), font="Courier",
                            font_size=50, color=BLACK)
        decimal_bits_1_text.move_to(cromo_1.get_right() + (decimal_bits_1_text.get_width()/2 +0.5)*RIGHT )

        cromo_2 = set_especific_bits_colors(sequ_bits_2, mutation_form, [BLUE, RED])
        decimal_bits__2 = (int(bits_str_2, 2)*10)/(2**bits-1) - 5
        # to fixed 2
        decimal_bits_2 = round(decimal_bits__2, 2)
        decimal_bits_2_text = Text(" = "+str(decimal_bits_2), font="Courier",
                            font_size=50, color=BLACK)
        decimal_bits_2_text.move_to(cromo_2.get_right() + (decimal_bits_2_text.get_width()/2 +0.5)*RIGHT )


        cromo_with_decimal_1 = VGroup(cromo_1, decimal_bits_1_text)
        cromo_with_decimal_1.scale(0.7)
        cromo_with_decimal_1.move_to(ORIGIN)

        cromo_with_decimal_2 = VGroup(cromo_2, decimal_bits_2_text)
        cromo_with_decimal_2.scale(0.7)
        cromo_with_decimal_2.move_to(DOWN)

        cromos = VGroup(cromo_with_decimal_1, cromo_with_decimal_2)
        cromos.move_to(ORIGIN)
        
        # arrow from top to bottom with 1 os height
        arrow = Arrow(DOWN, 2*DOWN, buff=0, color=BLACK)

        son_1_bits = []
        son_2_bits = []
        for i in range(bits):
            if(mutation_form[i] == 1):
                son_1_bits.append(sequ_bits_2[i])
                son_2_bits.append(sequ_bits_1[i])
            else:
                son_1_bits.append(sequ_bits_1[i])
                son_2_bits.append(sequ_bits_2[i])
        
        son_1 = set_especific_bits_colors(son_1_bits, mutation_form, [RED, RED])
        decimal_bits_son_1 = (int(''.join(str(e) for e in son_1_bits), 2)*10)/(2**bits-1) - 5
        # to fixed 2
        decimal_bits_son_1 = round(decimal_bits_son_1, 2)
        decimal_bits_son_1_text = Text(" = "+str(decimal_bits_son_1), font="Courier",
                            font_size=50, color=BLACK)
        decimal_bits_son_1_text.move_to(son_1.get_right() + (decimal_bits_son_1_text.get_width()/2 +0.5)*RIGHT )
        
        son_2 = set_especific_bits_colors(son_2_bits, mutation_form, [BLUE, BLUE])
        decimal_bits_son_2 = (int(''.join(str(e) for e in son_2_bits), 2)*10)/(2**bits-1) - 5
        # to fixed 2
        decimal_bits_son_2 = round(decimal_bits_son_2, 2)
        decimal_bits_son_2_text = Text(" = "+str(decimal_bits_son_2), font="Courier",
                            font_size=50, color=BLACK)
        decimal_bits_son_2_text.move_to(son_2.get_right() + (decimal_bits_son_2_text.get_width()/2 +0.5)*RIGHT )

        son_1_with_decimal = VGroup(son_1, decimal_bits_son_1_text)
        son_1_with_decimal.scale(0.7)
        son_1_with_decimal.move_to(2.5*DOWN)

        son_2_with_decimal = VGroup(son_2, decimal_bits_son_2_text)
        son_2_with_decimal.scale(0.7)
        son_2_with_decimal.move_to(3.5*DOWN)

        sons = VGroup(son_1_with_decimal, son_2_with_decimal)

        all = VGroup(cromos, arrow, sons)

        all.move_to(UP)
        
        self.add(all)



class mutacao(Scene):
    def construct(self):
        sequ_bits_1 = []

        bits = 16
        # select 4 diferente numbers between 0 and 16
        random_list = random.sample(range(0, bits), 4)
        
        for i in range(bits):
            sequ_bits_1.append(random.randint(0, 1))
        
        bits_str_1 = ''.join(str(e) for e in sequ_bits_1)

        mutation_form = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]

        cromo_1 = set_especific_bits_colors(sequ_bits_1, mutation_form, [RED, BLUE])
        decimal_bits_1 = (int(bits_str_1, 2)*10)/(2**bits-1) - 5
        # to fixed 2
        decimal_bits_1 = round(decimal_bits_1, 2)
        decimal_bits_1_text = Text(" = "+str(decimal_bits_1), font="Courier",
                            font_size=50, color=BLACK)
        decimal_bits_1_text.move_to(cromo_1.get_right() + (decimal_bits_1_text.get_width()/2 +0.5)*RIGHT )



        cromo_with_decimal_1 = VGroup(cromo_1, decimal_bits_1_text)
        cromo_with_decimal_1.scale(0.7)
        cromo_with_decimal_1.move_to(ORIGIN)


        cromos = VGroup(cromo_with_decimal_1)
        cromos.move_to(ORIGIN)
        
        # arrow from top to bottom with 1 os height
        arrow = Arrow(0.5*DOWN, 1.5*DOWN, buff=0, color=BLACK)

        son_1_bits = []

        for i in range(bits):
            if(mutation_form[i] == 1):
                if(sequ_bits_1[i] == 0):
                    son_1_bits.append(1)
                else:
                    son_1_bits.append(0)
            else:
                son_1_bits.append(sequ_bits_1[i])
        
        son_1 = set_especific_bits_colors(son_1_bits, mutation_form, [RED, BLUE])
        decimal_bits_son_1 = (int(''.join(str(e) for e in son_1_bits), 2)*10)/(2**bits-1) - 5
        # to fixed 2
        decimal_bits_son_1 = round(decimal_bits_son_1, 2)
        decimal_bits_son_1_text = Text(" = "+str(decimal_bits_son_1), font="Courier",
                            font_size=50, color=BLACK)
        decimal_bits_son_1_text.move_to(son_1.get_right() + (decimal_bits_son_1_text.get_width()/2 +0.5)*RIGHT )


        son_1_with_decimal = VGroup(son_1, decimal_bits_son_1_text)
        son_1_with_decimal.scale(0.7)
        son_1_with_decimal.move_to(2*DOWN)

        sons = VGroup(son_1_with_decimal)

        all = VGroup(cromos, arrow, sons)

        all.move_to(UP)
        

        self.add(all)