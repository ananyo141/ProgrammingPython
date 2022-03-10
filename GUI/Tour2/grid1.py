from tkinter import *

colors = ['red', 'green', 'orange', 'white', 'yellow', 'blue']

if __name__ == '__main__':
    root = Tk()
    for ind, color in enumerate(colors):
        Label(root, text=color, width=25, relief=RIDGE).grid(row=ind, column=0)
        Entry(root, bg=color, fg='black', width=40, relief=GROOVE).grid(row=ind, column=1)
    mainloop()

