import sys
import tkinter as tk
from PIL import ImageTk, Image

assert len(sys.argv) == 2, f"{sys.argv}\nSpecify Image path"

root = tk.Tk()
root.title('Canvas')
canv = tk.Canvas(root, width=300, height=300, bg='beige')
canv.pack(fill='both', expand=True)

for i in range(1, 20, 2):
    canv.create_line(5, i, 55, i)

oval = canv.create_oval(30, 30, 100, 100, fill='blue')
canv.create_line(0, 300, 150, 150, fill='green', width=15)
canv.create_arc(200, 200, 250, 100)

lab = tk.Label(canv, text='Spam', bg='black', fg='white')
lab.pack()
canv.create_window(30, 60, window=lab)
canv.create_text(60, 270, text='Ham')
canv.create_rectangle(100, 200, 150, 250, fill='red', width=10)
canv.create_line(45, 45, 100, 200)
canv.create_line(30, 65, 100, 250)
canv.tkraise(oval)

img = Image.open(sys.argv[1])
img.thumbnail((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)
canv.create_image(270, 30, image=photo, anchor='ne')

tk.mainloop()

