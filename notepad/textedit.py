from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class AppTextEdit(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.notePad = 'Notepad'
        self.title(self.notePad)
        self.geometry('1000x600')
        self.set_ui()
        self.file_p = None

    def set_ui(self):
        self.mainmenu = Menu(self)
        self.config(menu = self.mainmenu)
        self.f_menu = Menu(self.mainmenu, tearoff = 0)
        self.f_menu.add_command(label = 'new file', command = self.new_file)
        self.f_menu.add_command(label = 'open file', command = self.open_file)
        self.f_menu.add_command(label = 'save file', command = self.save_file)
        self.f_menu.add_command(label = 'save as', command = self.save_as)
        self.e_menu = Menu(self.mainmenu, tearoff = 0)
        self.e_menu.add_command(label = 'cut', command = self.cut_text)
        self.e_menu.add_command(label = 'copy', command = self.copy_text)
        self.e_menu.add_command(label = 'past', command = self.past_text)
        self.e_menu.add_command(label = 'delete', command = self.delete_field)
        self.v_menu = Menu(self.mainmenu, tearoff = 0)
        self.v_menu.add_command(label = 'font')
        self.v_menu.add_command(label = 'theme')
        self.v_menu.add_command(label = 'view')
        self.h_menu = Menu(self.mainmenu, tearoff = 0)
        self.h_menu.add_command(label = 'about', command = self.about)
        self.mainmenu.add_cascade(label = 'file', menu = self.f_menu)
        self.mainmenu.add_cascade(label = 'edit', menu = self.e_menu)
        self.mainmenu.add_cascade(label = 'view', menu = self.v_menu)
        self.mainmenu.add_cascade(label = 'help', menu = self.h_menu)
        self.text_field = Text(self,  borderwidth = 1, padx = 5, pady = 5, font = 'Arial 11')
        self.text_field.pack(expand = True, fill = BOTH)
        self.status_bar = Label(self, background = '#ECECEC', borderwidth = 2)
        self.status_bar.pack(side = BOTTOM, fill = X)

    def about(self):
        messagebox.showinfo('Notepad', 'version 1.0')

    def delete_field(self):
        self.text_field.delete(1.0, END)

    def new_file(self):
        if self.file_p:
            question = messagebox.askyesnocancel(title='save file?')
            if question == True:
                self.save_as()
            elif question == False:
                self.delete_field()
                self.file_p = None
                self.delete_field()
                self.title(self.notePad)

    def open_file(self):
        x = filedialog.askopenfilename(filetypes = (('text documents (*.txt)','*.txt'),('all files','*.*')))
        if x:
            self.file_p = x
            f = open(self.file_p, 'r').read()
            self.delete_field()
            self.text_field.insert(1.0, f)
            self.title(f'{self.file_p}  {self.notePad}')

    def save_as(self):
        x = filedialog.asksaveasfilename(filetypes = (('text documents (*.txt)','*.txt'),('all files','*.*')))
        if x:
            self.file_p = x
            self.save_file()

    def save_file(self):
        if self.file_p:
            f = open(self.file_p, 'w')
            text = self.text_field.get(1.0,'end')
            f.write(text)
            f.close()
            self.title(f'{self.file_p}  {self.notePad}')
        else:
            self.save_as()

    def cut_text(self):
        pass

    def past_text(self):
        pass

    def copy_text(self):
        pass

    def exit(self):
        pass


root = AppTextEdit()
root.mainloop()