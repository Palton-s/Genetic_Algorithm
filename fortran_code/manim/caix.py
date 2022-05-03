from manim import *
import random

config.background_color = "#fff"

def opcoes(number):
    opcao = Tex(str(number), font_size=30, color=BLACK)
    # circle
    contorno = Circle(stroke_width=3, stroke_color=BLACK, radius=0.3)
    contorno.move_to(opcao.get_center())
    ops = VGroup(contorno, opcao)
    ops.set_color(RED)
    return ops



class op(Scene):
    def construct(self):
        n_points = 10
        points = VGroup()
        random_points = [[4.872849308198155, -2.2409059053410405], [-2.4982124795431995, 1.048156406142997], [1.1920130320666287, -0.8458495018537917], [0.7611299157529228, 0.9894793558245141], [-2.1175877966292367, 2.706058382788937], [4.907307242096175, -1.2174958077678124], [4.285076083740545, -0.877719305001933], [-2.739897782238735, -0.23875607576379076], [0.860164248038231, -2.297226762916698], [2.663162762999206, -0.5506079251913305]]
        for i in range(n_points):
            opcao = opcoes(i)
            opcao.move_to(random_points[i][0]*RIGHT+ random_points[i][1]*UP)
            points.add(opcao)
        lines_sequence_1 = [0, 5,6,9,3,4,1,7,8,2, 0]
        lines_sequence_2 = [0, 3,1,2,9,0,6]
        lines = VGroup()
        for i in range(n_points):
            # add line between points
            line = Line(points[lines_sequence_1[i]].get_center(), points[lines_sequence_1[i+1]].get_center(), stroke_width=3, stroke_color=GREY, stroke_opacity=0.3)
            lines.add(line)
        for i in range(len(lines_sequence_2)-1):
            # add line between points
            line = Line(points[lines_sequence_2[i]].get_center(), points[lines_sequence_2[i+1]].get_center(), stroke_width=3, stroke_color=GREY, stroke_opacity=0.3)
            lines.add(line)
        lines = VGroup()
        self.add(points, lines)


points = []
for i in range(10):
    points.append([random.uniform(-5, 5), random.uniform(-3, 3)])

print(points)