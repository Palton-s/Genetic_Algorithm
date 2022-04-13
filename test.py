import numpy as np
import random
import colorsys


arr_h = []
arr_s = []
arr_l = []

for i in range(10000):
    random_color = np.array([random.uniform(0, 255) for i in range(3)])
    hsl_color = colorsys.rgb_to_hls(random_color[0], random_color[1], random_color[2])
    arr_h.append(hsl_color[0])
    arr_l.append(hsl_color[1]/255)
    arr_s.append(hsl_color[2]*-1)
    max_h = max(arr_h)
    max_s = max(arr_s)
    max_l = max(arr_l)
    print(max_h, max_s, max_l)