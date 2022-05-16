from manim import *

config.background_color = "#fff"

class CalculusSlope(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-3, 3], y_range=[-4, 14], y_length=7, x_length=12, background_line_style={"stroke_width": 1, "stroke_color": BLACK}, color=BLACK
        ).add_coordinates()
        plane.set_color(BLACK)
        graph1 = plane.get_graph(lambda x: x**2)
        graph2 = plane.get_graph(lambda x: x**3)
        graph3 = plane.get_graph(lambda x: x**4)
        graph4 = plane.get_graph(lambda x: x**5)
        self.add(plane)
        self.play(Create(graph1))
        self.play(Create(graph2))
        self.play(Create(graph3))
        self.play(Create(graph4))
        self.wait(2)