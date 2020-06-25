from tkinter import *
from difflib import get_close_matches
import english_Dictionary

class Window(object):

    def __init__(self,window):

        self.window = window
        self.window.wm_title("English Dictionary")
        self.word = StringVar()
        self.e1 = Entry(window, textvariable = self.word)
        self.e1.grid(row = 0, column = 0, padx = 10, pady = 50)

        self.listbox = Listbox(window, height = 6, width = 90)
        self.listbox.grid(row = 4, column = 0, padx = 25, pady = 25)

        sb1 = Scrollbar(window)
        sb1.grid(row = 2, column = 2, rowspan = 9)

        self.listbox.configure(xscrollcommand = sb1.set)
        sb1.configure(command = self.listbox.xview)

        self.listbox.bind('<<ListboxSelect>>', self.search_command)

        self.b2 = Button(window, text = "clear", width = 5, command = self.clear_command )
        self.b2.grid(row = 0, column = 1, sticky =W)

        self.b1 = Button(window, text = "search", width = 12, command = self.search_command)
        self.b1.grid(row = 1, column = 0)

        

    def search_command(self):
        try:
            global l1, label_0
            self.listbox.delete(0, END)
            result = english_Dictionary.translate(self.word.get())
            if type(result) is list:
                for item in result:
                    self.listbox.insert(END, item)
            elif result == 1:
                if len(get_close_matches(self.word.get(), english_Dictionary.data.keys())) > 0:
                    close_match = get_close_matches(self.word.get(), english_Dictionary.data.keys(), cutoff= 0.8)
                    label_0 = Label(window, text = "Did you mean: ")
                    label_0.grid(row = 1, column = 0)
                    l1 = Label(window, text = close_match[0])
                    l1.grid(row = 2, column = 0)
                    self.specific_word(close_match[0])
                else:
                    self.listbox.insert(0, "Word not found..!")
            else:
                self.listbox.insert(END, item)
        except IndexError:
            pass

    def specific_word(self, correct_word):
        try:
            self.listbox.delete(0, END)
            result = english_Dictionary.translate(correct_word)
            for item in result:
                self.listbox.insert(END, item)
        except IndexError:
            pass
    def clear_command(self):
        try:
            self.e1.delete(0, END)
            self.listbox.delete(0, END)
            label_0.destroy()
            l1.destroy()
        except:
            pass

window = Tk()
Window(window)
window.mainloop()