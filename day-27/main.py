from tkinter import *


window = Tk()
window.title("my first GUI program")
window.minsize(500,300)
window.config(padx=100,pady=200)

my_label = Label(text="i'm a Label",font=("Times new Roman",24,"bold"))
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)

def button_clicked():
    print("clicked successfull")
    new_text = input.get()
    my_label.config(text=new_text)
button = Button(text="click me",font=("Times new Romans",24,"bold"),command=button_clicked)
button.grid(column=1,row=1)

button1 = Button(text="new text",font=("Arial",24,"bold"))
button1.grid(column=2,row=0)

input = Entry(width=24)
input.grid(column=3,row=3)











# my_label["text"] = "new text"
# my_label.config(text="new text")








window.mainloop()