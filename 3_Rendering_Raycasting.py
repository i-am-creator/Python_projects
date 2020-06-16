from tkinter import *
import numpy
import math
import random


def dist(a1, a2, b1, b2):
    return math.sqrt((a1 - b1) ** 2 + (a2 - b2) ** 2)


# size = 400
width = 700
height = 700
fov = 60  # (in dig) field of version
strip_len = width / fov
record = numpy.empty([fov], dtype=int)


def color(h, min, max):
    col = ('#999999', '#888888', '#777777', '#666666', '#555555', '#444444', '#333333', '#222222', '#111111', '#987543')
    i = math.floor(h * (20 / height))
    # print(c)
    #print(i)
    if i < 9:
        return col[i]


def heig(a, f):
    if f:
        len_cont = height / dist(0, 0, height, width)
    else:
        len_cont = 1

    return (len_cont * a) / 2


colors = ("red", "blue", "white", "green", "gray", "silver")


class Partical:

    def __init__(self, canvas):
        self.x = width / 2
        self.y = height / 2
        self.rays = []
        self.color = "gray"
        self.rot = 90  # angle to rotate fov
        self.iangle = self.rot + fov/2  #initial angle  
        self.c = canvas
        self.fish_eye_effect = False

        for i in range(0, 360):  # range(-int(fov/2) - self.rot, int(fov/2) - self.rot, 1)
            self.rays.append(Ray(self.x, self.y, i, canvas))

    def setcolor(self, event):
        i = random.randrange(0, 5)
        self.color = colors[i]

    def show(self):
        i = 0
        for ray in self.rays:

            if ray.angle > self.rot and ray.angle < fov + self.rot:
                minm = 1000 ** 2
                cx = 0
                cy = 0
                for wall in walls:
                    pt = ray.hit(wall)
                    if pt:
                        if minm > dist(ray.ix, ray.iy, self.x, self.y):
                            minm = dist(ray.ix, ray.iy, self.x, self.y)
                            cx = ray.ix
                            cy = ray.iy
                if cx:
                    l = c.create_line(cx, cy, self.x, self.y, fill=self.color)
                    if self.fish_eye_effect:
                        record[i] = abs(dist(cx, cy, self.x, self.y))
                    else:
                        record[i] = abs(dist(cx, cy, self.x, self.y) * math.cos(math.radians(ray.angle - self.iangle)))
                    i += 1

            if not (self.rot < 360 and self.rot >= 0):
                cont1 = 360 - abs(self.rot)
                if ray.angle > cont1:
                    minm = 1000 ** 2
                    cx = 0
                    cy = 0
                    for wall in walls:
                        pt = ray.hit(wall)
                        if pt:
                            if minm > dist(ray.ix, ray.iy, self.x, self.y):
                                minm = dist(ray.ix, ray.iy, self.x, self.y)
                                cx = ray.ix
                                cy = ray.iy
                    if cx:
                        l = c.create_line(cx, cy, self.x, self.y, fill=self.color)
                        if self.fish_eye_effect:
                            record[i] = abs(dist(cx, cy, self.x, self.y))
                        else:
                            record[i] = abs(dist(cx, cy, self.x, self.y) * math.cos(math.radians(ray.angle - self.iangle)))
                        i += 1
            elif not ((self.rot + fov) < 360 and (self.rot + fov) >= 0):
                cont1 = abs(self.rot + fov) % 360
                if ray.angle < cont1:
                    minm = 1000 ** 2
                    cx = 0
                    cy = 0
                    record[-1] = height
                    record[-2] = height
                    for wall in walls:
                        pt = ray.hit(wall)
                        if pt:
                            if minm > dist(ray.ix, ray.iy, self.x, self.y):
                                minm = dist(ray.ix, ray.iy, self.x, self.y)
                                cx = ray.ix
                                cy = ray.iy
                    if cx:
                        l = c.create_line(cx, cy, self.x, self.y, fill=self.color)
                        if self.fish_eye_effect:
                            record[i] = abs(dist(cx, cy, self.x, self.y))
                        else:
                            record[i] = abs(dist(cx, cy, self.x, self.y) * math.cos(math.radians(ray.angle - self.iangle)))
                        i += 1

    def update(self, event):
        #print(event.keysym)
        if event.keysym == "Up":
            self.rot += 5
        elif event.keysym == "Down":
            self.rot -= 5
        elif event.keysym == "f":
            if self.fish_eye_effect :
                self.fish_eye_effect = False
            else:
                self.fish_eye_effect = True
        else:
            self.x = event.x
            self.y = event.y
            for ray in self.rays:
                ray.update(self.x, self.y)
        if self.rot + fov >= 360:
            self.rot = self.rot % 360
        elif self.rot + fov <= 0:
            self.rot = 360 + self.rot


class Boundary(object):
    def __init__(self, x1, y1, x2, y2, canvas):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas

    def show(self):
        l = self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="blue")


class Ray(object):
    def __init__(self, x, y, angle, canvas):
        self.posx = x
        self.posy = y
        self.dirx = math.sin(math.radians(angle))
        self.diry = math.cos(math.radians(angle))
        self.ix = 0  # intersecting points
        self.iy = 0
        self.angle = angle
        self.canvas = canvas

    def show(self):
        l = self.canvas.create_line(self.posx, self.posy, self.dirx + self.posx, self.diry + self.posy, fill="red")

    def update(self, x, y):
        self.posx = x
        self.posy = y

    # def lookat(self, event):
    #        self.dirx = event.x - self.posx
    #        self.diry = event.y - self.posy

    def hit(self, wall):
        x1 = wall.x1
        y1 = wall.y1
        x2 = wall.x2
        y2 = wall.y2

        x3 = self.posx
        y3 = self.posy
        x4 = self.dirx + self.posx
        y4 = self.diry + self.posy

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            # print("1")
            return
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
        if t > 0 and u > 0 and t < 1:
            self.ix = x1 + t * (x2 - x1)
            self.iy = y1 + t * (y2 - y1)
            # print(str(x)+str(y))
            # l = c.create_line(self.ix, self.iy, self.posx, self.posy, fill = "silver")

            return self.ix, self.iy
        else:
            self.ix = 0
            self.iy = 0
            # print("2")
            return


gui = Tk()
# gui.geometry("800x800")
gui.title("new")

c = Canvas(gui, width=width, height=height, bg='black')
c2 = Canvas(gui, width=width, height=height, bg='black')

c.pack(side=LEFT)
c2.pack(side=RIGHT)

walls = []
for i in range(5):
    x1 = random.randrange(width)
    x2 = random.randrange(width)
    y1 = random.randrange(height)
    y2 = random.randrange(height)
    walls.append(Boundary(x1, y1, x2, y2, c))

walls.append(Boundary(1, 1, width, 1, c))
walls.append(Boundary(1, 1, 1, height, c))
walls.append(Boundary(width, height, width, 1, c))
walls.append(Boundary(1, height, width, height, c))
p = Partical(c)
running = True
rect = []
while (running):

    c.delete("all")
    for wall in walls:
        wall.show()
    for r in rect:
        c2.delete(r)
    for i in range(0, fov):
        h = heig(record[i], p.fish_eye_effect)
        rect.append(
            c2.create_rectangle(strip_len * i, h, strip_len * (i + 1), height - h, fill=color(h, min(record), max(record)), outline=color(h, min(record), max(record))))

    c.bind("<Motion>", p.update)
    c.bind("<Double-Button>", p.setcolor)
    c.bind("<Key>", p.update)

    p.show()
    gui.update()

gui.update()
gui.mainloop()
