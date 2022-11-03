from manim import *

config.background_color = "#fff"
# set screen square
config.frame_height = 6
config.frame_width = 6
# make an animation for plotting the graph of the function


class Scarter(MovingCameraScene):
    def construct(self):
        # draw the axes
        axes = Axes(
            y_range=[0, 100, 1],
            x_range=[0, 100, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False},
        )
        
        coords_points = []
        for i in range(100):
            y = np.random.uniform(0, 100)
            x = np.random.uniform(0, 100)
            coords_points.append([x, y])

        points = VGroup()
        for i in range(len(coords_points)):
            x = coords_points[i][0]
            y = coords_points[i][1]
            # add points to the axes
            point = Dot(axes.c2p(x, y), radius=0.05, color=BLUE)
            points.add(point)
        avas = [np.exp(-val[0]**2-val[1]**2) for val in coords_points]
        # sort avas
        avas = sorted(avas)
        # order coords by avas
        coords_points = [x for _, x in sorted(zip(avas, coords_points))]
        self.add(points)
        
        last_coord = coords_points[:50]
        min_x = min([coord[0] for coord in last_coord])
        max_x = max([coord[0] for coord in last_coord])
        medium_x = (min_x + max_x) / 2
        # get screen height
        screen_height = self.camera.frame_height
        scalex = screen_height/(max_x - min_x)
        min_y = min([coord[1] for coord in last_coord])
        max_y = max([coord[1] for coord in last_coord])
        medium_y = (min_y + max_y) / 2

            

        # zoom in to the first point and scale the point
        scale = 0.5
        
        # animate the stroke axis
        

        self.play(
            AnimationGroup(self.camera.frame.animate.scale(scalex).move_to(axes.c2p(medium_x,medium_y)),*[point.animate.scale(scalex) for point in points]),
            run_time=3,
        )

        


        

        