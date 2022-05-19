from dataclasses import dataclass
from pathlib import Path
import time
from typing import Callable
import math
import threading
import tkinter
import cv2

import numpy

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Interval:
    min: float
    max: float

def normalize(values: list[float], min_v: float,  max_v: float, new_min: float, new_max: float) -> list[float]:
    new_points: list[float] = []
    for value in values:
        new_points.append(new_min + (value - min_v)*(new_max - new_min)/(max_v - min_v))

    return new_points

def gradient(color1: str, color2: str, value: float) -> tuple[int]:
    r1, g1, b1 = [int(color1[i:i+2], 16) for i in range(1, len(color1), 2)]
    r2, g2, b2 = [int(color2[i:i+2], 16) for i in range(1, len(color2), 2)]

    r3 = round(normalize([value], 0, 1, r1, r2)[0])
    g3 = round(normalize([value], 0, 1, g1, g2)[0])
    b3 = round(normalize([value], 0, 1, b1, b2)[0])

    # return f'#{r3:02x}{g3:02x}{b3:02x}'
    return (r3, g3, b3)

def create_image(function: Callable[[list[float]], float], interval: Interval, file_path: str, override: bool = False) -> None:
    if not override and Path(file_path).exists():
        return

    values: list[list[float]] = []
    for i in range(400):
        values.append([])
        for j in range(400):
            point = normalize([j, i], 0, 400, interval.min, interval.max)
            value = function(point)
            values[i].append(value)

    flat_list = [item for sublist in values for item in sublist]
    min_v = min(flat_list)
    max_v = max(flat_list)

    img = numpy.zeros((400,400,3), dtype=int)
    for i in range(400):
        for j in range(400):
            if values[i][j] == min_v:
                img[i,j] = (0,255,0)
            elif values[i][j]-min_v < 10:
                normalized = normalize([values[i][j]-min_v], 0, 10, 0, 1)[0]
                img[i,j] = gradient('#b92b27', '#ffffff', normalized)[::-1]
            else:
                normalized = normalize([values[i][j]-min_v], 10, max_v-min_v, 0, 1)[0]
                img[i,j] = gradient('#ffffff', '#1565C0', normalized)[::-1]

    cv2.imwrite(file_path, img)

class Drawable:

    def draw(self, canvas: tkinter.Canvas):
        ...

class Circle(Drawable):

    def __init__(self, center: Point, radius: int, fill: str = 'black') -> None:
        self.x0 = center.x - radius
        self.y0 = center.y + radius
        self.x1 = center.x + radius
        self.y1 = center.y - radius
        self.fill = fill

    def draw(self, canvas: tkinter.Canvas) -> None:
        canvas.create_oval(
            self.x0,
            self.y0,
            self.x1,
            self.y1,
            fill=self.fill
        )

class Canvas(threading.Thread):

    def __init__(self, image_path: str):
        threading.Thread.__init__(self)
        self.obj_list: list[Drawable] = []
        self.image_path = image_path
        self.start()

    def run(self):
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.img = tkinter.PhotoImage(file=self.image_path)

        self.root.after(math.floor(1000/30), self._paint_loop)
        self.root.mainloop()

    def _paint_loop(self):
        self.canvas.delete('all')
        self.canvas.create_image(0, 0, image=self.img, anchor=tkinter.NW)
        for obj in self.obj_list:
            obj.draw(self.canvas)
        self.root.after(math.floor(1000/30), self._paint_loop)

    def add_object(self, obj: Drawable):
        self.obj_list.append(obj)

    def add_point(self, center: Point, radius: int, fill: str = 'black'):
        self.obj_list.append(Circle(center, radius, fill))

    def remove_objects(self):
        self.obj_list = []

def draw(canvas: Canvas, min_v: float, max_v: float, points: list[list[float]], sleep: float) -> None:
    canvas.remove_objects()
    for point in points:
        point = normalize(point, min_v, max_v, 0, 400)
        canvas.add_point(Point(point[0],point[1]), 1)

    time.sleep(sleep)
