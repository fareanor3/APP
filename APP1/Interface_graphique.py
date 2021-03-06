from tkinter import *
from tkinter import font
from random import randrange
import random
import os

def clic_1():
    fen1.destroy()
    print("#########Bataille_normal#########")
    import Bataille_normal


def clic_2():
    fen1.destroy()
    print("#########Bataille_normal_26tours#########")
    import Bataille_normal_26tours


def clic_3():
    fen1.destroy()
    print("#########bataille_d_addition_26tours#########")
    import bataille_d_addition_26tours


def clic_4():
    fen1.destroy()
    print("#########la_bataille_d_addition#########")
    import la_bataille_d_addition


def clic_5():
    fen1.destroy()
    print("#########bataille_a_deux_26tours#########")
    import bataille_a_deux_26tours


def clic_6():
    fen1.destroy()
    print("#########bataille_a_deux#########")
    import bataille_a_deux


def clic_7():
    fen1.destroy()
    print("#########la_bataille_découverte#########")
    import la_bataille_découverte 


def clic_8():
    fen1.destroy()
    print("#########bataille_decouverte_26tours#########")
    import bataille_decouverte_26tours
    

fen1=Tk(className='Python - BATTAILLE DU GROUPE DES MEILLEURS -')
Can=Canvas(fen1,width=225, height=500, bg='white')
fen1['background']='#283747'
Bataille = Label(fen1, text="BATAILLE", fg = '#212F3C', font=font.Font(family="BOLD'",size=70),relief="raised")
Bataille.place(x=10,y=30, width=430, height=80)
mode_1 = Button(fen1, text="normale",relief="groove",command=clic_1)
mode_1.place(x=0,y=150, width=225, height=75)
mode_2 = Button(fen1, text="Bataille_normal_26tours",relief="groove",command=clic_2)
mode_2.place(x=225,y=150, width=225, height=75)
mode_3 = Button(fen1, text="la_bataille_d_addition_26tours",relief="groove",command=clic_3)
mode_3.place(x=225,y=225, width=225, height=75)
mode_4 = Button(fen1, text="la_bataille_d_addition",relief="groove",command=clic_4)
mode_4.place(x=0,y=225, width=225, height=75)
mode_5 = Button(fen1, text="bataille_a_deux_26tours",relief="groove",command=clic_5)
mode_5.place(x=225,y=375, width=225, height=75,)
mode_6 = Button(fen1, text="bataille_a_deux",relief="groove",command=clic_6)
mode_6.place(x=0,y=375, width=225, height=75)
mode_7 = Button(fen1, text="la_bataille_découverte",relief="groove",command=clic_7)
mode_7.place(x=0,y=300, width=225, height=75)
mode_8 = Button(fen1, text="bataille_decouverte_26tours",relief="groove",command=clic_8)
mode_8.place(x=225,y=300, width=225, height=75)

Quit = Button(fen1, text="Quitter",relief="sunken",command=fen1.quit)
Quit.place(x=112.5,y=450,width=225, height=50)

fen1.geometry("450x500")
fen1.mainloop()