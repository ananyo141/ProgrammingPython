from tkinter.filedialog   import askopenfilename
from tkinter.messagebox   import askquestion
from tkinter.colorchooser import askcolor
from tkinter.simpledialog import askfloat

demos = dict(
    Open  = askopenfilename,
    Color = askcolor,
    Query = lambda: askquestion('Sure?', 'You entered sudo rm -rf /'),
    Float = lambda: askfloat('Prompt', 'Enter credit card number'),
)

