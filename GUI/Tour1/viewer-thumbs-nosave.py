import os, mimetypes
from viewer_thumbs import Viewer
from PIL import Image

class ViewerNoCache(Viewer):
    def makeThumbs(self, imgdir=None, thumbdir='.thumbs', size=(100, 100)):
        ''' Create thumbnails on every program run, don't save or cache
        them in a directory '''
        
        if imgdir is None: imgdir = self.imgdir
        files = os.listdir(imgdir)
        images = []
        for filename in files:
            filepath = os.path.join(imgdir, filename)
            ftype, enc = mimetypes.guess_type(filepath)
            if ftype and ftype.split('/')[0] == 'image':
                try:
                    thumbObj = Image.open(filepath)
                    thumbObj.thumbnail(size, Image.ANTIALIAS)
                    images.append((filepath, thumbObj))
                except: print(f'Skipping {filepath}')
        return images

if __name__ == '__main__':
    import viewer_thumbs                    # import viewer_thumbs script
    viewer_thumbs.Viewer = ViewerNoCache    # and dynamically substitute the
    viewer_thumbs.main()                    # Viewer class to make it's main function
                                            # run the modified subclass
    
