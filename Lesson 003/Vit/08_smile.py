# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


sd.resolution = (1920, 1080)

def smile (x1, y1, color1):
    point1 = sd.get_point(x1, y1)
    point2 = sd.get_point(x1+80, y1)
    sd.line(point1, point2, color=color1, width=4)
    point3 = sd.get_point(x1-10, y1+10)
    point4 = sd.get_point(x1, y1)
    sd.line(point3, point4, color=color1, width=4)
    point5 = sd.get_point(x1+90, y1+10)
    point6 = sd.get_point(x1+80, y1)
    sd.line(point5, point6, color=color1, width=4)
    point7 = sd.get_point(x1+40, y1+50)
    sd.circle(point7, radius=100, color=color1, width=4)
    point8 = sd.get_point(x1, y1+80)
    sd.circle(point8, radius=20, color=color1, width=4)
    point9 = sd.get_point(x1+80, y1+80)
    sd.circle(point9, radius=20, color=color1, width=4)
    return


for _ in range(10):
    point = sd.random_point()
    color1 = sd.random_color()
    smile(x1=point.x, y1=point.y, color1=color1)




sd.pause()
