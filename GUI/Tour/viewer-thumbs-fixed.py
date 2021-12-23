from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage
import math, viewer_thumbs

class ViewerFixed(viewer_thumbs.Viewer):
    def attachThumbs(self):
        ''' The buttons that link to the actual image
        should have the dimension of the maximum 
        size of the image itself for alignment '''

        images = self.makeThumbs()
        if self.colsize is None or self.colsize < 1:
            self.colsize = int(math.sqrt(len(images)) + 0.5)
        (thumbFrame := Frame(self)).pack(expand=True, fill=BOTH)
        while images:
            thumbs, images = images[:self.colsize], images[self.colsize:]
            (row := Frame(thumbFrame)).pack(expand=True, fill=BOTH)
            for thumbname, thumbObj in thumbs:
                buttonsize = max(thumbObj.size)
                thumbPhoto = PhotoImage(thumbObj)
                handler = lambda thumbname=thumbname: viewer_thumbs.ImgViewer(thumbname).mainloop()
                Button(row, image=thumbPhoto, height=buttonsize, 
                            width=buttonsize, command=handler
                ).pack(side=LEFT, expand=True)
                self.thumbsaves.append(thumbPhoto)

if __name__ == '__main__':
    viewer_thumbs.Viewer = ViewerFixed
    viewer_thumbs.main()

