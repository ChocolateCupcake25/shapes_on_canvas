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

root.mainloop()


