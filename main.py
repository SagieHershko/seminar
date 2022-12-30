import tkinter as tk
from tkinter import *
from tkinter import ttk

import bh
from bh import startgamebh

root = tk.Tk()
gamesNum = 0
digsNum = 0
avgP1 = 0
guessNum_p1 = 0

avgP2 = 0
guessNum_p2 = 0
par_index = 1

flag = 0
selected_digits = IntVar()
int_var = IntVar()
canvas = Canvas(root, width=232, height=80, bg="red")
redC = canvas.create_text(116, 20, text="Please be patient! ", fill="black", font='Helvetica 10 bold')
greenC = canvas.create_text(116, 50, text="This process can take some seconds to proceed.", fill="black",
                            font='Helvetica 7 bold')

COLORS = ['blue', 'green', 'red', 'purple', 'yellow']
global parent

spinbox_dig = tk.Spinbox(root, from_=4, to=8, textvariable=selected_digits, width=4, wrap=True, state="readonly")
spinbox_games = ttk.Spinbox(root, textvariable=int_var, from_=1, to=100, width=4, wrap=True, state="readonly")


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
    spinbox_dig.pack()


def spinbox_gamesNum():
    spinbox_games.set(10)
    spinbox_games.pack()


def real_start():
    global par_index
    par_index = 1
    startgamebh(digsNum, gamesNum)
    createGameTable()
    root.after(2000 * gamesNum, canva_type, 2)


def canva_type(flag):
    if flag == 0:
        canvas.pack()
        flag = 1
    elif flag == 1:
        return
    elif flag == 2:
        canvas.config(bg="green")
        won_str = "Player ____ won! \nAvg guesses: ___ "
        canvas.itemconfig(redC, text="")
        canvas.itemconfig(greenC, text=won_str, font='Helvetica 10 bold')
        canvas.pack()


def start_game():
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
    global flag
    gamesNum = int(spinbox_games.get())
    digsNum = int(spinbox_dig.get())
    if digsNum > 4:
        canva_type(flag)
        root.after(1000, real_start)
    else:
        real_start()


def starting_screen():
    """
    Display a screen with spinboxes and a button for selecting the number of digits and games in a game.

    Parameters:
    None

    Returns:
    None
    """
    Label(root, text="To start the game you have to choose:").pack()
    Label(root, text="How many digits would be in the number?").pack()
    spinbox_digits()
    Label(root, text="How many games would you like to play?").pack()
    spinbox_gamesNum()
    Button(root, text="Start playing!", command=start_game).pack()


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
    style.theme_use("clam")
    style.configure("Treeview", background="black",
                    fieldbackground="76b5c5", foreground="white")

    tk_window2.title('Player two window')
    tk_window2.attributes('-topmost', True)
    tk_window2.resizable(False, False)
    style = ttk.Style(tk_window2)
    style.theme_use("clam")
    style.configure("Treeview", background="blue",
                    fieldbackground="#blue", foreground="white", borderwidth=2, separatorcolor='white')


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
    win_funcs(p1_gameTK, p2_gameTK)

    p1_game = ttk.Treeview(p1_gameTK)
    p2_game = ttk.Treeview(p2_gameTK)

    p1_game['columns'] = ('Guess', 'NumberGuessed_P1', 'Bh_P1', 'Nh_P1', 'Table_Size_P1')
    p2_game['columns'] = ('Guess', 'NumberGuessed_P2', 'Bh_P2', 'Nh_P2', 'Table_Size_P2')

    p1_game.column("#0", width=100, stretch=NO)
    p1_game.column("Guess", anchor=CENTER, width=130, minwidth=30)
    p1_game.column("NumberGuessed_P1", anchor=CENTER, width=130, minwidth=50)
    p1_game.column("Bh_P1", anchor=CENTER, width=50, minwidth=30)
    p1_game.column("Nh_P1", anchor=CENTER, width=50, minwidth=30)
    p1_game.column("Table_Size_P1", anchor=CENTER, width=100, minwidth=50)

    p2_game.column("#0", width=100, stretch=NO)
    p2_game.column("Guess", anchor=CENTER, width=130, minwidth=30)
    p2_game.column("NumberGuessed_P2", anchor=CENTER, width=130, minwidth=50)
    p2_game.column("Bh_P2", anchor=CENTER, width=50, minwidth=30)
    p2_game.column("Nh_P2", anchor=CENTER, width=50, minwidth=30)
    p2_game.column("Table_Size_P2", anchor=CENTER, width=100, minwidth=50)

    p1_game.heading("#0", text="Game Number", anchor=CENTER)
    p1_game.heading("Guess", text="Guess Num #", anchor=CENTER)
    p1_game.heading("NumberGuessed_P1", text="NumberGuessed_P1", anchor=CENTER)
    p1_game.heading("Bh_P1", text="Bh_P1", anchor=CENTER)
    p1_game.heading("Nh_P1", text="Nh_P1", anchor=CENTER)
    p1_game.heading("Table_Size_P1", text="Table_Size_P1", anchor=CENTER)

    p2_game.heading("#0", text="Game Number", anchor=CENTER)
    p2_game.heading("Guess", text="Guess Num #", anchor=CENTER)
    p2_game.heading("NumberGuessed_P2", text="NumberGuessed_P2", anchor=CENTER)
    p2_game.heading("Bh_P2", text="Bh_P2", anchor=CENTER)
    p2_game.heading("Nh_P2", text="Nh_P2", anchor=CENTER)
    p2_game.heading("Table_Size_P2", text="Table_Size_P2", anchor=CENTER)

    start_index = int(gamesNum)
    fill_table_template(p1_game, 0)
    fill_table_template2(p2_game, start_index)

    p2_game.pack()
    p1_game.pack()


def insert_row(my_game, parent, values, game_index):
    if parent:
        my_game.insert(parent, index='end', text='', values=values)
    else:
        parent = my_game.insert(parent='', index='end', text=game_index, values=values)
    return parent


def insert_row2(my_game, parent, values, game_index):
    global par_index
    if parent:
        my_game.insert(parent, index='end', text='', values=values)
    else:
        parent = my_game.insert(parent='', index='end', text=game_index, values=values)
        par_index = par_index + 1
    return parent


def fill_table_template(my_game, index):
    parent = None
    if index >= (len(bh.gameRounds_t) / 2):
        return
    for row_index in bh.gameRounds_t[index]:
        if row_index[0] == 1:
            parent = None
            parent = insert_row(my_game, parent, row_index, bh.gameRounds_t.index(bh.gameRounds_t[index]) + 1)
        else:
            my_game.after(2000, insert_row, my_game, parent, row_index,
                          bh.gameRounds_t.index(bh.gameRounds_t[index]) + 1)
    my_game.after(2000, fill_table_template, my_game, index + 1)


def fill_table_template2(my_game, index):
    parent = None
    global par_index

    if index >= (len(bh.gameRounds_t)):
        return

    for row_index in bh.gameRounds_t[index]:
        if row_index[0] == 1:
            parent = None
            parent = insert_row2(my_game, parent, row_index, par_index)
        else:
            my_game.after(2000, insert_row2, my_game, parent, row_index, par_index)
    my_game.after(2000, fill_table_template2, my_game, index + 1)


root.mainloop()
