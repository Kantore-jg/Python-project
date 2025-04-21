from tkinter import *


window = Tk()
window.title("Mile to Km converter")
window.minsize(500,600)

def miles_to_km():
    miles = float(mile_input.get())
    km = round(miles * 1.609)
    km_label_show.config(text=km)


is_equal_to_label = Label(text="is equal to",font=("Arial",25,"bold"))
is_equal_to_label.grid(column=0,row=1)

miles_label = Label(text="Miles",font=("Arial",25,"bold"))
miles_label.grid(column=2,row=0)

km_label = Label(text="Km",font=("Arial",25,"bold"))
km_label.grid(column=2,row=1)

km_label_show = Label(text=0,font=("Arial",25,"bold"))
km_label_show.grid(column=1,row=1)

mile_input = Entry(width=24)
mile_input.grid(column=1,row=0)


button = Button(text="Calculate",font=("Times new Romans",24,"bold"),command=miles_to_km)
button.grid(column=1,row=2)







window.mainloop()