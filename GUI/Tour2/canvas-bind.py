import tkinter as tk

def objClick(event):
    print(f"Got Obj Click: {event.x = }, {event.y = }, "
        f"{event.widget = }, {event.widget.find_closest(event.x, event.y) = }\n")
def canvClick(event):
    print(f"Got canvas Click: {event.x = }, {event.y = }, {event.widget = }\n")

root = tk.Tk()
(canv := tk.Canvas(root, width=100, height=100, 
            bg='sky blue')).pack(expand=True, fill='both')
canv.create_text(30, 40, text='Text 1', tag='textTag')
canv.create_text(30, 70, text='Text 2', tag='textTag')
canv.tag_bind('textTag', '<Double-1>',  objClick)
canv.bind('<Double-1>', canvClick)

tk.mainloop()

