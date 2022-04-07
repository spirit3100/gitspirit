from weather import Weather
from serv import *
from tkinter import *
import tkinter


class MyApp(Tk,Weather):
    def __init__(self):
        Tk.__init__(self)
        self.title('Погода сейчас')
        self.geometry('260x200')
        self.resizable(False,False)
        self.cityEntry = Entry(self)
        self.labCity = Label(self, text = '')
        self.labelText = Label(self, text ='', justify = LEFT)
        self.set_ui()

    def set_ui(self):
        Label(self, text = 'Введите интересующий Вас город').pack( anchor = 'center')
        self.cityEntry.bind("<Return>", self.set_city)
        self.cityEntry.pack(fill = tkinter.X)
        self.labCity.pack()
        self.labelText.pack()

    def set_city(self, a):
        a = self.cityEntry.get()
        try:
            w_m = Weather(get_server(a))
            self.labCity['text'] = a
            self.labelText['text'] = w_m.set()
        except AttributeError:
            self.clear(self.labelText, '')
            self.clear(self.labCity,'try again')
        self.cityEntry.delete(0,'end')

    @staticmethod
    def clear(obj, text):
        obj['text'] = text

root = MyApp()
root.mainloop()