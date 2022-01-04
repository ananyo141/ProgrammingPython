import sys, os
from tkinter import *
from PIL.ImageTk import PhotoImage
from tkinter.filedialog import askopenfilename

imgname = sys.argv[1] if len(sys.argv)>1 else askopenfilename(title='Enter image')
if imgname is None or not os.path.exists(imgname): 
    sys.exit("Invalid Filename")

root = Tk()
root.title(imgname)
root.protocol('WM_DELETE_WINDOW', lambda: None)

imgObj = PhotoImage(file=imgname)
(lab := Label(root, image=imgObj)).pack(expand=True, fill=BOTH)
lab.bind('<Double-1>', lambda event: root.quit())
print('Width=', imgObj.width(), '\nHeight=', imgObj.height(), sep='')

root.mainloop()

