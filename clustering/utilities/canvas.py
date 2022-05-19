from dataclasses import dataclass
import math
import threading
import tkinter

@dataclass
class Point:
    x: int
    y: int

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

    def __init__(self):
        threading.Thread.__init__(self)
        self.obj_list: list[Drawable] = []
        self.start()

    def run(self):
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.root.after(math.floor(1000/30), self._paint_loop)
        self.root.mainloop()

    def _paint_loop(self):
        self.canvas.delete('all')
        for obj in self.obj_list:
            obj.draw(self.canvas)
        self.root.after(math.floor(1000/30), self._paint_loop)

    def add_object(self, obj: Drawable):
        self.obj_list.append(obj)

    def add_point(self, center: list[list[float]], radius: int, fill: str = 'black'):
        self.obj_list.append(Circle(Point(center[0], center[1]), radius, fill))

    def remove_objects(self):
        self.obj_list = []
