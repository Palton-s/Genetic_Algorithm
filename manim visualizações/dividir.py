from manim import *

config.background_color = "#fff"

"""class dividir_conq(Scene):
    def construct(self):
        # draw a squadre 2x2 transparent and stroke black
        squares = VGroup()
        for i in range(20*20):
            sq = Square(side_length=1, fill_opacity=0, stroke_width=1, stroke_color="#000")
            squares.add(sq)
        squares.arrange_in_grid(20,20, buff=0)
        squares.scale(0.35)
        squares.move_to(ORIGIN)
        # put points 
        self.add(squares)"""

class dividir_conq(Scene):
    def construct(self):
        size = 5**2
        # points
        points = VGroup()
        for i in range(size*size):
            p = Dot(fill_color="#000", fill_opacity=1, radius=0.01)
            points.add(p)
        points.arrange_in_grid(size,size, buff=0.1)

        box = SurroundingRectangle(points, buff=0.1, color="#000", stroke_width=1)
        points.add(box)
        
        #ajust width and height to 5
        points.scale(7/points.get_width())
        # x scale
        
        points.move_to(ORIGIN)
        #points.scale(0.3)
        points.move_to(ORIGIN)
        points.set_color("#000")
        #box enclosing points with buf 1
        
        # put points
        self.add(points)