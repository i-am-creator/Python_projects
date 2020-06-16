import tkinter as tk
import math
import numpy as np
import time
import random


no_of_boids = 50
radi = 500
align_cont = .2
cohesion_cont = .001
sepa_cont = .2
max_val = 25
W, H = 600, 600

root = tk.Tk()
canvas = tk.Canvas(root, width=W, height=H, bg = 'black')
canvas.pack()

class flock():
    def __init__(self):
        self.boids = []
        for i in range(no_of_boids):
            self.boids.append(boid())
    def draw(self):

        for b in self.boids:
            b.update()
            b.draw()
        canvas.update()
    def update(self):
        for b in self.boids:
            total = 0
            separation = 0
            alignment = 0
            cohesion = 0
            for b_ in self.boids:
                if b == b_:
                    continue
                d = math.sqrt((b.x[0] - b_.x[0])**2 + (b.x[1] - b_.x[1])**2)
                if d < radi and d>0:
                    total += 1
                    alignment += b_.v
                    cohesion += b_.x
                    separation += (b.x - b_.x)/d
            if total != 0:
                alignment = alignment/total
                cohesion = cohesion/total
                separation = separation/total
                force = align_cont*(alignment - b.v) + cohesion_cont*(cohesion - b.x - b.v) + sepa_cont*(separation - b.v)
                b.a = force


class boid():
    def __init__(self):
        self.x = np.array((random.randint(0,W), random.randint(0,H)))  # (x, y)
        self.v = np.array((random.randint(-1000,0), random.randint(-1000,1000)))/1000  # (Vx, Vy)
        self.v[0] = 1 - self.v[0] ** 2
        self.a = np.array((random.randint(-1000,1000), random.randint(-1000,1000)))/1000  # (Ax, Ay)
        self.a[0] = 1 - self.a[0] ** 2

        self.mod_v = random.randint(50,100)  # magnitude of v
        self.mod_a = random.randint(1,12) # magnitude of a
        self.v *= self.mod_v
        self.a *= self.mod_a
        self.object = canvas.create_polygon(
            self.x[0] + 8*self.v[0], self.x[1] + 8*self.v[1],
            self.x[0] - 4*self.v[0], self.x[1] + 4*self.v[1],
            self.x[0] - 4*self.v[0], self.x[1] - 4*self.v[1],
            fill = '#ffffff'
        )
    def draw(self):
        x = int(self.x[0])
        y = int(self.x[1])
        p1 = - 18, 1
        p2 = - 4, + 4
        p3 = - 4, - 4

        p1 = np.matrix(p1).transpose()
        p2 = np.matrix(p2).transpose()
        p3 = np.matrix(p3).transpose()
        t = math.pi - math.atan(self.v[1] / self.v[0])
        rot = np.matrix((
            (math.cos(t), math.sin(t)),
            (-math.sin(t), math.cos(t))
        )
        )
        p1 = np.matmul(rot, p1)
        p2 = np.matmul(rot, p2)
        p3 = np.matmul(rot, p3)
        canvas.delete(self.object)
        # self.object = canvas.create_oval(x-5,y-5,x+5,y+5,fill='#ffffff')
        self.object = canvas.create_polygon(
            int(p1[0] + x), int(p1[1] + y),
            int(p2[0] + x), int(p2[1] + y),
            int(p3[0] + x), int(p3[1] + y),
            fill='#ffffff'
        )

    def update(self):
        self.mod_a = math.sqrt(self.a[0] ** 2 + self.a[1] ** 2)
        # self.a = self.a / self.mod_a if self.mod_a > 1 else self.a

        self.v += self.a
        self.v /= self.mod_v
        self.v *= max_val

            # print(self.v)


        self.mod_v = math.sqrt(self.v[0]**2 + self.v[1]**2)
        # self.v = self.v /self.mod_v
        try:
            self.x[0] += math.floor(self.v[0])
            self.x[1] += math.floor(self.v[1])
        except:
            pass
        if self.x[0] < 0:
            self.x[0] = W
        elif self.x[0] > W:
            self.x[0] = 0
        if self.x[1] < 0:
            self.x[1] = H
        elif self.x[1] >H:
            self.x[1] = 0


f = flock()
for i in range(10000):
    # f.draw()
    f.update()
    f.draw()
    # time.sleep(.05)

root.mainloop()
