# -*- coding: utf-8 -*-
import Tkinter as tk
from Emote import Emote
import os
import platform

class Application(tk.Frame):
    def __init__(self, master = None, searchtable = []):
        tk.Frame.__init__(self, master)
        self.buttons = [[tk.Button(), tk.Button()], [tk.Button(), tk.Button()], [tk.Button(), tk.Button()]]
        self.entry = tk.Entry()
        self.searchtable = searchtable
        self.grid(sticky = tk.N + tk.E + tk.W + tk.S)
        self.createWidgets()

    def copytoclipboard(self, button):
        string = button.cget("text")
        if platform.system() == 'Linux':
            os.system("echo -n '%s' | xclip -sel clip" % string.replace("\'", "\'\\\'\'").encode('utf-8'))
        elif platform.system() == 'Windows':
            self.clipboard_clear()
            self.clipboard_append(string)
            self.update()
        elif platform.system() == 'Darwin': #Mac
            process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
            process.communicate(output.encode('utf-8'))

    def keyrelease(self, key):
        #TODO: create emote searching buttons
        final = []
        entrydata = self.entry.get().lower().split()
        for pair in self.searchtable:
            for item in entrydata:
                if item in pair[0]:
                    final.append(pair[1])
        final = list(set(final))
        curr = 0
        for i in self.buttons:
            for button in i:
                if curr < len(final):
                    button.config(text = final[curr].text)
                    curr += 1
                else:
                    button.config(text = "")

    def createWidgets(self):
        top=self.winfo_toplevel()
        top.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)
        #create entry field
        self.entry.grid(row = 0, column = 0, sticky = tk.N + tk.E + tk.W, columnspan=2)
        self.entry.bind("<KeyRelease>", self.keyrelease)
        self.entry.focus_set()
        #TODO: create 'new emote' button
        #create emote buttons
        for i in range(3):
            top.rowconfigure(i + 1, weight = 2)
            for n in range(2):
                top.columnconfigure(n, weight = 2)
                self.buttons[i][n].grid(row = i + 1, column = n, sticky = tk.N + tk.E + tk.W + tk.S)
                self.buttons[i][n].config(text = "", command = lambda b=self.buttons[i][n]: self.copytoclipboard(b))
