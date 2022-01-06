from tkinter import *

def action():
    miles=input.get()
    km=int(miles)*1.609
    label3.config(text=km)

window=Tk()
window.title("Miles To Km Converter")
window.minsize(width=500,height=100)

label1=Label(text="Miles")
label1.place(x=450,y=40)

input=Entry(width=10,)
input.insert(0,string="0")
input.place(x=360,y=40)

button=Button(text="Convert",width=8,command=action)
button.place(x=200,y=60)

label1=Label(text="Km")
label1.place(x=450,y=80)

label3=Label(text="0")
label3.place(x=360,y=80)



window.mainloop()