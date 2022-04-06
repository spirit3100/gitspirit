import tkinter
from weather import Weather
from serv import *
from tkinter import *

class MyApp(Tk,Weather):
    def __init__(self):
        global m
        Tk.__init__(self)
        self.title('Погода сейчас')
        self.geometry('260x200')
        self.resizable(False,False)
        self.set_ui()

    def set_ui(self):
        Label(self, text = 'Введите интересующий Вас город').pack( anchor = 'center')
        self.cityEntry = Entry(self)
        self.cityEntry.bind("<Return>", self.set_city)
        self.cityEntry.pack(fill = tkinter.X)
        self.labCity = Label(self, text = '')
        self.labCity.pack()
        self.label = Label(self, text = '',justify = LEFT)
        self.label.pack()

    def set_city(self, a):
        a = self.cityEntry.get()
        try:
            m = Weather(get_server(a))
            self.labCity['text'] = a
            self.label['text'] = m.set()
        except AttributeError:
            self.clear(self.label,'')
            self.clear(self.labCity,'try again')
        self.cityEntry.delete(0,'end')

    def clear(self, obj, text):
        obj['text'] = text
root = MyApp()
root.mainloop()

