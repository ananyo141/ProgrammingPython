import sys, os, math, logging
import tkinter as tk
from tkinter.messagebox import askokcancel
from tkinter import ttk
from PIL.ImageTk import PhotoImage

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'Tour1'))
import viewer_thumbs as vt

logging.basicConfig(
        level    = logging.DEBUG,
        format   = '%(asctime)s - %(levelname)s - %(lineno)d - %(message)s',
        datefmt  = '%d/%m/%Y - %I:%M:%S %p',
        #filename = 'viewer_thumbs_scrolled.log', filemode='w',
)

logging.disable(logging.CRITICAL)

# Display the full image using tkinter canvas widget
class FullImgViewer(vt.ImgViewer):
    def showimage(self):
        ''' 
        Override the base method that uses label and use canvas instead,
        make scrollable if image dimensions exceed that of display screen 
        '''
        maxwidth, maxheight     = self.winfo_screenwidth(), self.winfo_screenheight()
        imageWidth, imageHeight = self.imageObj.width(), self.imageObj.height();        logging.debug(f'{imageWidth = }, {imageHeight = }')
        makeyscroll = imageHeight > maxheight
        makexscroll = imageWidth  > maxwidth
        displayWidth  = maxwidth  if makexscroll else imageWidth
        displayHeight = maxheight if makeyscroll else imageHeight
        canv = tk.Canvas(self, width=displayWidth, height=displayHeight)
        if makexscroll:
            xscroll = ttk.Scrollbar(self, command=canv.xview, orient='horizontal')
            canv.config(xscrollcommand=xscroll.set)
            xscroll.pack(side='bottom', fill='x')
        if makeyscroll:
            yscroll = ttk.Scrollbar(self, command=canv.yview)
            canv.config(yscrollcommand=yscroll.set)
            yscroll.pack(side='right', fill='y')
        canv.config(scrollregion=(0, 0, imageWidth, imageHeight))
        canv.create_image(0,0, image=self.imageObj, anchor='nw')
        canv.pack(expand=True, fill='both')

# Use a canvas to make a scrollable viewer
class CanvViewer(vt.Viewer):
    def attachThumbs(self, canvsize=(300,300), buttonsize=(90,70), colsize=5):
        ''' 
        Use a canvas widget instead of nested frames to achieve
        a scrollable widget that prevents clipping if number of images
        is large 
        '''
        images = self.makeThumbs()
        buttonwidth, buttonheight = buttonsize
        rowsize = math.ceil(len(images) / colsize);                                   logging.info(f'{len(images) = }, {rowsize = }')
        buttnscrollregion = (0, 0, colsize * buttonwidth, rowsize * buttonheight);    logging.info(f'{buttnscrollregion = }')
        canv = tk.Canvas(self, scrollregion=buttnscrollregion,
                    width=canvsize[0], height=canvsize[1])

        # Insert the buttons
        row = 0
        while images:
            col = 0
            imgRow, images = images[:colsize], images[colsize:]
            for thumbname, thumbimg in imgRow:
                thumbPhoto = PhotoImage(thumbimg)
                handler = (lambda thumbname=thumbname: 
                           FullImgViewer(thumbname).mainloop())
                (link := tk.Button(canv, width=buttonwidth, height=buttonheight,
                                command=handler, image=thumbPhoto)).pack()
                canv.create_window(col, row, window=link, width=buttonwidth, 
                        height=buttonheight, anchor='nw');                           logging.debug(f'{row = }, {col = }')
                self.thumbsaves.append(thumbPhoto)
                col += buttonwidth
            row += buttonheight

        logging.debug(f'{row = }, {col = }')
        if buttnscrollregion[3] > canvsize[1]:  # make y scroll
            yscroll = ttk.Scrollbar(self, command=canv.yview)
            canv.config(yscrollcommand=yscroll.set)
            yscroll.pack(side='right', fill='y')
        if buttnscrollregion[2] > canvsize[0]:  # make x scroll
            xscroll = ttk.Scrollbar(self, command=canv.xview, orient='horizontal')
            canv.config(xscrollcommand=xscroll.set)
            xscroll.pack(side='bottom', fill='x')
        canv.pack(expand=True, fill='both')
    
    def attachButtons(self):
        conf = lambda: askokcancel(title='Confirmation',
                       message='Are you sure you want to exit?') and sys.exit()
        ttk.Button(self, text='Quit', command=conf).pack(side='bottom', fill='x')

if __name__ == '__main__':
    vt.Viewer    = CanvViewer
    vt.ImgViewer = FullImgViewer
    vt.main()

