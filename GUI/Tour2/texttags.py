import sys
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk

imagefilename = tk.filedialog.askopenfilename(title='Enter image', 
                   filetypes=(('JPEG', '.jpg'), ('PNG', '.png'), ('GIF', '.gif')))
if not imagefilename:
    sys.exit("No Image specified")

def handle(event):
    print('Handler called', file=sys.stderr)

root = tk.Tk()
root.title('Advanced Text')
textwid = tk.Text(root, font=('courier', 20, 'normal'), height=12, width=20)
textwid.pack(expand=True, fill='both')
textwid.insert('end', 'This is\n\nthe meaning\n\nof life\n\n')

(button := ttk.Button(textwid, text='Spam', command=lambda: handle(None))).pack()
textwid.window_create('end', window=button)
textwid.insert('end', '\n\n')

img = ImageTk.Image.open(imagefilename)
img.thumbnail((100,150), ImageTk.Image.ANTIALIAS)
photoimg = ImageTk.PhotoImage(img)
textwid.image_create('end', image=photoimg)

textwid.tag_add('demo', '1.5', '1.7')
textwid.tag_add('demo', '3.0', '3.3')
textwid.tag_add('demo', '5.3', '5.7')
textwid.tag_config('demo', font=('times', 25, 'bold'),
                           background='blue', foreground='white')
textwid.tag_bind('demo', '<Double-1>', handle)

root.mainloop()

