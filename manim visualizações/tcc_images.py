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
        #resolution_fa = 50
        
        resolution_fa = 64
        self.set_camera_orientation(phi=45 * DEGREES, theta=10 * DEGREES)

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 1, [0.0, 0.0]
            d = np.linalg.norm(np.array([x, y]))
            #z = (np.cos(3*math.pi*d)**2)*np.exp(-(d ** 2 ))
            #z = np.exp(-(d ** 2 ))
            r1 = (x+1.5)**2 + (y-1.5)**2
            r2 = (x-1.0)**2 + (y+1.0)**2
            r3 = (x-1.02753)**2 + (y-1.5793)**2
            random_points = [[-0.5730190814373182, 1.1133101800664646], [-1.4861996650438938, -0.9004050816703724], [0.14868370307354528, -1.0277901981840407], [-1.5040675371220051, -0.10140018583878385], [0.2812806120517575, -0.9959156311503494], [-0.6326965728809371, -1.418631009015305], [-1.2008288252188888, -1.018523020048121], [-1.3823626040359085, 0.9457646097217305], [0.06793665643720814, 0.13559733521599027], [0.06231283662861209, -1.5281672275173213], [0.6499383094521569, -0.9527253123032335], [0.197410307436106, -1.9329924913188519], [0.6472051107462717, -0.294726397400479], [1.675630843751076, 0.0035076663160631405], [-0.728139876424577, -0.15903522727604358], [-0.6465846139006248, -0.10370495025819082], [-0.5777388022198418, 1.6879456952576715], [1.624504101046897, 1.8924824126833988], [0.14051163937017241, 0.7971860143882821], [1.0244134762484145, 1.2637928589945093], [1.5171922278754528, 0.7509318175163733], [-0.035051964737847996, -0.20965739172816766], [-0.7441397363890636, -0.3613044402517649], [-1.281445256809286, 0.5649705367154598], [0.9200562966770782, -1.5109509705900406], [0.21949226652130926, 0.9546359751026312], [0.05457392339016298, -0.5446744815551088], [1.4303375998703602, 0.17112424562522666], [0.90841034719858, -1.777192373903834], [1.80758124295485, -1.1997604962699522], [-0.2673414328256176, 1.5733944746188002], [-0.4035346806276414, -0.1879654192335818], [1.9260899693369828, 0.32208297738343594], [-0.9180044980208866, 1.9948416596986545], [-0.7862003920916831, -1.5906197537237876], [0.6441753892468367, 1.9055693838815966], [-0.6903157415114718, 1.3154910802216593], [-1.0032423269755704, -0.6702249853882183], [1.3611935630322218, 0.1465163936983389], [-0.35978621504604824, -1.6628604520689083], [0.7027317085709708, -1.9751168368384873], [-0.30207289896281875, 1.2593835605300079], [-0.17046917046567422, 1.64109750506088], [-0.3942080786630764, -0.6468992901613517], [0.5171317623414105, -0.7959576691418069], [0.6037371534931117, 1.8577542847500275], [1.4256559909746258, -0.30832053345692056], [0.7748582482006134, 0.5131240574314124], [0.47917311875408375, 1.6284594169501658], [1.4936150679848597, -1.0371548810661149], [1.8245316438796517, 0.7339956017101716], [-0.5683086465688163, -0.03789192339008984], [1.7301377359917653, -1.0039682274841222], [-1.6278665617390988, -0.726943533795958], [0.9002833009383266, -0.9193136531206525], [1.431622783747851, 1.06348249979666], [-0.5299773294007166, -0.6488270002622314], [0.537396950971579, -0.601133302574318], [-0.3833435303732511, 0.15908161130923038], [1.4631243123945468, -0.5886376176334851]]
            z = 0
            z += 0.8*np.exp(-(r1 )/(0.3**2))
            z += 0.879008*np.exp(-(r2 )/(0.03**2))
            z += 1.5345*np.exp(-(r3 )/(0.03**2))
            for i in range(len(random_points)):
                #z += 0.6*np.exp(-((x-random_points[i][0])**2 + (y-random_points[i][1])**2)/(0.06**2))
                z += ((i/len(random_points))*0.3+0.3)*np.exp(-((x-random_points[i][0])**2 + (y-random_points[i][1])**2)/(0.06**2))
            return np.array([x, y, z])

        """gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2.5, +2.5],
            u_range=[-2.5, +2.5]
        )

        gauss_plane.scale(2, about_point=ORIGIN)
        #gauss_plane.set_fill(RED_A)
        gauss_plane.set_fill(RED)
        gauss_plane.set_opacity(0.9)
        self.add(gauss_plane)
        """
        # 9 gauss planes
        gaus_planes = VGroup()
        n_cortes = 9
        range_ = 2.5
        sq = int(np.sqrt(n_cortes))
        for i in range(sq-1, -1, -1):
            for j in range(sq):
                gauss_plane = Surface(
                    param_gauss,
                    resolution=(resolution_fa, resolution_fa),
                    v_range=[-range_+i*range_*2/sq, -range_+(i+1)*range_*2/sq],
                    u_range=[-range_+j*range_*2/sq, -range_+(j+1)*range_*2/sq]
                )
                gauss_plane.scale(1.5, about_point=ORIGIN)
                gauss_plane.set_fill(RED)                
                gauss_plane.set_opacity(0.9)
                #gauss_plane.shift((i-1)*RIGHT*2+(j-1)*UP*2)
                gaus_planes.add(gauss_plane)
        self.add(gaus_planes)
        

        # space each gauss plane by 1
        gaus_planes.arrange_in_grid(buff=0.2)
        # move all gauss bottom to z = 0
        for i in range(len(gaus_planes)):
            # move bottom to z = 0
            bottom_point = gaus_planes[i].get_corner(DOWN)
            gaus_planes[i].shift(-bottom_point[2]*UP)


        #gauss_plane.set_stroke(RED, 1)
        #gauss_plane.set_sheen(0.3, 0.3, 0.3)
        axes = ThreeDAxes(x_range=[-2, 2], y_range=[-2, 2], z_range=[-2, 2])
        #self.add(axes)

        """individuos = [[-1.94818169021358, -1.2996162097828505, 9.78365732898492e-05], [-0.6738277560368546, -1.858992457961019, 0.0009656423624013115], [1.7669463074962009, -1.8027746815319503, 0.0009998311132622755], [-0.08099580123949846, -1.989600096966404, 0.0014507642914383847], [-1.7131797734189997, 1.5142939127099289, 0.0026665844683042674], [-1.820715487441677, -0.22964778857965262, 0.002690290041583342], [-1.9048970997411292, 0.5092756907800364, 0.003077566478173798], [-1.017061552714945, -1.1451713379701873, 0.006683827436349807], [-1.5043037530816084, -0.18280102392420794, 0.011294371520461994], [-1.4387239371362028, 0.12432738293988033, 0.020246356660157335], [1.9891620982084928, 1.4054179035542411, 0.047960125367869845], [0.8541023225406481, -0.9943571908554452, 0.0945627287227092], [-0.8354301268169206, 1.1599233678618268, 0.10873163736784396], [0.12975264716703494, 1.922021614893484, 0.11541411998499534], [-0.20940975004158435, -0.6198323236773322, 0.17251231968336028], [1.7514276363244834, 0.7277042835279977, 0.19831068345492064], [1.6862392340218775, 0.9506940387811511, 0.199829927454382], [-0.35524463030427844, -0.42461795476839725, 0.20466889745517297], [0.07057466092604425, -0.5462169195884479, 0.27832216630283474], [0.9258397711011752, -0.5250847266456002, 0.29166826320742467], [1.325069601708611, -0.1736034259912329, 0.32158884662512943], [0.8337295473877617, 1.4568396812937219, 0.35810910139898783], [0.09046087139512782, 1.3316638326306673, 0.4234215481859689], [0.4168260548334004, 1.3889532736941135, 0.45060875209687734], [0.010198301541597843, 1.1212470382112336, 0.5348047316400706], [-0.28586302086748816, 0.5306838101162494, 0.5387400083241476], [1.1611230243241155, 0.6110201251316236, 0.6380050237349056], [0.24500871215859776, 0.8713926985376408, 0.8163165311588785], [0.8536897044782377, 0.6444072255495357, 0.8642010384574683], [0.28431195542240095, 0.3299474683059844, 0.9273361144635903]]

        for i in range(len(individuos)):
            x = individuos[i][0]
            y = individuos[i][1]
            z = individuos[i][2]
            sphere = threeDPoint([x,y,z])
            self.add(sphere)"""

class superficies_separadas(ThreeDScene):
    def construct(self):
        #resolution_fa = 50
        
        resolution_fa = 8
        self.set_camera_orientation(phi=45 * DEGREES, theta=10 * DEGREES)

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 1, [0.0, 0.0]
            d = np.linalg.norm(np.array([x, y]))
            #z = (np.cos(3*math.pi*d)**2)*np.exp(-(d ** 2 ))
            #z = np.exp(-(d ** 2 ))
            r1 = (x+1.5)**2 + (y-1.5)**2
            r2 = (x-1.0)**2 + (y+1.0)**2
            r3 = (x-1.02753)**2 + (y-1.5793)**2
            random_points = [[-0.5730190814373182, 1.1133101800664646], [-1.4861996650438938, -0.9004050816703724], [0.14868370307354528, -1.0277901981840407], [-1.5040675371220051, -0.10140018583878385], [0.2812806120517575, -0.9959156311503494], [-0.6326965728809371, -1.418631009015305], [-1.2008288252188888, -1.018523020048121], [-1.3823626040359085, 0.9457646097217305], [0.06793665643720814, 0.13559733521599027], [0.06231283662861209, -1.5281672275173213], [0.6499383094521569, -0.9527253123032335], [0.197410307436106, -1.9329924913188519], [0.6472051107462717, -0.294726397400479], [1.675630843751076, 0.0035076663160631405], [-0.728139876424577, -0.15903522727604358], [-0.6465846139006248, -0.10370495025819082], [-0.5777388022198418, 1.6879456952576715], [1.624504101046897, 1.8924824126833988], [0.14051163937017241, 0.7971860143882821], [1.0244134762484145, 1.2637928589945093], [1.5171922278754528, 0.7509318175163733], [-0.035051964737847996, -0.20965739172816766], [-0.7441397363890636, -0.3613044402517649], [-1.281445256809286, 0.5649705367154598], [0.9200562966770782, -1.5109509705900406], [0.21949226652130926, 0.9546359751026312], [0.05457392339016298, -0.5446744815551088], [1.4303375998703602, 0.17112424562522666], [0.90841034719858, -1.777192373903834], [1.80758124295485, -1.1997604962699522], [-0.2673414328256176, 1.5733944746188002], [-0.4035346806276414, -0.1879654192335818], [1.9260899693369828, 0.32208297738343594], [-0.9180044980208866, 1.9948416596986545], [-0.7862003920916831, -1.5906197537237876], [0.6441753892468367, 1.9055693838815966], [-0.6903157415114718, 1.3154910802216593], [-1.0032423269755704, -0.6702249853882183], [1.3611935630322218, 0.1465163936983389], [-0.35978621504604824, -1.6628604520689083], [0.7027317085709708, -1.9751168368384873], [-0.30207289896281875, 1.2593835605300079], [-0.17046917046567422, 1.64109750506088], [-0.3942080786630764, -0.6468992901613517], [0.5171317623414105, -0.7959576691418069], [0.6037371534931117, 1.8577542847500275], [1.4256559909746258, -0.30832053345692056], [0.7748582482006134, 0.5131240574314124], [0.47917311875408375, 1.6284594169501658], [1.4936150679848597, -1.0371548810661149], [1.8245316438796517, 0.7339956017101716], [-0.5683086465688163, -0.03789192339008984], [1.7301377359917653, -1.0039682274841222], [-1.6278665617390988, -0.726943533795958], [0.9002833009383266, -0.9193136531206525], [1.431622783747851, 1.06348249979666], [-0.5299773294007166, -0.6488270002622314], [0.537396950971579, -0.601133302574318], [-0.3833435303732511, 0.15908161130923038], [1.4631243123945468, -0.5886376176334851]]
            z = 0
            z += 0.8*np.exp(-(r1 )/(0.3**2))
            z += 0.879008*np.exp(-(r2 )/(0.03**2))
            z += 1.5345*np.exp(-(r3 )/(0.03**2))
            for i in range(len(random_points)):
                #z += 0.6*np.exp(-((x-random_points[i][0])**2 + (y-random_points[i][1])**2)/(0.06**2))
                z += ((i/len(random_points))*0.3+0.3)*np.exp(-((x-random_points[i][0])**2 + (y-random_points[i][1])**2)/(0.06**2))
            return np.array([x, y, z])

        """gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2.5, +2.5],
            u_range=[-2.5, +2.5]
        )

        gauss_plane.scale(2, about_point=ORIGIN)
        #gauss_plane.set_fill(RED_A)
        gauss_plane.set_fill(RED)
        gauss_plane.set_opacity(0.9)
        self.add(gauss_plane)
        """
        # 9 gauss planes
        gaus_planes = VGroup()
        n_cortes = 9
        from_range = 5/6
        to_range = 2.5
        range_ = to_range - from_range
        sq = int(np.sqrt(n_cortes))
        for i in range(sq-1, -1, -1):
            for j in range(sq):
                gauss_plane = Surface(
                    param_gauss,
                    resolution=(resolution_fa, resolution_fa),
                    v_range=[from_range + (range_/sq)*i, from_range + (range_/sq)*(i+1)],
                    u_range=[from_range + (range_/sq)*j, from_range + (range_/sq)*(j+1)]
                )
                gauss_plane.scale(4, about_point=ORIGIN)
                gauss_plane.set_fill(RED)                
                gauss_plane.set_opacity(0.9)
                #gauss_plane.shift((i-1)*RIGHT*2+(j-1)*UP*2)
                gaus_planes.add(gauss_plane)
        
        

        # space each gauss plane by 1
        gaus_planes.arrange_in_grid(buff=1)
        #gaus planes to center
        gaus_planes.move_to(ORIGIN)
        # move all gauss bottom to z = 0
        for i in range(len(gaus_planes)):
            # move bottom to z = 0
            bottom_point = gaus_planes[i].get_corner(DOWN)
            gaus_planes[i].shift(-bottom_point[2]*OUT)
        self.add(gaus_planes)
"""coords = []  
for i in range(60):
    x = np.random.uniform(-2,2)
    y = np.random.uniform(-2,2)
    coords.append([x,y])
print(coords)"""
