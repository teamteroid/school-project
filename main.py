from tkinter import *
import time

from turtle import turtle
from login import login
from wcf import wcf
from flappy import flappy
from ttt import ttt


logedin = 0

consolewindow = Tk()
consolewindow.title("VVLC Gaming Console")
consolewindow.geometry("600x300")


def loginer():
    login_info = login.login(consolewindow)
    loginbtn["state"] = "disabled"
    tttbtn["state"] = "normal"
    flappybtn["state"] = "normal"
    wcfbtn["state"] = "normal"
    turtlebtn["state"] = "normal"
    return login_info


def turtlegame():
    turtle.game(1232, consolewindow)


def flappygame():
    flappy.game(12312, consolewindow)


def wcfgame():
    wcf.game(1231, consolewindow)


def tttgame():
    ttt.game(1234, consolewindow)


def crediter():
    pass


flappybtn = Button(consolewindow, text="Play Flappy Bird", command=flappygame)
flappybtn.pack()
flappybtn["state"] = "disabled"
turtlebtn = Button(consolewindow, text="Play Turtle Race", command=turtlegame)
turtlebtn.pack()
turtlebtn["state"] = "disabled"
wcfbtn = Button(consolewindow, text="Play WCF", command=wcfgame)
wcfbtn.pack()
wcfbtn["state"] = "disabled"
tttbtn = Button(consolewindow, text="Play TicTacToe", command=tttgame)
tttbtn.pack()
tttbtn["state"] = "disabled"
loginbtn = Button(consolewindow, text="Login", command=loginer)
loginbtn.pack()
creditsbutton = Button(consolewindow, text="Credits", command=crediter)
creditsbutton.pack()

consolewindow.mainloop()
