from turtle import right
from manim import *
import random

config.background_color = "#fff"

class box_1(Scene):
    def construct(self):
        n_bits = 10
        #a image of a box red
        boxes = VGroup()
        n_cortes = 3
        n_dim = 2
        # a box 6x6
        box_big = Rectangle(height=6, width=6, stroke_width=3, stroke_color=RED)
        for i in range(n_cortes**n_dim):
            box = Rectangle(height=2, width=2, stroke_width=3, stroke_color=RED)
            # fill red with random alpha
            box.set_fill(RED, opacity=0.7*random.random())
            box.move_to(ORIGIN)
            boxes.add(box)
        
        # arrange boxes in a grid
        boxes.arrange_in_grid(n_rows=n_cortes, n_cols=n_cortes, buff=0.4)
        # add a Brace legend on top of the first box informing the width and height
        boxes[0].set_fill(RED, opacity=0.8)
        brace_l = Brace(boxes[0], direction=UP)
        text_l = brace_l.get_text("2x2")
        # add a Brace legend on top of the first box informing the width and height
        brace_2_l = Brace(boxes[0], direction=LEFT)
        text_2_l = brace_2_l.get_text("2x2")
        # box bix left boxes    
        box_big.next_to(boxes, LEFT, buff=2)
        # add a Brace legend on top of big_box informing the width and height
        brace = Brace(box_big, UP)
        text = brace.get_text("6x6")
        # add a Brace legend on left of big_box informing the width and height
        brace_2 = Brace(box_big, LEFT)
        text_2 = brace_2.get_text("6x6")

        #arrow from box_big to boxes
        seta = Arrow(box_big.get_right(), boxes.get_left(), color=RED)
        group_all = VGroup(box_big, boxes, seta, text, brace, text_2, brace_2, brace_l, text_l, brace_2_l, text_2_l)
        group_all.set_color(RED)
        # scale to 0.5
        group_all.scale(0.8)
        # move to the center
        group_all.move_to(ORIGIN)
        self.add(group_all)
        

class box_2(Scene):
    def construct(self):
        n_bits = 10
        #a image of a box red
        boxes = VGroup()
        n_cortes = 3
        n_dim = 2
        # a box 6x6
        box_big = Rectangle(height=6, width=6, stroke_width=3, stroke_color=RED, fill_color=RED, fill_opacity=0.3)
        for i in range(n_cortes**n_dim):
            box = Rectangle(height=2, width=2, stroke_width=3, stroke_color=RED)
            # fill red with random alpha
            box.set_fill(RED, opacity=0.5*random.random())
            box.move_to(ORIGIN)
            boxes.add(box)
        
        # arrange boxes in a grid
        boxes.arrange_in_grid(n_rows=n_cortes, n_cols=n_cortes, buff=0.4)
        boxes[2].set_fill(RED, opacity=0)
        boxes[2].set_stroke(RED, width=0)

        small_boxes = VGroup()
        for i in range(n_cortes**n_dim):
            small_box = Rectangle(height=2/3, width=2/3, stroke_width=2, stroke_color=RED)
            # fill red with random alpha
            small_box.set_fill(RED, opacity=0.5+0.2*random.random())
            small_boxes.add(small_box)
        #arrange small boxes in a grid
        small_boxes.arrange_in_grid(n_rows=n_cortes, n_cols=n_cortes, buff=0.1)
        # shift up right
        
        
        #position inside of boxes[2]
        small_boxes.move_to(boxes[2].get_center())
        small_boxes.shift(0.5*RIGHT+0.5*UP)
        # scale for 1.5
        small_boxes.scale(1.3)
        selected_box = 8
        small_boxes[selected_box].set_fill(RED, opacity=0)
        small_boxes[selected_box].set_stroke(RED, width=0)
        small_small_boxes = VGroup()
        for i in range(n_cortes**n_dim):
            small_small_box = Rectangle(height=2/9, width=2/9, stroke_width=2, stroke_color=RED)
            # fill red with random alpha
            small_small_box.set_fill(RED, opacity=0.7+0.3*random.random())
            small_small_boxes.add(small_small_box)
        #arrange small boxes in a grid
        small_small_boxes.arrange_in_grid(n_rows=n_cortes, n_cols=n_cortes, buff=0.05)
        #position inside of boxes[selected_box]
        small_small_boxes.move_to(small_boxes[selected_box].get_center())
        small_small_boxes.shift(0.5*RIGHT+0.5*DOWN)
        # scale for 1.5
        small_small_boxes.scale(2)

        small_small_boxes[selected_box].set_fill(RED, opacity=0)
        small_small_boxes[selected_box].set_stroke(RED, width=0)

        smaill_small_small_boxes = VGroup()
        for i in range(n_cortes**n_dim):
            small_small_small_box = Rectangle(height=2/27, width=2/27, stroke_width=2, stroke_color=RED)
            # fill red with random alpha
            small_small_small_box.set_fill(RED, opacity=0.9+0.1*random.random())
            smaill_small_small_boxes.add(small_small_small_box)
        #arrange small boxes in a grid
        smaill_small_small_boxes.arrange_in_grid(n_rows=n_cortes, n_cols=n_cortes, buff=0.02)
        #position inside of boxes[selected_box]
        smaill_small_small_boxes.move_to(small_small_boxes[selected_box].get_center())
        smaill_small_small_boxes.shift(0.5*RIGHT+0.5*DOWN)
        # scale for 1.5
        smaill_small_small_boxes.scale(5)





                    
        

        # box bix left boxes    
        box_big.next_to(boxes, LEFT, buff=2)
        # add a Brace legend on top of big_box informing the width and height
        #arrow from box_big to boxes
        seta = Arrow(box_big.get_right(), boxes.get_left(), color=RED)
        group_all = VGroup(box_big, boxes, seta, small_boxes, small_small_boxes, smaill_small_small_boxes)
        group_all.set_color(RED)
        # scale to 0.5
        group_all.scale(0.8)

        # move to the center
        group_all.move_to(ORIGIN)
        self.add(group_all)

class box(Scene):
    def construct(self):
        n_bits = 10
        #a image of a box red
        boxes = VGroup()
        n_cortes = 3
        n_dim = 2
        # a box 6x6
        box_big = Rectangle(height=6, width=6, stroke_width=3, stroke_color=RED, fill_color=RED, fill_opacity=0.3)
        for i in range(n_cortes**n_dim):
            box = Rectangle(height=2, width=2, stroke_width=3, stroke_color=RED)
            # fill red with random alpha
            box.set_fill(RED, opacity=0.3*random.random())
            box.move_to(ORIGIN)
            boxes.add(box)
        
        # arrange boxes in a grid
        boxes.arrange_in_grid(n_rows=n_cortes, n_cols=n_cortes, buff=0.4)

        boxes[0].set_fill(RED, opacity=0.1)
        boxes[1].set_fill(RED, opacity=0.6)
        boxes[2].set_fill(RED, opacity=0.7)
        boxes[3].set_fill(RED, opacity=0.1)
        boxes[6].set_fill(RED, opacity=0.2)


        boxes[4].set_fill(RED, opacity=0)
        boxes[4].set_stroke(RED, width=0)
        boxes[5].set_fill(RED, opacity=0)
        boxes[5].set_stroke(RED, width=0)
        boxes[7].set_fill(RED, opacity=0)
        boxes[7].set_stroke(RED, width=0)
        boxes[8].set_fill(RED, opacity=0)
        boxes[8].set_stroke(RED, width=0)
        

        

        small_boxes = VGroup()
        for i in range(n_cortes**n_dim):
            small_box = Rectangle(height=2/3, width=2/3, stroke_width=2, stroke_color=RED)
            # fill red with random alpha
            small_box.set_fill(RED, opacity=0.2+0.1*random.random())
            small_boxes.add(small_box)
        #arrange small boxes in a grid
        small_boxes.arrange_in_grid(n_rows=n_cortes, n_cols=n_cortes, buff=0.1)
        # shift up right
        small_boxes[0].set_fill(RED, opacity=0.6)
        small_boxes[1].set_fill(RED, opacity=0.9)
        small_boxes[2].set_fill(RED, opacity=0.9)
        small_boxes[3].set_fill(RED, opacity=0.7)
        small_boxes[4].set_fill(RED, opacity=0.7)
        small_boxes[5].set_fill(RED, opacity=0.8)
        
        

        # position in the center of boxes[4], boxes[5], boxes[7], boxes[8]
        small_boxes.move_to(VGroup(boxes[4], boxes[5], boxes[7], boxes[8]).get_center())
        
        # scale for 1.5
        small_boxes.scale(2)

        boxes_2 = VGroup()
        for i in range(n_cortes**n_dim):
            box = Rectangle(height=2, width=2, stroke_width=3, stroke_color=RED)
            # fill red with random alpha
            box.set_fill(RED, opacity=0.5*random.random())
            box.move_to(ORIGIN)
            boxes_2.add(box)
        # arrange boxes in a grid]
        boxes_2.arrange_in_grid(n_rows=n_cortes, n_cols=n_cortes, buff=0.4)

        boxes_2[1].set_fill(RED, opacity=0)
        boxes_2[1].set_stroke(RED, width=0)
        boxes_2[2].set_fill(RED, opacity=0)
        boxes_2[2].set_stroke(RED, width=0)
        boxes_2[4].set_fill(RED, opacity=0)
        boxes_2[4].set_stroke(RED, width=0)
        boxes_2[5].set_fill(RED, opacity=0)
        boxes_2[5].set_stroke(RED, width=0)

        boxes_2[0].set_fill(RED, opacity=0.1)
        boxes_2[3].set_fill(RED, opacity=0.1)
        boxes_2[6].set_fill(RED, opacity=0.2)
        boxes_2[7].set_fill(RED, opacity=0.2)
        boxes_2[8].set_fill(RED, opacity=0.2)


        small_boxes_2 = VGroup()
        for i in range(n_cortes**n_dim):
            small_box = Rectangle(height=2/3, width=2/3, stroke_width=2, stroke_color=RED)
            # fill red with random alpha
            small_box.set_fill(RED, opacity=0.2+0.3*random.random())
            small_boxes_2.add(small_box)
        #arrange small boxes in a grid
        small_boxes_2.arrange_in_grid(n_rows=n_cortes, n_cols=n_cortes, buff=0.1)
        #position in center of boxes_2[1], boxes_2[2], boxes_2[4], boxes_2[5]
        small_boxes_2[4].set_fill(RED, opacity=0.8)
        small_boxes_2[5].set_fill(RED, opacity=0.8)
        small_boxes_2[7].set_fill(RED, opacity=0.8)
        small_boxes_2[8].set_fill(RED, opacity=0.8)

        boxes_3 = VGroup()
        for i in range(n_cortes**n_dim):
            box = Rectangle(height=2, width=2, stroke_width=3, stroke_color=RED)
            # fill red with random alpha
            box.set_fill(RED, opacity=0.5*random.random())
            box.move_to(ORIGIN)
            boxes_3.add(box)
        # arrange boxes in a grid]
        boxes_3.arrange_in_grid(n_rows=n_cortes, n_cols=n_cortes, buff=0.4)

        small_boxes_3 = VGroup()
        for i in range(n_cortes**n_dim):
            small_box = Rectangle(height=2/3, width=2/3, stroke_width=2, stroke_color=RED)
            # fill red with random alpha
            small_box.set_fill(RED, opacity=0.2+0.8*random.random())
            small_boxes_3.add(small_box)
        #arrange small boxes in a grid
        small_boxes_3.arrange_in_grid(n_rows=n_cortes, n_cols=n_cortes, buff=0.1)
        #position in center of boxes_2[1], boxes_2[2], boxes_2[4], boxes_2[5]
        small_boxes_3[1].set_fill(RED, opacity=1)
        small_boxes_3[2].set_fill(RED, opacity=1)
        small_boxes_3[4].set_fill(RED, opacity=1)
        small_boxes_3[5].set_fill(RED, opacity=1)

        boxes_3[5].set_fill(RED, opacity=0)
        boxes_3[5].set_stroke(RED, width=0)
        boxes_3[0].set_fill(RED, opacity=0.1)
        boxes_3[1].set_fill(RED, opacity=0.6)
        boxes_3[2].set_fill(RED, opacity=0.7)
        boxes_3[6].set_fill(RED, opacity=0.2)
        boxes_3[7].set_fill(RED, opacity=0.2)
        boxes_3[8].set_fill(RED, opacity=0.2)
        boxes_3[4].set_fill(RED, opacity=0)




        

        






        # box bix left boxes    
        box_big.next_to(boxes, LEFT, buff=2)

        boxes_2.next_to(boxes, RIGHT, buff=2)

        boxes_3.next_to(boxes_2, RIGHT, buff=2)


        small_boxes_2.move_to(VGroup(boxes_2[1], boxes_2[2], boxes_2[4], boxes_2[5]).get_center())
        small_boxes_2.scale(2)

        small_boxes_3.move_to(boxes_3[5].get_center())
        small_boxes_3.scale(1.1)


        # add a Brace legend on top of big_box informing the width and height
        #arrow from box_big to boxes
        seta = Arrow(box_big.get_right(), boxes.get_left(), color=RED)
        seta_2 = Arrow(boxes.get_right(), boxes_2.get_left(), color=RED)
        seta_3 = Arrow(boxes_2.get_right(), boxes_3.get_left(), color=RED)
        group_all = VGroup(box_big, boxes, seta, small_boxes, boxes_2, seta_2, small_boxes_2, boxes_3, small_boxes_3, seta_3)
        group_all.set_color(RED)
        # scale to 0.5
        group_all.scale(0.4)

        # move to the center
        group_all.move_to(ORIGIN)
        self.add(group_all)