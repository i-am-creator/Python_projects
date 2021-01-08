import tkinter as tk
import math
import numpy as np
import time
import random


colors = ['#FF0000', '#FFC000', '#FFFC00', '#FF0000', '#00FFFF', '#FF0000']
no_of_boids = 50
radi = 100
align_cont = .2
cohesion_cont = .001
sepa_cont = .3
max_vel = 350
min_vel = 50
time_step = .2
# sleep_time = .0001
sleep_time = 0

root = tk.Tk()
root.title("Boids")
W, H = 1200, 600
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
            separation = np.array([0,0])
            alignment = np.array([0,0])
            cohesion = np.array([0,0])
            for b_ in self.boids:
                if b == b_:
                    continue
                d = math.sqrt((b.x[0] - b_.x[0])**2 + (b.x[1] - b_.x[1])**2)
                if d < radi and d>0:
                    total += 1
                    alignment = alignment + b_.v
                    cohesion = cohesion + b_.x
                    separation = separation + (b.x - b_.x)/d
            if total != 0:
                alignment = alignment/total
                cohesion = cohesion/total
                separation = separation/total
                force = align_cont*(alignment - b.v) + cohesion_cont*(cohesion - b.x - b.v) + sepa_cont*(separation - b.v)
                b.a = force


class boid():
    def __init__(self):
        self.x = np.array((random.randint(0,W), random.randint(0,H)))  # (x, y)
        self.v = np.array((random.randint(-1000,1), random.randint(-1000,1000)))/1000  # (Vx, Vy)
        self.v[0] = 1 - self.v[0] ** 2
        self.a = np.array((random.randint(-1000,1000), random.randint(-1000,1000)))/1000  # (Ax, Ay)
        self.a[0] = 1 - self.a[0] ** 2

        self.mod_v = random.randint(50,100)  # magnitude of v
        self.mod_a = random.randint(1,12) # magnitude of a
        self.v *= self.mod_v
        self.a *= self.mod_a
        self.color = random.choice(colors)
        self.object = canvas.create_oval(self.x[0]-25,self.x[1]-25,self.x[0]+5,self.x[1]+5,fill=self.color)
        self.oldX = self.x
        # self.object = canvas.create_polygon(
        #     self.x[0] + 8*self.v[0], self.x[1] + 8*self.v[1],
        #     self.x[0] - 4*self.v[0], self.x[1] + 4*self.v[1],
        #     self.x[0] - 4*self.v[0], self.x[1] - 4*self.v[1],
        #     fill = self.color
        # )
    def draw(self):

        x = int(self.x[0])
        y = int(self.x[1])
        canvas.delete(self.object)
        self.object = canvas.create_oval(x-8,y-8,x+8,y+8,fill=self.color)

        # x = int(self.x[0]- self.oldX[0])
        # y = int(self.x[1]- self.oldX[1])
        # canvas.move(self.object, x, y)
        # self.oldX = self.x

        # p1 = - 18, 1
        # p2 = - 4, + 4
        # p3 = - 4, - 4
        #
        # p1 = np.matrix(p1).transpose()
        # p2 = np.matrix(p2).transpose()
        # p3 = np.matrix(p3).transpose()
        # t = math.pi - math.atan(self.v[1] / self.v[0])
        # rot = np.matrix((
        #     (math.cos(t), math.sin(t)),
        #     (-math.sin(t), math.cos(t))
        # )
        # )
        # p1 = np.matmul(rot, p1)
        # p2 = np.matmul(rot, p2)
        # p3 = np.matmul(rot, p3)
        # canvas.delete(self.object)

        # self.object = canvas.create_oval(x-5,y-5,x+5,y+5,fill='#ffffff')
        # self.object = canvas.create_polygon(
        #     int(p1[0] + x), int(p1[1] + y),
        #     int(p2[0] + x), int(p2[1] + y),
        #     int(p3[0] + x), int(p3[1] + y),
        #     fill=self.color
        # )

    def update(self):
        self.v = self.v + time_step * self.a
        # self.v = np.array([min(max(2, self.v[0]), max_vel), min(max(2, self.v[1]), max_vel)])
        self.mod_v = math.sqrt(self.v[0] ** 2 + self.v[1] ** 2)
        if self.mod_v != 0:
            v_dir = self.v/self.mod_v
        else:
            v_dir = self.v
        if self.mod_v<min_vel:
            self.v = v_dir * min_vel
        elif self.mod_v > max_vel:
            self.v = v_dir * max_vel


        self.x = self.x +  time_step * self.v

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
    canvas.update()
    if i == 100:
        time.sleep(5)

    time.sleep(sleep_time)

root.mainloop()
