from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

fen = Tk()
can = Canvas(fen, width = 700, height = 500)


a=Variable()
ch = IntVar()

boutonrooteur=Button(text="Rooteur", command=lambda : ch.set(1))
boutonrooteur.pack(side=TOP)
boutonswitch=Button(text="Switch", command=lambda : ch.set(2))
boutonswitch.pack(side=TOP)
boutonpc=Button(text="PC", command=lambda : ch.set(3))
boutonpc.pack(side=TOP)
boutontrait=Button(text="Câble", command=lambda : ch.set(4))
boutontrait.pack(side=TOP)

can.pack()

def rooteur():
    imgr = Image.open("C:/Users/j06j0/rooteur.png")
    imgr = imgr.resize((40,40))
    imgroot = ImageTk.PhotoImage(imgr)
    return imgroot
imgroot=rooteur()

def switch():
    imgs = Image.open("switch.png")
    imgs = imgs.resize((40,40))
    imgsw = ImageTk.PhotoImage(imgs)
    return imgsw
imgsw=switch()

def pc():
    imgp = Image.open("pc.png")
    imgp = imgp.resize((40,40))
    imgpc = ImageTk.PhotoImage(imgp)
    return imgpc
imgpc=pc()

def clic_droit(event):
    X = event.x
    Y = event.y
    remove=can.find_closest(X,Y)
    can.delete(remove)
can.bind("<Button-3>",clic_droit)

def clic_gauche(event) :
    global a 
    global ch

    X = event.x
    Y = event.y
    ch.get()
    if ch.get() == 1 :
        a=imgroot
        can.create_image(X, Y, image=a)
    if ch.get() == 2 :
        a=imgsw
        can.create_image(X, Y, image=a)
    if ch.get() == 3 :
        a=imgpc
        can.create_image(X, Y, image=a)
    if ch.get() == 4 :
        can.create_line(X, Y, X, Y, fill='black')    
can.bind("<Button-1>",clic_gauche)

def move(event):
    global a
    global ch
    if ch.get() == 1 :
        a=imgroot
        can.create_image(event.x, event.y, image=a)
    if ch.get() == 2 :
        a=imgsw
        can.create_image(event.x, event.y, image=a)
    if ch.get() == 3 :
        a=imgpc
        can.create_image(event.x, event.y, image=a)
can.bind("<B2-Motion>",move)



fen.mainloop()