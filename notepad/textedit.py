import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class AppTextEdit(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.notePad = 'Notepad'
        self.title(self.notePad)
        self.geometry('200x100')
        self.m_menu = Menu(self)
        self.f_menu = Menu(self.m_menu, tearoff = 0)
        self.e_menu = Menu(self.m_menu, tearoff = 0)
        self.v_menu = Menu(self.m_menu, tearoff = 0)
        self.h_menu = Menu(self.m_menu, tearoff = 0)
        self.text_field = Text(self,  borderwidth = 1, padx = 5, pady = 5, font = 'Arial 11')
        self.status_bar = Label(self, background = '#ECECEC', borderwidth = 2)
        self.file_p = None
        self.memory = ''
        self.set_ui()

    def set_ui(self):
        self.config(menu = self.m_menu)
        self.f_menu.add_command(label = 'new file', command = self.new_file)
        self.f_menu.add_command(label = 'open file', command = self.open_file)
        self.f_menu.add_command(label = 'save file', command = self.save_file)
        self.f_menu.add_command(label = 'save as', command = self.save_as)

        self.e_menu.add_command(label = 'cut', command = self.cut_text)
        self.e_menu.add_command(label = 'copy', command = self.copy_text)
        self.e_menu.add_command(label = 'past', command = self.past_text)
        self.e_menu.add_command(label = 'delete', command = self.del_text)

        self.v_menu.add_command(label = 'font')
        self.v_menu.add_command(label = 'theme')
        self.v_menu.add_command(label = 'view')

        self.h_menu.add_command(label = 'about', command = self.about)

        self.m_menu.add_cascade(label ='file', menu = self.f_menu)
        self.m_menu.add_cascade(label ='edit', menu = self.e_menu)
        self.m_menu.add_cascade(label ='view', menu = self.v_menu)
        self.m_menu.add_cascade(label ='help', menu = self.h_menu)

        self.text_field.pack(expand = True, fill = BOTH)
        self.status_bar.pack(side = BOTTOM, fill = X)

    @staticmethod
    def about():
        messagebox.showinfo('Notepad', 'version 1.0')

    def new_file(self):
        if self.file_p:
            question = messagebox.askyesnocancel(title = 'save file?')
            if question:
                self.save_as()
            elif not question:
                self.text_field.delete(1.0, END)
                self.file_p = None
                self.title(self.notePad)

    def open_file(self):
        x = filedialog.askopenfilename(filetypes = (('text documents (*.txt)', '*.txt'), ('all files', '*.*')))
        if x:
            self.file_p = x
            f = open(self.file_p, 'r').read()
            self.text_field.delete(1.0, END)
            self.text_field.insert(1.0, f)
            self.title(f'{self.file_p}  {self.notePad}')

    def save_as(self):
        x = filedialog.asksaveasfilename(filetypes = (('text documents (*.txt)', '*.txt'), ('all files', '*.*')))
        if x:
            self.file_p = x
            self.save_file()

    def save_file(self):
        if self.file_p:
            f = open(self.file_p, 'w')
            text = self.text_field.get(1.0, 'end')
            f.write(text)
            f.close()
            self.title(f'{self.file_p}  {self.notePad}')
        else:
            self.save_as()

    def cut_text(self):
        self.copy_text()
        self.del_text()

    def past_text(self):
        self.del_text()
        self.text_field.insert(tkinter.INSERT, self.memory)

    def copy_text(self):
        a, b = self.get_index_text()
        if a is not None:
            self.memory = self.text_field.get(a, b)
        else:
            self.memory = ''

    def del_text(self):
        a, b = self.get_index_text()
        if a is not None:
            self.text_field.delete(a, b)

    def get_index_text(self):
        try:
            first_l = self.text_field.index(tkinter.SEL_FIRST)
            last_l = self.text_field.index(tkinter.SEL_LAST)
            return first_l, last_l
        except Exception:
            return None, None

    def exit(self):
        pass

root = AppTextEdit()
root.mainloop()
