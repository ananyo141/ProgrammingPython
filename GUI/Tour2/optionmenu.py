import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
option1 = tk.StringVar()
option2 = tk.StringVar()

tk.OptionMenu(root, option1, 'spam', 'eggs', 'toast').pack(expand=True, fill='x')
tk.OptionMenu(root, option2, 'ham', 'bacon', 'sausage').pack(expand=True, fill='x')

option1.set('spam')
option2.set('bacon')

getState = lambda: tk.messagebox.showinfo('Values', f"1: {option1.get()}\n"
                                                    f"2: {option2.get()}")
tk.Button(root, text='State', command=getState).pack()
root.mainloop()

