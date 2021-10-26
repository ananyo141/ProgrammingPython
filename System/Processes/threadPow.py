import _thread, time

def action(i):          # simple function
    print(i ** 32)

class Action:
    def __init__(self, i):
        self.i = i
    def action(self):   # bound method
        print(self.i ** 32)

_thread.start_new_thread(action, (2,))
_thread.start_new_thread((lambda: action(2)), ())
powObj = Action(2)
_thread.start_new_thread(powObj.action, ())

time.sleep(3)

