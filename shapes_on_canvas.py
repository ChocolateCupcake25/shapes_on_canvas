# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 20:58:29 2022

@author: HP
"""

from tkinter import*
from tkinter import ttk

root=Tk()
root.title("shapes_on_canvas")
root.geometry("700x700")
root.configure(bg="antique white")

canvas=Canvas(root,width=990,height=490,bg="misty rose",highlightbackground = "dark violet")
canvas.pack()

choose_color_lable=Label(root,text="Choose a color",font="monospace",bg="antique white")
startx_label=Label(root,text="startx",font="monospace",bg="antique white")
starty_label=Label(root,text="starty",font="monospace",bg="antique white")
endx_label=Label(root,text="endx",font="monospace",bg="antique white")
endy_label=Label(root,text="endy",font="monospace",bg="antique white")

cordinates_value = [10,50,100,200,300,400,500,600,800,900]
colors = ["red","blue","green","yellow","pink","purple","black","brown","gray"]
Colors_dropdown = ttk.Combobox(root,values= colors,width=10,state="readonly")
d1 = ttk.Combobox(root,values= cordinates_value,width=10,state="readonly")
d2 = ttk.Combobox(root,values= cordinates_value,width=10,state="readonly")
d3 = ttk.Combobox(root,values= cordinates_value,width=10,state="readonly")
d4 = ttk.Combobox(root,values= cordinates_value,width=10,state="readonly")

choose_color_lable.place(relx=0.6,rely=0.9,anchor=CENTER)
startx_label.place(relx=0.1,rely=0.85,anchor=CENTER)
starty_label.place(relx=0.3,rely=0.85,anchor=CENTER)
endx_label.place(relx=0.5,rely=0.85,anchor=CENTER)
endy_label.place(relx=0.7,rely=0.85,anchor=CENTER)

Colors_dropdown.place(relx=0.8,rely=0.9,anchor=CENTER)
d1.place(relx=0.2,rely=0.85,anchor=CENTER)
d2.place(relx=0.4,rely=0.85,anchor=CENTER)
d3.place(relx=0.6,rely=0.85,anchor=CENTER)
d4.place(relx=0.8,rely=0.85,anchor=CENTER)

keypress=""
oldx=0
oldy=0
newx=0
newy=0

def circle(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx=d1.get()
    oldy=d2.get()
    newx=d3.get()
    newy=d4.get()
    keypress="c"
    draw(keypress,oldx,oldy,newx,newy)

def rectangle(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx=d1.get()
    oldy=d2.get()
    newx=d3.get()
    newy=d4.get()
    keypress="r"
    draw(keypress,oldx,oldy,newx,newy)

def line(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx=d1.get()
    oldy=d2.get()
    newx=d3.get()
    newy=d4.get()
    keypress="l"
    draw(keypress,oldx,oldy,newx,newy)

def draw(keypress,oldx,oldy,newx,newy):
    fill_color=Colors_dropdown.get()
    if(keypress=="c"):
        circle=canvas.create_oval(oldx,oldy,newx,newy,width = 3,fill = fill_color)
    if(keypress=="r"):
        rectangle=canvas.create_rectangle(oldx,oldy,newx,newy,width = 3,fill = fill_color)
    if(keypress=="l"):
        line = canvas.create_line(oldx,oldy,newx,newy,width = 2,fill = fill_color)
    
        
root.bind("<c>",circle)
root.bind("<r>",rectangle)
root.bind("<l>",line)

root.mainloop()


