"""
HelloWorldO0.py

Copyright (c) 2020 by Robert Russell Millward. All rights reserved.
"""

from tkinter import *

class GenResearch(Frame):
    def sayHi(self):
        print("hi Bob");

    def createWidgits(self):
        self.QUIT = Button(self);
        self.QUIT["text"] = "Quit";
        self.QUIT["fg"] = "red";
        self.QUIT["command"] = self.quit;

        self.QUIT.pack({"side": "left"});

        self.hi_there = Button(self);
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.sayHi;

        self.hi_there.pack({"side": "left"});

    def __init__(self, master=None):
        Frame.__init__(self, master);
        self.pack();
        self.createWidgits();

root = Tk();
app = GenResearch(master=root);
app.mainloop();
root.destroy();

#END

