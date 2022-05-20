from turtle import fillcolor
from main import *
from manim import *


def rgb2hex(rgb):
    return '#%s' % ''.join(['%02x' % rgb[0], '%02x' % rgb[1], '%02x' % rgb[2]])





config.background_color = '#CCC'



class Teste(Scene):
    def construct(self):
        cor_alvo_ = [50,150,190]
        resultado = procura_melhores_cores(paleta, cor_alvo_)

        cores_resultado = []
        for i in range(len(resultado)):
            cores_resultado.append(rgb2hex(resultado[i][4]))

        circles = VGroup()
        for i in range(len(cores_resultado)):
            circle = Circle(radius=1, color=cores_resultado[i], fill_opacity=1)
            # fillcolor(cores_resultado[i])
            circle.set_color(cores_resultado[i])
            circles.add(circle)
        for i in range(len(cores_resultado)):
            circles[i].move_to(RIGHT*3*i)
        circles.move_to(ORIGIN)
        self.add(circles)

        cinza = procura_melhor_cinza(cor_alvo_, resultado[0][4], resultado[0][2][1])

        cor_alvo = Circle(radius=1, color=rgb2hex(cor_alvo_), fill_opacity=1)
        cor_alvo.next_to(circles, DOWN)
        self.add(cor_alvo)
        