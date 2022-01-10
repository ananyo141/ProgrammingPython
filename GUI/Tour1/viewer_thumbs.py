import os, sys, mimetypes, math
from tkinter import *
from tkinter.messagebox import askokcancel
from PIL import Image
from PIL.ImageTk import PhotoImage

# Subclass Toplevel object to create specialized objects that display 
# a single image
class ImgViewer(Toplevel):
    def __init__(self, imgpath, parent=None, **kw):
        Toplevel.__init__(self, parent, **kw)
        self.title(os.path.basename(imgpath))
        self.imageObj = PhotoImage(file=imgpath)    # persistent image object
        self.configs  ()
        self.showimage()
        self.focus_set()

    def showimage(self):
        Label(self, image=self.imageObj).pack(expand=True, fill=BOTH)

    def configs(self):
        self.protocol('WM_DELETE_WINDOW', self.destroy)

# Make a tkinter container and attach images in the given directory
# according to given colsize or calculate NxN colwidth gridwise, each
# thumbnail should refer to the full image
class Viewer(Frame):
    ''' Assemble buttons with thumbnail images that map to view the
    full image using the ImgViewer popup windows '''
    def __init__(self, imgdir:str=os.getcwd(), parent=None, colsize:int=None, 
                            thumbsize:(int,int)=(100,100), **kw):
        Frame.__init__(self, parent, **kw)
        self.pack()                 # repack at convenience
        self.imgdir     = imgdir
        self.colsize    = colsize
        self.thumbsaves = []
        self.attachButtons()
        self.attachThumbs ()

    # Make thumbs with cache support, return filename and pillow image objs
    def makeThumbs(self, imgdir:str=None, thumbdir:str='.cache', 
                    size:(int, int)=(100, 100)) -> [(str, Image)]:
        ''' Create thumbnail image objects from the given imgdir
        and return a list of (filename, imageobj) to the caller,
        load the thumbnail if already cached from a previous run '''
        if imgdir is None: imgdir = self.imgdir                 # make thumbs of the
        thumbdir = os.path.join(imgdir, thumbdir)               # object directory if
        os.makedirs(thumbdir, exist_ok=True)                    # none specified

        images = []
        for filename in os.listdir(imgdir):
            filepath = os.path.join(imgdir, filename)
            if os.path.isdir(filepath): continue                # skip if directory
            ftype, enc = mimetypes.guess_type(filename)
            if ftype and ftype.split('/')[0] == 'image':
                thumbpath = os.path.join(thumbdir, filename)
                if os.path.exists(thumbpath):
                    imgObj = Image.open(thumbpath)
                else:
                    try:
                        imgObj = Image.open(filepath)
                        imgObj.thumbnail(size, Image.ANTIALIAS) # downsize filter
                        imgObj.save(thumbpath)
                    except Exception as exc:
                        print(f'Unable to create thumbnail for {filepath}, skipping...'
                            f'\nDetails: {str(exc)}\n\n',
                            file=sys.stderr)
                        continue                                # skip if error occurred
                images.append((filepath, imgObj))               # original image, thumbnail obj
        return images

    def attachThumbs(self):
        cfg = dict(
            expand=True, 
            fill=BOTH,
        )
        images = self.makeThumbs()
        if self.colsize is None or self.colsize < 1:
            self.colsize = int(math.sqrt(len(images)) + 0.5) # instead of math.ceil
        (thumbFrame := Frame(self)).pack(**cfg)   # master frame that contains 
        while images:                             # all the thumb rows
            thumbs, images = images[:self.colsize], images[self.colsize:]   # scoops the colsize-
            (row := Frame(thumbFrame)).pack(**cfg)                          # number of objs and
            for thumbname, thumbimg in thumbs:                              # deletes ones done,
                thumbPhoto = PhotoImage(thumbimg)                           # continues until none left
                # Install handler that opens the actual image, remember
                # each filename individually by applying default argument
                handler = lambda thumbname=thumbname: ImgViewer(thumbname).mainloop()
                Button(row, image=thumbPhoto, command=handler).pack(side=LEFT, **cfg)
                self.thumbsaves.append(thumbPhoto)  # save from being garbage collected
            
    def attachButtons(self):
        conf = lambda: askokcancel(title='Confirmation',  # if pressed ok, quit program
                       message='Are you sure you want to quit?') and sys.exit()

        Button(self, text='Quit', 
                command=conf
        ).pack(side=BOTTOM, expand=True, fill=BOTH)

def main():
    from tkinter.filedialog import askdirectory

    picdir = askdirectory(title='Choose Picture Directory')
    picdir = os.path.normpath(picdir) if picdir else sys.exit('No Directory Chosen')
    root = Tk()
    root.title("View")
    root.maxsize(width=900, height=600)
    root.minsize(width=200, height=100)
    viewer = Viewer(picdir, root)
    viewer.pack(expand=True, fill=BOTH)
    root.focus()
    mainloop()

if __name__ == '__main__': main()

