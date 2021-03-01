from tkinter import *
from tkinter import font
from random import randrange
import random
import os

def clic_1():
    fen1.destroy()
    import Bataille_normal.py
    Bataille_normal.initialiser()

def clic_2():
    fen1.destroy()
    import Bataille_normal_26tours.py
    Bataille_normal_26tours.initialiser()


def clic_3():
    fen1.destroy()
    import bataille_d_addition_26tours.py
    la_bataille_d_addition_26tours.initialiser()

def clic_4():
    fen1.destroy()
    import la_bataille_d_addition.py 
    la_bataille_d_addition.initialiser()

def clic_5():
    fen1.destroy()
    import bataille_a_deux_26tours.py
    bataille_a_deux_26tours.initialiser()

def clic_6():
    fen1.destroy()
    import bataille_a_deux.py 
    bataille_a_deux.initialiser()

def clic_7():
    fen1.destroy()
    import la_bataille_découverte.py 
    la_bataille_découverte.initialiser()

def clic_8():
    fen1.destroy()
    import bataille_decouverte_26tours.py 
    bataille_decouverte_26tours.initialiser()

fen1=Tk()
Can=Canvas(fen1,width=225, height=500, bg='white')
Bataille = Label(fen1, text="BATAILLE", font=font.Font(family="Consolas",size=75))
Bataille.place(x=0,y=0, width=450, height=150)
mode_1 = Button(fen1, text="normale",command=clic_1)
mode_1.place(x=0,y=150, width=200, height=75)
mode_2 = Button(fen1, text="A deux",command=clic_2)
mode_2.place(x=0,y=300, width=200, height=75)
mode_3 = Button(fen1, text="la_bataille_d_addition_26tours",command=clic_3)
mode_3.place(x=0,y=450, width=200, height=75)
mode_4 = Button(fen1, text="la_bataille_d_addition",command=clic_4)
mode_4.place(x=0,y=225, width=200, height=75)
mode_5 = Button(fen1, text="bataille_a_deux_26tours",command=clic_5)
mode_5.place(x=0,y=525, width=200, height=75)
mode_6 = Button(fen1, text="bataille_a_deux",command=clic_6)
mode_6.place(x=0,y=375, width=200, height=75)
mode_7 = Button(fen1, text="la_bataille_découverte",command=clic_7)
mode_7.place(x=200,y=150, width=200, height=75)
mode_8 = Button(fen1, text="bataille_decouverte_26tours",command=clic_8)
mode_8.place(x=200,y=300, width=200, height=75)

Quit = Button(fen1, text="Quitter",command=fen1.quit)
Quit.place(x=0,y=600,width=200, height=50)

fen1.geometry("425x650")
fen1.mainloop()
