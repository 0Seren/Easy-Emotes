# -*- coding: utf-8 -*-
import Tkinter as tk
from Emote import Emote
import math
import os
import platform

class Application(tk.Tk):
    def __init__(self, searchtable = []):
        tk.Tk.__init__(self)
        self.geometry('{}x{}'.format(math.trunc(math.ceil(9.75 * self.winfo_fpixels( '1c' ))), math.trunc(math.ceil(7 * self.winfo_fpixels( '1c' )))))
        self.minsize(width = math.trunc(math.ceil(2.5 * self.winfo_fpixels( '1c' ))), height = 30)
        self.wm_title("Easy Emotes")

        self.searchtable = searchtable
        self.createWidgets()

    def createWidgets(self):
        self.searchbar = SearchFrame(self)
        self.bind("<KeyRelease>", self.onkeyrelease)
        self.searchbar.pack(fill="x", side="top")

        self.buttons = ButtonTable(self)
        self.buttons.bind("<Configure>", self.buttons.updateonresize)
        self.buttons.pack(fill="x", side = "top", expand = False)

    def onkeyrelease(self, key):
        #TODO: create emote searching buttons
        final = []
        entrydata = self.searchbar.gettext().lower().split()
        for pair in self.searchtable:
            for item in entrydata:
                if item in pair[0]:
                    final.append(pair[1].text)
        final = list(set(final))
        self.buttons.updatebuttontext(final)


class SearchFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)

        self.entryfield = tk.Entry(self)
        self.entryfield.grid(row=0, column=0, sticky="nesw")
        self.entryfield.focus_set()

        self.addemotebutton = tk.Button(self)
        self.addemotebutton.grid(row=0, column=1, sticky="ne")

    def gettext(self):
        return self.entryfield.get()


class ButtonTable(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.button_min_width = math.trunc(3.25 * parent.winfo_fpixels( '1c' )) #2.5cm in pixels
        self._widgets = []
        self.parent = parent
        self._button_texts = []
        self.old_num_rows = 0
        self.old_num_columns = 0
        self.num_rows = 0
        self.num_columns = 0

    def updatebuttontext(self, button_texts = []):
        self._button_texts = button_texts
        self.update(self.parent.winfo_width(), purge = True)

    def updateonresize(self, event):
        self.update(event.width)

    def update(self, width, purge = False):
        if purge:
            for array in self._widgets:
                for button in array:
                    button.destroy()
            self._widgets = []
            self.old_num_rows = 0
            self.old_num_columns = 0
            self.num_rows = 0
            self.num_columns = 0
        if len(self._button_texts) != 0:
            current_width = width
            self.num_columns = math.trunc(current_width / self.button_min_width)
            if(self.num_columns < 1):
                self.num_columns = 1
                current_width = self.button_min_width
            self.num_rows = math.trunc(math.ceil(len(self._button_texts) / (self.num_columns*1.0)))

            if self.num_rows != self.old_num_rows or self.num_columns != self.old_num_columns:
                self.old_num_rows = self.num_rows
                self.old_num_columns = self.num_columns
                for array in self._widgets:
                    for button in array:
                        button.destroy()

                self._widgets = []
                button_width = self.button_min_width
                current_text_index = 0
                num_buttons = 0
                for row in range(self.num_rows):
                    current_row = []
                    for column in range(self.num_columns):
                        if len(self._button_texts) > current_text_index:
                            button_text = self._button_texts[current_text_index]
                            button = tk.Button(self, text = button_text, width = button_width, command = lambda b = button_text: self.copytoclipboard(b))
                            button.grid(row=row, column=column, sticky="nsew")
                            current_row.append(button)
                            current_text_index = current_text_index + 1
                    self._widgets.append(current_row)

                for column in range(self.num_columns):
                    self.grid_columnconfigure(column, weight=1)
        try:
            self.parent.geometry('{}x{}'.format(self.parent.winfo_width(), (self._widgets[0][0].winfo_height() * (self.num_rows)) + self.parent.searchbar.winfo_height()))
        except IndexError:
            self.parent.geometry('{}x{}'.format(self.parent.winfo_width(), self.parent.searchbar.winfo_height()+30))

    def copytoclipboard(self, string):
        self.parent.clipboard_clear()
        self.parent.clipboard_append(string)
        self.parent.update()
        if platform.system() == 'Linux':
            try:
                os.system("echo -n '%s' | xclip -sel clip" % string.replace("\'", "\'\\\'\'").encode('utf-8'))
            except:
                print "Error with copying to clipboard [Linux]. Will not be able to paste after this program closes."
        elif platform.system() == 'Darwin': #Mac
            try:
                process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
                process.communicate(output.encode('utf-8'))
            except:
                print "Error with copying to clipboard [Mac]. Will not be able to paste after this program closes."
