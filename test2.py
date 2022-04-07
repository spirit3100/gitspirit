import tkinter
from tkinter import *

root = Tk()
entry = Text()
entry.pack()

def command():
    print("Cursor position:", entry.index(tkinter.INSERT))
    selection_from = entry.index(tkinter.SEL_FIRST)
    selection_to = entry.index(tkinter.SEL_LAST)
    print(f'first {selection_from}')
    print(f'last {selection_to}')
    print(f"Selection from {selection_from} to {selection_to}")
    print("Selected text:", entry.get()[selection_from:selection_to])

button = Button(text="Press me", command=command)
button.pack()

root.mainloop()