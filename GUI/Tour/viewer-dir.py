# Display all the images in the given directory

import sys, os, mimetypes
from tkinter import *
from tkinter.filedialog import askdirectory
from PIL.ImageTk import PhotoImage

dirname = sys.argv[1] if len(sys.argv) > 1 else askdirectory(
                                    title='Choose Image Directory')
if not os.path.exists(dirname) or dirname is None:
    sys.exit("Invalid Directory")

root = Tk()
Button(root, text='Quit', 
             command=root.quit,
             font=('courier', 20, 'bold'),
).pack(expand=True, fill=BOTH)

saveobjs = []
for filename in os.listdir(dirname):
    filepath = os.path.join(dirname, filename)
    ftype, enc = mimetypes.guess_type(filename)
    if ftype and ftype.split('/')[0] == 'image':
        try:
            imgobj = PhotoImage(file=filepath)
        except:
            print('Skipping:', filename, '...', file=sys.stderr)
            continue
        saveobjs.append(imgobj)
        win = Toplevel(root)
        win.title(filename)
        Label(win, image=imgobj).pack(expand=True, fill=BOTH)

if not saveobjs: sys.exit('No images found')
mainloop()

