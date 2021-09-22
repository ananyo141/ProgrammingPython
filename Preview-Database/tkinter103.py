# create reply event function
# create main window and give title and icon
# give label for main window, text and pack
# create entry to enter name and pack
# create button, give text and event command (use lambda for correct execution)
# pack 
# execute window

from tkinter import *
from tkinter.messagebox import showinfo

def reply(name: str) -> None:
    '''Create a widget containing the given name as string'''
    showinfo(title = 'Reply', message = f'Hello {name}!')

main = Tk() # main window that hosts the entry text fields and submit button
main.title('Echo')
main.iconbitmap("py-blue-trans-out.ico")
Label(main, text = 'Enter your name:').pack(side = TOP)

entryField = Entry(main) # input field within main window
entryField.pack(side = TOP)

# button in the main window
button = Button(main, text='Submit', command=(lambda: reply(entryField.get())))
button.pack(side = RIGHT)

main.mainloop()
