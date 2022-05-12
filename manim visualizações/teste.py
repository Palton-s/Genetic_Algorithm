import math as mt

from manim import *
from manim.utils import scale

config["background_color"] = "#0F1A26"


class Testing(Scene):
    def construct(self):
        name = Tex("Palton").to_edge(UL, buff=0.5)
        sq = Square(side_length=0.5, fill_color=GREEN,
                    fill_opacity=0.75).shift(LEFT*3)
        tri = Triangle().scale(0.6).to_edge(DR)
        self.play(Write(name))
        self.play(DrawBorderThenFill(sq), run_time=2)
        self.play(Create(tri))
        self.wait()

        self.play(name.animate.to_edge(UR), run_time=2)
        self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time=3)
        self.wait()


class Erros(Scene):
    def construct(self):

        ax = Axes()
        self.play(Create(ax, run_time=3))
        self.wait()


class LogScalingExample(Scene):
    def construct(self):
        rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UR)

        circ = Circle().to_edge(DOWN)

        arrow = always_redraw(
            lambda: Line(start=rect.get_center(),
                         end=circ.get_center()).add_tip()
        )

        self.play(FadeIn(VGroup(rect, circ, arrow)))
        self.play(rect.animate.to_edge(LEFT))
        self.wait()
        self.play(FadeOut(VGroup(rect, arrow)))
        self.play(circ.animate(rate_func=smooth).scale(0.5))
        self.play(circ.animate(rate_func=exponential_decay).to_edge(UP))


class Updaters(Scene):
    def construct(self):
        num = MathTex("ln(2)")
        box = always_redraw(lambda: SurroundingRectangle(
            num, color=RED_B, fill_opacity=0.4, fill_color=RED, buff=0.5)
        )

        name = always_redraw(lambda: Tex(
            "Palton").next_to(box, DOWN, buff=0.25)
        )

        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT*2), run_time=2)
        self.wait()


class ValueTrackers(Scene):
    def construct(self):

        k = ValueTracker(5)

        num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))

        self.play(FadeIn(num))
        self.wait()
        self.play(k.animate.set_value(0), run_time=5, rate_func=linear)
        self.wait()


class Graphing(Scene):
    def construct(self):

        k = ValueTracker(1)

        plane = NumberPlane(
            x_range=[-4, 4, 1], x_length=6, y_range=[0, 16, 4], y_length=6).to_edge(DOWN).add_coordinates()

        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")
        parab = plane.get_graph(lambda x: x**2, x_range=[-4, 4], color=GREEN)

        func_label = MathTex("f(x)=x^2").scale(
            0.6).next_to(parab, UL, buff=0.5)

        area = always_redraw(lambda: plane.get_riemann_rectangles(
            graph=parab, x_range=[-2, 3], dx=k.get_value(), stroke_width=0.1, stroke_color=WHITE
        ))

        self.play(DrawBorderThenFill(plane))
        self.play(FadeIn(VGroup(labels, parab, func_label)), run_time=3)
        self.wait()
        self.play(Create(area))
        self.play(k.animate.set_value(0.1), run_time=5, rate_func=linear)
        self.wait()


class UpdaterGraphing(Scene):
    def construct(self):

        k = ValueTracker(-4)

        polar = PolarPlane()

        ax = (Axes(x_range=[-4, 4, 1], y_range=[-1, 1, mt.pi/4], x_length=10,
              y_length=6)
              .to_edge(DOWN)
              .add_coordinates()).set_color(WHITE)
        func1 = ax.get_graph(lambda x: mt.cos(
            x)**2, x_range=[-4, 4], color=BLUE)
        func2 = ax.get_graph(lambda x: mt.sin(
            x)**2, x_range=[-4, 4], color=BLUE)
        slope = always_redraw(
            lambda:
            ax.get_secant_slope_group(
                x=k.get_value(), graph=func1, dx=0.001, secant_line_color=GREEN, secant_line_length=6)
        )

        pt = always_redraw(lambda: Dot().move_to(
            ax.c2p(k.get_value(), func1.underlying_function(k.get_value()))))

        self.play(Create(VGroup(ax, func1, slope, pt)))
        self.wait()
        self.play(k.animate.set_value(4), run_time=3, rate_func=smooth)
        self.play(k.animate.set_value(-2), run_time=3, rate_func=smooth)
        self.play(k.animate.set_value(1), run_time=3, rate_func=smooth)
        self.play(k.animate.set_value(0), run_time=3, rate_func=smooth)
        self.play(Transform(func1, func2), run_time=3)
        self.wait()


class bezier(Scene):
    def construct(self):

        t = ValueTracker(0)

        def lerp(a, b, t):
            return a*(1-t) + b*t

        P0 = always_redraw(lambda: Circle(radius=0.1, color=BLUE).set_stroke(
            color=BLUE, width=2).move_to(np.array((0.0, 3.0, 0.0))))
        P1 = always_redraw(lambda: Circle(radius=0.1, color=BLUE).set_stroke(
            color=BLUE, width=2).move_to(np.array((1.0, 1.0, 0.0))))
        P2 = always_redraw(lambda: Circle(radius=0.1, color=BLUE).set_stroke(
            color=BLUE, width=2).move_to(np.array((-5.0, 2.0, 0.0))))
        P3 = always_redraw(lambda: Circle(radius=0.1, color=BLUE).set_stroke(
            color=BLUE, width=2).move_to(np.array((3.0, 4.0, 0.0))))
        P4 = always_redraw(lambda: Circle(radius=0.1, color=BLUE).set_stroke(
            color=BLUE, width=2).move_to(np.array((4.0, 1.0, 0.0))))

        line1 = always_redraw(lambda: Line(
            P0.get_center(), P1.get_center()).set_stroke(color=GRAY, width=2))
        line2 = always_redraw(lambda: Line(
            P1.get_center(), P2.get_center()).set_stroke(color=GRAY, width=2))
        line3 = always_redraw(lambda: Line(
            P2.get_center(), P3.get_center()).set_stroke(color=GRAY, width=2))
        line4 = always_redraw(lambda: Line(
            P3.get_center(), P4.get_center()).set_stroke(color=GRAY, width=2))

        A = always_redraw(lambda: Circle(radius=0.1, color=BLUE).set_stroke(
            color=BLUE, width=2).move_to(lerp(P0.get_center(), P1.get_center(), t.get_value())))
        B = always_redraw(lambda: Circle(radius=0.1, color=BLUE).set_stroke(
            color=BLUE, width=2).move_to(lerp(P1.get_center(), P2.get_center(), t.get_value())))
        C = always_redraw(lambda: Circle(radius=0.1, color=BLUE).set_stroke(
            color=BLUE, width=2).move_to(lerp(P2.get_center(), P3.get_center(), t.get_value())))
        D = always_redraw(lambda: Circle(radius=0.1, color=BLUE).set_stroke(
            color=BLUE, width=2).move_to(lerp(P3.get_center(), P4.get_center(), t.get_value())))

        E = always_redraw(lambda: Circle(radius=0.1, color=BLUE).set_stroke(
            color=BLUE, width=2).move_to(lerp(A.get_center(), B.get_center(), t.get_value())))
        F = always_redraw(lambda: Circle(radius=0.1, color=BLUE).set_stroke(
            color=BLUE, width=2).move_to(lerp(C.get_center(), D.get_center(), t.get_value())))

        P = always_redraw(lambda: Point(
            lerp(E.get_center(), F.get_center(), t.get_value()), color=RED))

        lineA = always_redraw(lambda: Line(
            A.get_center(), B.get_center(), color=BLUE).set_stroke(color=BLUE, width=2))
        lineB = always_redraw(lambda: Line(
            C.get_center(), D.get_center(), color=BLUE).set_stroke(color=BLUE, width=2))
        lineC = always_redraw(lambda: Line(
            E.get_center(), F.get_center(), color=BLUE).set_stroke(color=BLUE, width=2))

        path = VMobject(stroke_width=2, stroke_color=RED_B)

        path.set_points_as_corners([P.get_center(), P.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([P.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)

        circ = always_redraw(lambda: Circle(
            radius=0.1, color=RED).move_to(P.get_center()))

        circA = always_redraw(lambda: Circle(radius=0.1, color=BLUE).set_stroke(
            color=BLUE, width=2).move_to(A.get_center()))

        self.add(P0, P1, P2, P3, P4, A, B, C, D, E, F, P, path)
        self.add(circ, circA)
        self.add(lineA, lineB, lineC, line1, line2, line3, line4)

        self.play(t.animate().set_value(0.5), run_time=2, rate_func=linear)
        self.play(t.animate().set_value(1), run_time=2, rate_func=linear)
        self.play(t.animate().set_value(0.5), run_time=2, rate_func=linear)
        self.wait(1)
        self.wait(1)

        self.wait()


class PointWithTrace(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        self.play(dot.animate().shift(DOWN), rate_func=smooth, run_time=3)
        self.wait()
        self.play(dot.animate().shift(UP))
        self.play(dot.animate().shift(LEFT))
        self.wait()


class line(Scene):
    def construct(self):
        line = Line(start=ORIGIN, end=UR*3)
        self.play(Create(line))
        self.wait()


class SquareCircle(Scene):
    def construct(self):
        circle = Circle(radius=2)
        square = Square()
        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.wait()


class BezierCurve(Scene):
    def construct(self):
        # create a circle then move the camera around the circle
        circle = Circle(radius=2)
        self.play(Create(circle))
        self.wait()
        self.play(ApplyMethod(circle.move_to, ORIGIN))
        self.wait()
        self.play(ApplyMethod(circle.move_to, UR*3))
        self.wait()
        self.play(ApplyMethod(circle.move_to, UL*3))
        self.wait()
        self.play(ApplyMethod(circle.move_to, ORIGIN))
        self.wait()


class CircleLines(Scene):
    def construct(self):
        circleRadius = 2
        circle = Circle(radius=circleRadius, stroke_width=2,
                        stroke_color="#B00001")
        circle2 = Circle(radius=0.4*circleRadius,
                         stroke_width=2, stroke_color="#B00001")
        circle3 = Circle(radius=0.6*circleRadius,
                         stroke_width=2, stroke_color="#B00001")
        circle4 = Circle(radius=0.8*circleRadius,
                         stroke_width=2, stroke_color="#B00001")
        circle5 = Circle(radius=0.3*circleRadius,
                         stroke_width=2, stroke_color="#B00001")

        # Create a line from the center of the circle to the edge of the circle
        n_lines = 101
        anglePattern = 2*np.pi/n_lines
        angle = 0
        times = 2*np.pi/anglePattern

        # add 10 lines from the center of the circle to the edge of the circle

        for i in range(int(times)):

            end = circleRadius*(UP*np.cos(angle) + RIGHT*np.sin(angle))
            start = circle.get_center() + 0.4*end

            self.add(Line(start, end, stroke_width=2, stroke_color="#B00001"))
            angle += anglePattern

        # add circle and line
        self.add(circle, circle2, circle3, circle4, circle5)

        k = ValueTracker(0)

        moovingLine = always_redraw(lambda: Line(
            circle.get_center(), circle.get_center() + 1.1*circleRadius*UP))

        # triangle
        triangle = always_redraw(lambda: Triangle(stroke_width=2, stroke_color="#B00001").scale(
            0.1)).move_to(circle.get_center() + 1.1*circleRadius*UP)

        seta = VGroup(triangle, moovingLine)

        self.add(seta)

        self.wait()
        self.play(seta.rotate(np.pi/2), run_time=2, rate_func=linear)

        self.wait()


class triangulo(Scene):
    def construct(self):
        # triangle
        triangle = Triangle(stroke_width=2, stroke_color="#B00001").scale(0.5)
        line = Line(start=ORIGIN, end=UR*3)
        # group with triangle and line
        group = VGroup(triangle, line)
        # add group to the scene
        self.add(group)
        self.wait()
        self.play(group.rotate(PI/3))
        self.wait()



class CircleExample(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.5)
        self.add(circle)

class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: UP*pos[0]**2 + RIGHT*pos[1]**2
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

class UnionExample(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=1).move_to([-2, 0, 0])
        cr = Circle(color=BLUE, fill_opacity=1).move_to([-1.3, 0.7, 0])
        un = Union(sq, cr, color=GREEN, fill_opacity=1).move_to([1.5, 0.3, 0])
        self.add(sq, cr, un)

class WarpSquare(Scene):
    def construct(self):
        square = Square()
        square.move_to(DOWN)
        self.play(
            ApplyPointwiseFunction(
                lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
                square,
            ),
        )
        self.wait()

#array with numbers from -10 to 10 using lambda function
array = np.array([lambda x: x - 10, lambda x: x, lambda x: x + 10])
print(array[:](0))

