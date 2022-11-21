from enum import Enum
import tkinter as tk
from tkinter import *
from tkinter.ttk import Separator

from bh import *


root = tk.Tk()
# root.attributes('-topmost', True)
# root.geometry("500x500")


COLORS=['blue','green','red','purple','yellow']
listData=[('Guess','NumberGuessed ','Bh ','Nh ','NumberGuessed ','Bh ','Nh'),
          (1,"","","","","",""),
          (2,"","","","","",""),
          (3,"","","","","",""),
          (4,"","","","","",""),
          (5,"","","","","",""),
          (6,"","","","","",""),
          (7,"","","","","",""),
          (8,"","","","","",""),
          (9,"","","","","",""),
          (10,"","","","","","")]

##
def disable_entry(e):
   e.config(state= "disabled")

def color_bg1(e):
    e.config(disabledbackground="red")

def color_bg2(e):
    e.config(disabledbackground="green")


def createGameTable():
    for i in range(NumberOfGames):
        for j in range(7):
            if(j>3):
               e = Entry(test, width=15, fg='red', font=('Arial', 12, 'bold'))
            else:
               e = Entry(test, width=15, fg='blue', font=('Arial', 12, 'bold'))
            e.grid(row=i,column=j)
            e.insert(END,listData[i][j])
            disable_entry(e)
            if( j>0 and j<=3):
                color_bg1(e)
            else:
                color_bg2(e)

            # e.insert(END,listData[])

def canvas_Click_event(self):
    # self.x, self.y = event.x, event.y
    print("you pressed : ")


var = StringVar()
gameNum = 1
# gameLabel = Label(root, text="\nNumber of games " + str(NumberOfGames))

# numberToGuess1=Label(root,text=str(SecretNumber))
# numberToGuess2=Label(root,text=str(SecretNumber))

# guessNumberLabel = Label(root, text="guessNum: "+ str(SecretNumber))
# currentGuessLabel = Label(root, text="guess: ")
# nbLabel = Label(root, text="nb: ")
# nhLabel = Label(root, text="nh: ")
# spaceLabel = Label(root, text="                     ")
#
#
#
# guessNumberLabel2 = Label(root, text="guessNum: " + str(SecretNumber))
# currentGuessLabel2 = Label(root, text="guess:")
# nbLabel2 = Label(root, text="nb:")
# nhLabel2 = Label(root, text="nh:")


def democolorChange():b1.configure(bg="red",fg="yellow")

labels = []
##def create_label(NumberOfGames):
    ##NumberOfGames=NumberOfGames+1
    # count = len(root.winfo_children())
    ##label = tk.Label(root, text=f"Label #{NumberOfGames}")
    ##label.grid(row=NumberOfGames,column=1,sticky=W,pady=2)
    ##labels.append(label)##


b1=Button(root,text='button1',command=createGameTable())
# b2=Button(root,text='Press for new label',command=create_label(NumberOfGames))
NumberOfGames=NumberOfGames+1

# numberToGuess1.grid(row=0, column=0, sticky="", pady=2, columnspan=1)
# numberToGuess2.grid(row=0, column=6, sticky="", pady=2,columnspan=1)

# guessNumberLabel.grid(row=1, column=0, sticky=W, pady=2)
# currentGuessLabel.grid(row=1, column=1, sticky=W, pady=2)
# nbLabel.grid(row=1, column=3, sticky=W, pady=2)
# nhLabel.grid(row=1, column=4, sticky=W, pady=2)
# b1.grid(row=10, column=5, sticky=W, pady=2)
# # b2.grid(row=2,column=2,sticky=W,pady=2)
#
# spaceLabel.grid(row=1, column=5, sticky=W, pady=2)
#
# guessNumberLabel2.grid(row=1, column=6, sticky=E, pady=2)
# currentGuessLabel2.grid(row=1, column=7, sticky=E, pady=2)
# nbLabel2.grid(row=1, column=8, sticky=E, pady=2)
# nhLabel2.grid(row=1, column=9, sticky=E, pady=2)
#
#
# separator = Separator(root, orient='horizontal')
# separator.place(relx=0, rely=1.0, relwidth=1, relheight=1)

root.mainloop()

# -------------------------------------------------------------

# def create_circle(x, y, r, canvas): #center coordinates, radius
#     x0 = x - r
#     y0 = y - r
#     x1 = x + r
#     y1 = y + r
#     return canvas.create_oval(x0, y0, x1, y1)

# """canvasArray=[]
# for i in COLORS:
#     canvas = Canvas(root,width=200, height=200, bg='white')
#     canvas.pack(expand=YES, fill=BOTH,side="left")
#     # canvas.grid(row=1,column=i)
#     canvas.create_oval(10, 10, 30, 30, width=2, fill=i)
#     canvas.bind('<Button-1>',canvas_Click_event)
#     # canvas.grid(row=0,column=i)
#     canvasArray.append(canvas)
#     # canvas.grid(row=0,column=i)"""

# count=0
# def add_line():
#     global count
#     count+=1
#     if(count<=1):
#         tk.Label(text='Label %d'% count +'Label %d'% count+'Label %d'% count+'Label %d'% count).pack(side=)
#         tk.Label(text='Label %d'% count +'Label %d'% count+'Label %d'% count+'Label %d'% count).pack(side=RIGHT)
#     else:
#         tk.Label(text='').pack(side=TOP)

# tk.Label(text="").pack(side=tk.CENTER)
# tk.Button(root,text='button1',command=add_line).pack()
