from manim import *
import random

config.background_color = "#fff"

def set_box(my_arr):
    bits = VGroup()
    for i in range(len(my_arr)):
        # make a square with a number 1 inside
        square = Square(stroke_width=3, stroke_color=BLACK, side_length=1)
        bit_number = Text(str(my_arr[i]), font="Courier",
                          font_size=50, color=BLACK)
        bit_number.move_to(square.get_center())
        # make group with square and number 1
        group = VGroup(square, bit_number)
        # move the left side for the right side of the previous square
        group.shift(RIGHT*i * square.get_width())
        # add group to the bits
        bits.add(group)
    bits.move_to(ORIGIN)
    bits.set_color(RED)
    return bits

class Perm(Scene):
    def construct(self):
        n_vals = 10
        # Arranje of 10 values
        #vals = [i for i in range(n_vals)]
        # Randomize the values
        
        vals = [[0,1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,9,8], [0,1,2,3,4,5,6,9,7,8], [0,1,2,3,4,5,9,6,7,8]]
        boxs = VGroup()
        for i in range(4):
            random.shuffle(vals[i])
            box = set_box(vals[i])
            box.move_to(1.4*DOWN*i)
            boxs.add(box)
        threeDots = Text("...", font="Courier",)
        boxs.set_color(RED)
        boxs.move_to(ORIGIN)
        threeDots.rotate(PI/2)
        threeDots.next_to(boxs, DOWN)
        threeDots.set_color(RED)
        self.add(boxs, threeDots)



def individuos(n_vals, n_inds, percent_mut):
    # Arranje of 10 values
    vals = [i for i in range(n_vals)]
    # Randomize the values

    boxs = VGroup()
    for i in range(n_inds):
        random.shuffle(vals)
        box = set_box(vals)
        box.move_to(1.4*DOWN*i)
        boxs.add(box)
    container = Rectangle(height=boxs.get_height()+0.8, width=boxs.get_width()+0.8, stroke_width=3, stroke_color=RED)
    container.move_to(boxs.get_center())
    boxs.add(container)
    boxs.set_color(RED)
    boxs.move_to(ORIGIN)

    for i in range(n_inds):
        if random.random() < percent_mut:
            boxs[i].set_color(BLUE)
    boxs.scale(0.5)

    return boxs
    

        

class Perm_2(Scene):
    def construct(self):
        n_vals = 10
        n_inds = 8
        
        boxs_1 = individuos(n_inds, n_vals, 0.4)
        boxs_2 = individuos(n_inds, n_vals, 0.4)
        boxs_2.next_to(boxs_1, RIGHT, buff=2)
        texto_1 = Text("1ª Geração", font="Courier", color=RED)
        texto_2 = Text("2ª Geração", font="Courier", color=RED)
        texto_1.next_to(boxs_1, DOWN, buff=0.5)
        texto_2.next_to(boxs_2, DOWN, buff=0.5)
        seta = Arrow(boxs_1.get_right(), boxs_2.get_left(), color=RED)

        grupo = VGroup(boxs_1, boxs_2, seta, texto_1, texto_2)
        grupo.scale(0.8)
        grupo.move_to(ORIGIN)
        
        self.add(grupo)