# Modify viewer-thumbs to grid instead of packing

import math
from tkinter import *
from PIL.ImageTk import PhotoImage
from viewer_thumbs import Viewer, ImgViewer

class ViewerGrid(Viewer):
    def attachThumbs(self):
        images = self.makeThumbs()
        if self.colsize is None or self.colsize < 1:
            self.colsize = int(math.ceil(math.sqrt(len(images))))
        (thumbFrame := Frame(self)).pack(expand=True, fill=BOTH)
        rownum = 0
        while images:
            colnum = 0
            thumbs, images = images[:self.colsize], images[self.colsize:]
            for thumbname, thumbimg in thumbs:
                def handler(filename=thumbname):
                    ImgViewer(filename).mainloop()

                thumbPhoto = PhotoImage(thumbimg)
                Button(thumbFrame, image=thumbPhoto, 
                                   command=handler,
                ).grid(row=rownum, column=colnum)
                self.thumbsaves.append(thumbPhoto)
                
                colnum += 1
            rownum += 1

if __name__ == '__main__':
    import viewer_thumbs
    viewer_thumbs.Viewer = ViewerGrid
    viewer_thumbs.main()

