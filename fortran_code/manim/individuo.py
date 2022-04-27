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

class cromossomo_(Scene):
    def construct(self):
        n_bits = 16
        cromo = set_bits(n_bits)
        cromo.scale(0.7)
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


def set_decimals(n_decimais):
    arra_dec = [0.11,  -0.1, -0.1, 0.0, 0.0]
    decimals = VGroup()
    inds = []
    for i in range(n_decimais):
        # make a square with a random number inside fixed to 0.1
        randon = arra_dec[i]
        #randon = round(randon, 1)
        decimal_number = Text(str(randon), font="Courier",
                                font_size=50, color=BLACK)
        side_square = 2
        square = Rectangle(width=side_square, height=1.25, stroke_width=3, stroke_color=RED, fill_opacity=0)
        decimal_number.move_to(square.get_center())
        # make group with square and number 1
        group = VGroup(square, decimal_number)
        # move the left side plus 1/2 of the square for the right side of the previous square
        group.shift(RIGHT*(1.25*i)*side_square)
        group.set_color(RED)
        #if (i == 3 or i == 4):
            #group.set_color(BLUE)
        # make a magins between the squares
        # add group to the bits
        decimals.add(group)
        inds.append(randon)
    decimals.move_to(ORIGIN)
    evaluates = VGroup()
    for i in range(len(inds)):
        evaluate = np.exp(-(inds[i]**2))
        # evaluate to fixed 2
        evaluate = round(evaluate, 2)
        evaluate_number = Text(str(evaluate), font="Courier",
                                font_size=50, color=BLACK)
        side_square = 2
        square = Rectangle(width=side_square, height=1.25, stroke_width=3, stroke_color=BLUE, fill_opacity=0)
        evaluate_number.move_to(square.get_center())
        # make group with square and number 1
        group = VGroup(square, evaluate_number)
        group.set_color(RED)
        #if (i == 3 or i == 4):
         #   group.set_color(BLUE)
        # move the left side plus 1/2 of the square for the right side of the previous square
        group.shift(RIGHT*(1.25*i)*side_square)
        # make a magins between the squares
        # add group to the bits
        
        evaluates.add(group)
    evaluates.move_to(ORIGIN+DOWN*2)

    return VGroup(decimals, evaluates)

class decimals(Scene):
    def construct(self):
        decimals = set_decimals(5)
        # elvolve individuos with a box
        #width_decimal = decimals.get_width()
        #height_decimal = decimals.get_height()
        #box = Rectangle(width=width_decimal+1, height=height_decimal+1, stroke_width=3, stroke_color=BLACK,fill_opacity=0)
        #box.move_to(decimals)
        #decimal_box = VGroup(box, decimals)
        #decimal_box.set_color(RED)
        #decimals.set_color(RED)
        decimals.move_to(ORIGIN)
        #decimal_box.move_to(ORIGIN)

        self.add(decimals)
        