from tkinter import *
from tkinter import ttk
import math
import random

def dist(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2
    
size = 800
width = 800
height =800


class Partical :
    def __init__(self, canvas):
        self.x = width /2
        self.y = height / 2
        self.rays = []
        for i in range(0, 360, 1):
            self.rays.append(Ray(self.x, self.y, math.radians(i), canvas))

    def show(self):
        for ray in self.rays:
            minm = 1000**2
            cx=0
            cy=0
            #ray.update(self.x, self.y)
            #ray.show()
            for wall in walls:
                
                pt = ray.hit(wall)
                if pt :
                    if minm > dist(ray.ix, ray.iy,self.x, self.y):
                        minm = dist(ray.ix, ray.iy, self.x, self.y)
                        cx = ray.ix
                        cy = ray.iy
                
                            
            if cx :
                l = c.create_line(cx , cy, self.x, self.y, fill = "silver")
        
    def update(self, event):
        self.x = event.x
        self.y = event.y
        for ray in self.rays:
            ray.update(self.x, self.y)
            
                   
class Boundary(object) :
    def __init__(self, x1, y1, x2, y2,canvas):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
    def show(self):
        l = self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill = "blue" )
    
class Ray(object) :
    def __init__(self, x, y, angle, canvas) :
        self.posx = x
        self.posy = y
        self.dirx = math.sin(angle) 
        self.diry = math.cos(angle) 
        self.ix   = 0          #intersecting points
        self.iy   = 0
        self.canvas = canvas
    def show(self):
        l = self.canvas.create_line(self.posx, self.posy, self.dirx  + self.posx,self.diry  +self.posy, fill = "red" )
    def update(self, x, y):
        self.posx = x
        self.posy = y
    #def lookat(self, event):
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
        if den == 0 :
            #print("1")
            # Ray start on the wall
            return 
        t =  ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4))/den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3))/den
        if t >0 and u > 0 and t < 1 :
            self.ix = x1 + t * (x2 - x1)
            self.iy = y1 + t * (y2 - y1)
            #print(str(x)+str(y))
            #l = c.create_line(self.ix, self.iy, self.posx, self.posy, fill = "silver")
        
            return self.ix, self.iy
        else :
            self.ix = 0
            self.iy = 0
            #print("2")
            return 
         
gui = Tk()  
gui.geometry("800x800")
gui.title("new")

c = Canvas(gui, width = size, height = size, bg = 'black' )
c.pack()
walls = []
for i in range(15):
    x1 = random.randrange(width)
    x2 = random.randrange(width)
    y1 = random.randrange(height)
    y2 = random.randrange(height)
    walls.append(Boundary(x1, y1, x2, y2, c))

walls.append(Boundary(1, 1, width, 1, c))
walls.append(Boundary(1, 1, 1, height, c))
walls.append(Boundary(width, height, width, 1, c))
walls.append(Boundary(1, height, width, height, c))
#ray = Ray(100, 200,0,c)
p = Partical(c)
running = True
while(running):
    
    c.delete("all")
    for wall in walls:
        wall.show()
    
    c.bind("<B1-Motion>", p.update)

    
    p.show()
    gui.update()
    
gui.update()
gui,mainloop()
