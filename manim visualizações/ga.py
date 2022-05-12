from distutils.dep_util import newer_group
import math
from operator import le
from manim import *

config.background_color = "#324d6a"

# make an animation for plotting the graph of the function


class Graph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-1, 2],
            stroke_width=1,
            # hide numbers
            axis_config={"include_tip": False, "numbers_to_exclude": [], "include_numbers": False})
        axes.to_edge(UR)

        group_lines = VGroup()

        # add points to graph
        for x in range(-4, 4, 1):
            y = math.exp(-x**2)
            # add x, y  to the array points
            group_lines += Dot(
                axes.coords_to_point(x,y),
                color=GREEN_A,
                stroke_width=3)

        

        axis_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        graph = axes.get_graph(
            lambda x: math.exp(-x**2), x_range=[-4, 4]).set_color(YELLOW).set_stroke(width=1)

        graphing_stuff = VGroup(axes, graph, axis_labels)

        self.play(Create(graphing_stuff))
        self.play(DrawBorderThenFill(group_lines))

        #new values for points
        new_group_lines = VGroup()

        # add points to graph
        for x in range(-4, 4, 1):
            y = math.exp(-(x/2)**2)
            # add x, y  to the array points
            new_group_lines += Dot(
                axes.coords_to_point(x/2,y),
                color=GREEN_A,
                stroke_width=3)

        
        """for i in range(len(group_lines)):
            self.play(ApplyMethod(group_lines[i].move_to, new_group_lines[i].get_all_points()[0]))"""


        #self.play(Transform(group_lines, group_lines, run_time=2, rate_function=linear))

        # self.add(points)
