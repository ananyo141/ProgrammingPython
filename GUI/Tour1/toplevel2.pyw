from tkinter import *

trees = (("The Larch!",       "light blue"),
        ("The Pine!",         "light green"),
        ("The Giant Redwood", "red"))

root = Tk()
for tree, color in trees:
    popup = Toplevel(root)
    popup.title('Sing...')
    popup.protocol('WM_DELETE_WINDOW', lambda: None)
    frame = Frame(popup)
    frame.pack(expand=True, fill=BOTH)
    button = Button(frame, text=tree, font=('times', 20, 'bold italic'), command=popup.destroy)
    button.config(bg='black', fg=color, bd=5, relief=GROOVE)
    button.config(height=5, width=20)
    button.pack(expand=True, fill=BOTH, padx=20, pady=10)

root.title('Sing...')
rootframe = Frame(root, height=10, width=50)
rootframe.pack(expand=True, fill=BOTH)
Label(rootframe, text='Root Window', height=10, width=50).pack(side=TOP, expand=True, fill=Y)
Button(rootframe, text='Quit All', command=root.quit).pack(expand=True, padx=10, pady=10)
mainloop()

