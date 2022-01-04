from tkinter import *

root = Tk()
widget = Message(root, text='Oh by the way, which one\'s pink?')
widget.config(font=('comicsans', 30, 'italic'), bg='pink')
widget.config(width=300)
widget.pack(expand=True, fill=BOTH)
mainloop()

