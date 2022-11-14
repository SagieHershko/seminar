from enum import Enum
import tkinter as tk
from tkinter import *
from bh import *

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

root = tk.Tk()
root.attributes('-topmost', True)
root.geometry("500x500")

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

var = StringVar()
gameNum = 1
gameLabel = Label(root, text="\nNumber of games " + str(NumberOfGames))

gameLabel.pack(side="top")

root.mainloop()











