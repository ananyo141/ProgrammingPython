#!/usr/bin/env python
"read till eof and show squares" # this is basically an input redirection script
def interact():
    print("Hello stream!")
    while True:
        try:   inp = int(input("Enter Int: "))
        except EOFError: break
        except ValueError: continue
        else:  print(f"{inp} squared is {inp * inp}")
    print("\nBye!")

if __name__ == "__main__":
    interact()
