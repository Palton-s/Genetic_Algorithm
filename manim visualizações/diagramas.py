from manim import *

config.background_color = "#fff"

class dividir_conq(Scene):
    def construct(self):
        # draw a squadre 2x2
        sq = Rectangle(fill_color=RED, fill_opacity=0.5, width=7, height=7)
        sq2 = Rectangle(fill_color=RED, fill_opacity=0.2, width=3, height=4, stroke_width=0)
        sq2.shift(LEFT*3.5)
        self.add(sq, sq2)