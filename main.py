from enum import Enum
import tkinter as tk
from tkinter import *

COLORS=['blue','green','red','purple','yellow']

def canvas_Click_event(self):
    # self.x, self.y = event.x, event.y
    print("you pressed : ")

# def create_circle(x, y, r, canvas): #center coordinates, radius
#     x0 = x - r
#     y0 = y - r
#     x1 = x + r
#     y1 = y + r
#     return canvas.create_oval(x0, y0, x1, y1)

root = Tk()
"""canvasArray=[]
for i in COLORS:
    canvas = Canvas(root,width=200, height=200, bg='white')
    canvas.pack(expand=YES, fill=BOTH,side="left")
    # canvas.grid(row=1,column=i)
    canvas.create_oval(10, 10, 30, 30, width=2, fill=i)
    canvas.bind('<Button-1>',canvas_Click_event)
    # canvas.grid(row=0,column=i)
    canvasArray.append(canvas)
    # canvas.grid(row=0,column=i)"""

T = Text(root, height = 5, width = 52)
T.pack()

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED)


var.set("game number :")
label.pack()

root.mainloop()











