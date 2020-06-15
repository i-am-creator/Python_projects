# Importing files
from tkinter import *
from tkinter import ttk
import random
import time
import math

w = 800
h = 800
no_of_star = 50

# defining a class STAR which store the current position of star and how the start move over time setp

class star(object):
    def __init__(self, canvas):
        self.x = random.randrange(w)
        self.y = random.randrange(h)
        self.z = 1
        self.c = canvas
        #self.l = self.c.create_line(w/2, h/2, self.x+2, self.y+2 , fill = "white")
        dir_x = (w/2 - self.x)
        dir_y = (h/2 - self.y)
        k = math.sqrt(dir_x**2 + dir_y**2)
        self.dirx = dir_x /k
        self.diry = dir_y /k
        self.o = self.c.create_oval(self.x-2, self.y-2, self.x+2, self.y+2 , fill = "white")
    def show(self):
    
        # this function calculate the new pos of star and move the star to new pos
        
        #if self.x < w/2 and self.y < h/2 :
        sx = self.x - self.dirx * (self.z + 5) #/(self.dirx +self.diry)
        sy = self.y - self.diry * (self.z + 5) #/(self.dirx +self.diry)
        #self.c.move(self.o ,sx, sy)
        self.c.delete(self.o)
        self.o = self.c.create_oval(sx-2, sy-2, sx+2, sy+2 , fill = "white")
        self.x= sx
        self.y= sy
        self.z += 1
        c.update()
        
        # CHEACKING IF THE STAR MOVES OUT FROM CANVAS THEN AGING GIVE THE STAR NEW CO-ORDINATES NREAR THE CENTER OF CANVAS
        
        if abs(self.x - w/2) >= w/2 -1 or abs(self.y - h/2) >= h/2  -1 :
            self.z = 1
            self.x = random.randrange(w)
            self.y = random.randrange(h)
            dir_x = (w/2 - self.x)
            dir_y = (h/2 - self.y)
            k = math.sqrt(dir_x**2 + dir_y**2)
            self.dirx = dir_x /k
            self.diry = dir_y /k
        

        


gui = Tk()
gui.geometry(str(w) + "x" + str(h))
gui.title("Space")
c = Canvas(gui, width = w, height = h, bg = 'black' )
c.pack()
#gui.mainloop()
stars = []
for i in range(no_of_star):
    stars.append(star(c))

for i in range(3000):
    for star in stars:
        star.show()
        #time.sleep(.1)
    
