from tkinter import *
fen1 = Tk()
tex1 = Label(fen1, text='Bonjour tout le monde !', fg='red')
tex1.pack()
bou1 = Button(fen1, text='Quitter', command = fen1.destroy)
bou1.pack()
fen1.mainloop()