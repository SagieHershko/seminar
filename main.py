import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import bh
from bh import startgamebh

root = tk.Tk()
gamesNum=0
digsNum = 0
selected_digits = IntVar()
int_var = IntVar()
COLORS=['blue','green','red','purple','yellow']

spinboxdig = tk.Spinbox(root, from_=4, to=8, textvariable=selected_digits, width=4, wrap=True)
spinboxgames = ttk.Spinbox(root, textvariable=int_var, from_=0, to=100, width=4, wrap=True)


def start_window():
    """
    Create and display a Tkinter window with a title, fixed size, and non-resizable attributes.

    Parameters:
    None

    Returns:
    None
    """
    root.attributes('-topmost', True)
    root.geometry("250x250")
    root.resizable(False, False)
    root.title('Bulls and pigs')
    starting_screen()

def spinbox_digits():
    spinboxdig.pack()

def spinbox_gamesNum():
    spinboxgames.set(10)
    spinboxgames.pack()


def startgame():
    """
    Initialize the game with the selected number of digits and games, and display a message showing the selected values.
    If the digsNum is bigger than 4, the process can take some seconds to proceed - so show this window.

    Parameters:
    None

    Returns:
    None
    """
    global gamesNum
    global digsNum
    gamesNum = int(spinboxgames.get())
    digsNum = int(spinboxdig.get())
    if digsNum>4:
        messagebox.showwarning("Please be patient!", "Please be patient! This process can take some seconds to proceed.")
    tk.Label(root, text="You selected " + str(digsNum) + " digits, and " + str(gamesNum) + " games. ").pack()
    startgamebh(digsNum, gamesNum)
    createGameTable()



def starting_screen():
    """
    Display a screen with spinboxes and a button for selecting the number of digits and games in a game.

    Parameters:
    None

    Returns:
    None
    """
    Label(root, text="To start the game you have to choose:").pack()
    Label(root, text="How much digits would be in the number?").pack()
    spinbox_digits()
    Label(root, text="How much games would you like to play?").pack()
    spinbox_gamesNum()
    Button(root, text="Start playing!", command=startgame).pack()


start_window()


def win_funcs(tk_window, tk_window2):
    """
    Modify the appearance and behavior of Tkinter windows.

    Parameters:
    tk_window (Tk): The first Tkinter window to be modified.
    tk_window2 (Tk): The second Tkinter window to be modified.

    Returns:
    None
    """
    tk_window.attributes('-topmost', True)
    tk_window.resizable(False, False)
    tk_window.title('Player one window')
    style = ttk.Style(tk_window)
    # set ttk theme to "clam" which support the fieldbackground option
    style.theme_use("clam")
    style.configure("Treeview", background="black",
                    fieldbackground="black", foreground="white")

    tk_window2.title('Player two window')
    tk_window2.attributes('-topmost', True)
    tk_window2.resizable(False, False)
    style = ttk.Style(tk_window2)
    # set ttk theme to "clam" which support the fieldbackground option
    style.theme_use("clam")
    style.configure("Treeview", background="blue",
                    fieldbackground="blue", foreground="white")


def clean_Treeview(treeview):
    """
      Removes all lines from a Treeview widget.

      Parameters:
      treeview: The Treeview widget to be cleaned.

      Returns:
      None
    """
    treeview.delete(*treeview.get_children())


def createGameTable():
    """
    Create and display two Tkinter windows with Treeview widgets, each containing a table with columns and headings.

    Parameters:
    None

    Returns:
    None
    """
    p1_gameTK = tk.Tk()
    p2_gameTK = tk.Tk()
    win_funcs(p1_gameTK,p2_gameTK)

    p1_game = ttk.Treeview(p1_gameTK)
    p2_game = ttk.Treeview(p2_gameTK)

    p1_game['columns'] = ('Guess', 'NumberGuessed_P1', 'Bh_P1', 'Nh_P1')
    p2_game['columns'] = ('Guess', 'NumberGuessed_P2', 'Bh_P2', 'Nh_P2')

    p1_game.column("#0", width=100,  stretch=NO)
    p1_game.column("Guess",anchor=CENTER, width=130, minwidth=30)
    p1_game.column("NumberGuessed_P1",anchor=CENTER,width=130, minwidth=50)
    p1_game.column("Bh_P1",anchor=CENTER,width=50, minwidth=30)
    p1_game.column("Nh_P1",anchor=CENTER,width=50, minwidth=30)

    p2_game.column("#0", width=100,  stretch=NO)
    p2_game.column("Guess",anchor=CENTER, width=130, minwidth=30)
    p2_game.column("NumberGuessed_P2",anchor=CENTER,width=130, minwidth=50)
    p2_game.column("Bh_P2",anchor=CENTER,width=50, minwidth=30)
    p2_game.column("Nh_P2",anchor=CENTER,width=50, minwidth=30)

    p1_game.heading("#0", text="Game Number", anchor=CENTER)
    p1_game.heading("Guess", text="Guess Num #", anchor=CENTER)
    p1_game.heading("NumberGuessed_P1", text="NumberGuessed_P1", anchor=CENTER)
    p1_game.heading("Bh_P1", text="Bh_P1", anchor=CENTER)
    p1_game.heading("Nh_P1", text="Nh_P1", anchor=CENTER)

    p2_game.heading("#0", text="Game Number", anchor=CENTER)
    p2_game.heading("Guess", text="Guess Num #", anchor=CENTER)
    p2_game.heading("NumberGuessed_P2", text="NumberGuessed_P2", anchor=CENTER)
    p2_game.heading("Bh_P2", text="Bh_P2", anchor=CENTER)
    p2_game.heading("Nh_P2", text="Nh_P2", anchor=CENTER)

    fill_table_templet(p1_game)
    fill_table_templet(p2_game)

    p2_game.pack()
    p1_game.pack()

    # Schedule the clean_Treeview() function to be called after a 10-second delay
    #root.after(10000, clean_Treeview, p1_game)

#
# def sendResult(T):
#     fill_table_templet(my_game)

def fill_table_templet(my_game):
    temp_iid=0
    temp_per=0
    #while bh.gameRounds_t:
    for game_index in bh.gameRounds_t: #all of them have the same parent
        for row_index in game_index:
            if row_index[0]==1:
                #my_game.insert(parent='', index='end', iid=temp_iid, text='1',
                #               values=row_index)
                my_game.insert(parent='', index='end', text=bh.gameRounds_t.index(game_index)+1,
                                   values=row_index)
                temp_per=temp_iid
            else:
                #my_game.insert(parent='', index='end', iid=temp_iid, text='1',
                #               values=row_index)
                my_game.insert(parent='', index='end', text='',
                                values=row_index)
                #my_game.move(str(temp_iid), str(temp_per), str(temp_per))
            #temp_iid+=1






root.mainloop()

















"""
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
#


def createGameTable():
    for i in range(7):
        for j in range(7):
            if(j>3):
               e = Entry(test, width=15, fg='red', font=('Arial', 12, 'bold'))
            else:
               e = Entry(test, width=15, fg='blue', font=('Arial', 12, 'bold'))
            e.grid(row=i,column=j)
            e.insert(END,listData[i][j])
            if(i>0):
                disable_entry(e)
            # if( j>0 and j<=3):
            #     color_bg1(e)
            # else:
            #     color_bg2(e)

            # e.insert(END,listData[])

"""






#var = StringVar()
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


#def democolorChange():b1.configure(bg="red",fg="yellow")

#labels = []
##def create_label(NumberOfGames):
    ##NumberOfGames=NumberOfGames+1
    # count = len(root.winfo_children())
    ##label = tk.Label(root, text=f"Label #{NumberOfGames}")
    ##label.grid(row=NumberOfGames,column=1,sticky=W,pady=2)
    ##labels.append(label)##


#b1=Button(root,text='button1',command=createGameTable())








#b1=Button(root,text='button1',command=createGameTable())








# b2=Button(root,text='Press for new label',command=create_label(NumberOfGames))
#NumberOfGames=NumberOfGames+1

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
