from manim import *
import numpy as np
import random

config.background_color = "#fff"

class gaussian(Scene):
    def construct(self):
        axes = Axes(x_range=[-2, 2], y_range=[0, 1.5])
        self.add(axes)
        gaussian = lambda x: np.exp(-x**2)

        gaussian_graph = axes.plot(gaussian, color=BLUE)
        axes.set_color(BLACK)
        gaussian_graph.set_color(RED)
        plts = VGroup(axes, gaussian_graph)

        random_points = VGroup()
        for i in range(10):
            x = random.random()*0.25-0.125
            y = gaussian(x)
            random_points.add(Dot(axes.c2p(x, y), color=BLACK, radius=0.1, fill_opacity=0.5))
        text_geracao = Text("7ª Geracao", font="Courier", font_size=50, color=BLACK)
        text_geracao.next_to(plts, LEFT, buff=0)
        # zoom out
        grupo = VGroup(plts, random_points, text_geracao)
        funcss = Tex("f(x) = e^{-x^2}", color=RED, font="Courier", font_size=50)
        funcss.next_to(grupo, DOWN, buff=0)
        grupo.move_to(ORIGIN)
        grupo.scale(0.8)
        self.add(plts)

class gaussian_2(Scene):
    def construct(self):
        axes = Axes(x_range=[-2, 2], y_range=[0, 1.5])
        gaussian = lambda x: np.exp(-x**2)
        gaussian_graph = axes.plot(gaussian, color=BLUE)
        axes.set_color(BLACK)
        gaussian_graph.set_color(RED)
        
        text_func = Tex("f(x) = e^{-x^2}", color=RED, font="Courier", font_size=50)
        text_func.next_to(gaussian_graph, UL, buff=0)
        self.add(axes, gaussian_graph, text_func)

        
