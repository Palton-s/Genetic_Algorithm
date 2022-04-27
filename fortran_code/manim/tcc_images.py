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

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 1, [0.0, 0.0]
            d = np.linalg.norm(np.array([x, y]))
            #z = (np.cos(3*math.pi*d)**2)*np.exp(-(d ** 2 ))
            #z = np.exp(-(d ** 2 ))
            r1 = (x)**2 + (y)**2
            r2 = (x+1)**2 + (y+1)**2
            z = 0.8*np.exp(-(r1 )/(0.3**2))+0.879008*np.exp(-(r2 )/(0.03**2))
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

        """individuos = [[-1.94818169021358, -1.2996162097828505, 9.78365732898492e-05], [-0.6738277560368546, -1.858992457961019, 0.0009656423624013115], [1.7669463074962009, -1.8027746815319503, 0.0009998311132622755], [-0.08099580123949846, -1.989600096966404, 0.0014507642914383847], [-1.7131797734189997, 1.5142939127099289, 0.0026665844683042674], [-1.820715487441677, -0.22964778857965262, 0.002690290041583342], [-1.9048970997411292, 0.5092756907800364, 0.003077566478173798], [-1.017061552714945, -1.1451713379701873, 0.006683827436349807], [-1.5043037530816084, -0.18280102392420794, 0.011294371520461994], [-1.4387239371362028, 0.12432738293988033, 0.020246356660157335], [1.9891620982084928, 1.4054179035542411, 0.047960125367869845], [0.8541023225406481, -0.9943571908554452, 0.0945627287227092], [-0.8354301268169206, 1.1599233678618268, 0.10873163736784396], [0.12975264716703494, 1.922021614893484, 0.11541411998499534], [-0.20940975004158435, -0.6198323236773322, 0.17251231968336028], [1.7514276363244834, 0.7277042835279977, 0.19831068345492064], [1.6862392340218775, 0.9506940387811511, 0.199829927454382], [-0.35524463030427844, -0.42461795476839725, 0.20466889745517297], [0.07057466092604425, -0.5462169195884479, 0.27832216630283474], [0.9258397711011752, -0.5250847266456002, 0.29166826320742467], [1.325069601708611, -0.1736034259912329, 0.32158884662512943], [0.8337295473877617, 1.4568396812937219, 0.35810910139898783], [0.09046087139512782, 1.3316638326306673, 0.4234215481859689], [0.4168260548334004, 1.3889532736941135, 0.45060875209687734], [0.010198301541597843, 1.1212470382112336, 0.5348047316400706], [-0.28586302086748816, 0.5306838101162494, 0.5387400083241476], [1.1611230243241155, 0.6110201251316236, 0.6380050237349056], [0.24500871215859776, 0.8713926985376408, 0.8163165311588785], [0.8536897044782377, 0.6444072255495357, 0.8642010384574683], [0.28431195542240095, 0.3299474683059844, 0.9273361144635903]]

        for i in range(len(individuos)):
            x = individuos[i][0]
            y = individuos[i][1]
            z = individuos[i][2]
            sphere = threeDPoint([x,y,z])
            self.add(sphere)"""

      
