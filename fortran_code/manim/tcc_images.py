from distutils.dep_util import newer_group
import math
from operator import le
from re import X
from tkinter import font
from manim import *
from numpy import size
import random

config.background_color = "#fff"

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
                axes.coords_to_point(x, y),
                color=GREEN_A,
                stroke_width=3)

        axis_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        graph = axes.get_graph(
            lambda x: math.exp(-x**2), x_range=[-4, 4]).set_color(YELLOW).set_stroke(width=1)

        graphing_stuff = VGroup(axes, graph, axis_labels)

        self.play(Create(graphing_stuff))
        self.play(DrawBorderThenFill(group_lines))

        # new values for points
        new_group_lines = VGroup()

        # add points to graph
        for x in range(-4, 4, 1):
            y = math.exp(-(x/2)**2)
            # add x, y  to the array points
            new_group_lines += Dot(
                axes.coords_to_point(x/2, y),
                color=GREEN_A,
                stroke_width=3)

        """for i in range(len(group_lines)):
            self.play(ApplyMethod(group_lines[i].move_to, new_group_lines[i].get_all_points()[0]))"""

        #self.play(Transform(group_lines, group_lines, run_time=2, rate_function=linear))

        # self.add(points)


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
    return bits


class cromossomo(Scene):
    def construct(self):
        n_bits = 8

        pai = set_bits(n_bits)
        pai.set_color(RED)
        pai.move_to(UP*2)
        mae = set_bits(n_bits)
        mae.set_color(BLUE)
        mae.move_to(0.5*UP)

        pais = VGroup(pai, mae)

        mae_p1 = mae[0:4].copy()
        mae_p2 = mae[4:8].copy()
        mae_p1.shift(LEFT+DOWN)
        mae_p2.shift(RIGHT+DOWN)

        mae_sep = VGroup(mae_p1, mae_p2)

        pai_p1 = pai[0:4].copy()
        pai_p2 = pai[4:8].copy()
        pai_p1.shift(LEFT+DOWN)
        pai_p2.shift(RIGHT+DOWN)

        pai_sep = VGroup(pai_p1, pai_p2)

        pais_sep = VGroup(pai_sep, mae_sep)

        pais_sep.shift(DOWN*2)

        #self.add(pai, mae)

        self.add(pais_sep, pais)

        p1 = pais_sep[0][1].get_center()
        p2 = pais_sep[1][1].get_center()
        self.wait()
        self.play(pais_sep[1][1].animate.move_to(p1),
                  pais_sep[0][1].animate.move_to(p2), run_time=3)
        self.wait()
        self.play(pais_sep[0][0].animate.shift(RIGHT),
                  pais_sep[0][1].animate.shift(LEFT),
                  pais_sep[1][0].animate.shift(RIGHT),
                  pais_sep[1][1].animate.shift(LEFT), run_time=3)
        self.wait()


def threeDPoint(pos):
    x = pos[0]*2-1
    y = pos[1]*2-1
    z = pos[2]*2
    sphere = Surface(
        lambda u, v: np.array([
            np.cos(u) * np.cos(v),
            np.cos(u) * np.sin(v),
            np.sin(u)
        ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
        checkerboard_colors=[RED_D, RED_E], resolution=(15, 32)
    )
    sphere.move_to(ORIGIN)
    sphere.set_stroke(width=0)
    sphere.set_fill(GREEN, opacity=1)
    sphere.scale(0.1)
    sphere.shift(x * RIGHT + y * UP + z*OUT)

    return sphere


class ThreeDSurfacePlot(ThreeDScene):
    def construct(self):
        resolution_fa = 126
        self.set_camera_orientation(phi=45 * DEGREES, theta=10 * DEGREES)

        def function_exp(x, y):
            domain_exps = [[0,2], [0,2]]
            n_expx = 35
            exps = 0
            intervals = []
            for i in range(n_expx):
                intervals.append([round(random.uniform(0,1.5),1),round(random.uniform(0,1.5),1)])
            intervals = [[1.3, 1.4], [0.2, 1.3], [1.3, 1.3], [0.8, 1.1], [0.2, 0.5], [1.3, 0.2], [0.5, 0.4], [0.9, 0.3], [0.9, 0.9], [0.8, 0.5], [1.4, 0.5], [0.2, 0.8], [0.2, 0.7], [0.2, 1.2], [1.1, 0.1], [1.2, 1.1], [0.1, 0.9], [0.8, 0.3], [0.1, 0.6], [0.3, 1.3], [1.4, 1.0], [0.8, 0.6], [0.2, 0.6], [0.4, 0.5], [0.5, 1.0], [0.3, 0.2], [1.0, 0.4], [1.0, 0.9], [1.2, 0.6], [0.6, 1.3], [1.5, 1.2], [0.4, 0.8], [0.2, 0.9], [1.2, 1.4], [0.8, 0.7]]
            for i in range(n_expx):
                random_x = intervals[i][0]
                random_y = intervals[i][1]
                #random_x =1
                #random_y =1
                exps += 0.5*np.exp((-((x-random_x)**2+(y-random_y)**2))/0.002)
            return exps
            
            

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 1, [0.0, 0.0]
            d = np.linalg.norm(np.array([x, y]))
            #z = (np.cos(3*math.pi*d)**2)*np.exp(-(d ** 2 ))
            #z = np.exp(-(d ** 2 ))
            r1 = (x-1.5)**2 + (y-1.5)**2
            r2 = (x-1)**2 + (y-1)**2
            z = 0.8*np.exp(-(r1 )/(0.3**2))+0.879008*np.exp(-(r2 )/(0.03**2)) + function_exp(x, y)
            #z = function_exp(x, y)
            return np.array([x, y, z])

        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, +2],
            u_range=[-2, +2]
        )

        

        gauss_plane.scale(2, about_point=ORIGIN)
        #gauss_plane.set_fill(RED_A)
        gauss_plane.set_fill(RED)
        gauss_plane.set_opacity(0.9)
        #gauss_plane.set_stroke(RED, 1)
        #gauss_plane.set_sheen(0.3, 0.3, 0.3)
        axes = ThreeDAxes(x_range=[-2, 2], y_range=[-2, 2], z_range=[-2, 2])
        self.add(axes, gauss_plane)

      
