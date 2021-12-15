from tkinter import *

root = Tk()
root.protocol('WM_DELETE_WINDOW', lambda: None)
root.title("Main")
Label(root, text='This is the main window', height=10, width=50).pack(fill=BOTH)
Button(root, text='Quit Main', command=root.quit).pack(expand=True, padx=20, pady=20)
popup = Toplevel(root)
popup.title("Popup")
Label(popup, text='This is the popup window', height=10, width=50).pack(fill=BOTH)
Button(popup, text='Quit Popup', command=popup.destroy).pack(expand=True, padx=20, pady=20)
popup.protocol('WM_DELETE_WINDOW', lambda: None)
mainloop()

