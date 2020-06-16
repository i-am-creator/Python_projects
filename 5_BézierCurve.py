tk 2020-06-16 10-03-43.mp4

Type
Video
Size
30 MB (31,648,236 bytes)
Storage used
30 MB (31,648,236 bytes)
Location
Python
Owner
me
Modified
10:14 AM by me
Opened
10:12 AM by me
Created
10:10 AM with Google Drive Web
Add a description
Caption tracks
Viewers can download
import tkinter as tk
from tkinter import *


import math
import numpy as np
import time

lines = []
a = []
const1 = 1000


# only for 2 line
def draw_shape():
    global lines
    if len(lines) == 0:
        canvas.delete('all')
        return
    line_ = []
    # lines[1] = (lines[1][-2], lines[1][-1], lines[1][0], lines[1][1])
    for line in lines:
        l=np.zeros((const1,2))

        x1, y1, x2, y2 = line

        l[-1] = x2, y2
        k1 = (x2 - x1)/const1
        k2 = (y2 - y1)/const1
        k = np.asarray((k1, k2))
        for i in range(const1):
            l[i] = l[i-1] - k
            x1, y1 = int(l[i][0]), int(l[i][1])
            x2, y2 = int(l[i - 1][0]), int(l[i - 1][1])
            canvas.create_line(x1, y1, x2, y2, width=1, fill='red')

        line_.append(l)
    # print(line_)
    bezier_curve(line_)



def section(x1, y1, x2, y2, m):
    # Applying section formula
    n = const1 - m
    x = (n * x1 + m * x2)/(m+n)
    y = (n * y1 + m * y2)/(m + n)
    return x, y

def make_line():
    canvas.create_rectangle(0, 0, 25, 25, fill = 'red')
    for l in lines:
        x1, y1, x2, y2 = l
        canvas.create_line(x1, y1, x2, y2, fill = '#ffffff')

def bezier_curve(li):
    l = li[::-1]
    if len(l)!=0:
        prev_cord = int(l[0][0][0]), int(l[0][0][1])
    if len(l) == 1:
        canvas.delete('all')
        make_line()
        for i in range(const1):
            [x1, y1] = int(l[0][i][0]), int(l[0][i][1])
            x2, y2 = prev_cord
            # print(x1, y1)
            canvas.create_line(x1, y1, x2, y2, width=4, fill='red')
            prev_cord = x1, y1
        canvas.update()
            # time.sleep(.1)
    elif len(l) > 1:
        temp = []
        p = None
        while len(l) > 1:
            l1 = l.pop()
            l2 = l.pop()
            l3 = []
            for i in range(const1):
                x1,y1 = l1[i]
                x2,y2 = l2[i]
                new_l = section(x1, y1, x2, y2, i)
                # if p:
                #     canvas.delete(p)
                # p = canvas.create_line(x1,y1,x2,y2, fill = 'green')
                # p0 = canvas.create_oval(new_l[0], new_l[1], new_l[0] + 1, new_l[1], fill = "#ff00ff")
                # canvas.update()
                # time.sleep(.001)
                l3.append(new_l)
            l.append(l2)
            temp.append(l3)
        # print(len(temp))
        bezier_curve(temp)


def draw(event):
    x, y = event.x, event.y
    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        line = canvas.create_line(x, y, x1, y1)
        # lines.append((x, y, x1, y1))
        # if len(lines) == 2:
        #     draw_shape()
    canvas.old_coords = x, y


def draw_line(event):
    if str(event.type) == 'ButtonPress':
        canvas.old_coords = event.x, event.y

    elif str(event.type) == 'ButtonRelease':
        x, y = event.x, event.y
        x1, y1 = canvas.old_coords
        line = canvas.create_line(x, y, x1, y1)
        lines.append(np.asarray((x, y, x1, y1)))
        draw_shape()



def nearst_point(x, y):
    dist = math.inf
    for i in range(len(lines)):
        p1_x, p1_y, p2_x, p2_y = lines[i]
        d1 = math.sqrt((p1_x - x) ** 2 + (p1_y - y) ** 2)
        d2 = math.sqrt((p2_x - x) ** 2 + (p2_y - y) ** 2)
        k = min(d1, d2)
        if k < dist:
            dist = k
            canvas.bakwas = k ,i ,  0 if d1 < d2 else 1, 1

        canvas.update()

def update_line(event):
    global lines
    x = event.x
    y = event.y
    d0, d1, d2, d3 = canvas.bakwas

    if d3 == 0:
        nearst_point(x, y)
    else:
        if str(event.type) == 'Motion':
            if d2 == 0:
                i = d1
                lines[i][0] = event.x
                lines[i][1] = event.y
            elif d2 == 1:
                i = d1
                lines[i][2] = event.x
                lines[i][3] = event.y
        elif str(event.type) == 'ButtonRelease':
            if event.x <= 25 and event.y <= 25:
                # lines.remove(lines[d1])
                lines = lines[:d1] + lines[d1+1:]
            canvas.bakwas = 0, 0, 0, 0
            canvas.update()
    draw_shape()
    if event.x <= 25 and event.y <= 25:
        canvas.create_rectangle(0, 0, 35, 35, fill='red')



def draw_shape_event(event):
    draw_shape()

root = tk.Tk()
W, H = 1200, 600
canvas = tk.Canvas(root, width=W, height=H, bg = 'black')
canvas.old_coords = None
canvas.bakwas = 0, 0, 0, 0
canvas.bind('<ButtonPress-1>', draw_line)
canvas.bind('<ButtonRelease-1>', draw_line)
canvas.bind('<B3-Motion>', update_line)
canvas.bind('<ButtonRelease-3>', update_line)
root.bind('<Motion>', draw_shape_event)

canvas.pack()

canvas.update()
# root.bind('<B1-Motion>', draw)
# root.bind('<ButtonRelease-1>', reset_coords)

root.mainloop()
