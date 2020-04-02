"""
GenResearchO0Plan.py

Copyright (c) 2020 by Robert Russell Millward. All rights reserved.
"""

from tkinter import *

class GenResearch(Frame):
    def sayHi(self):
        print("hi Bob");
        return;

    def loadIt(self):
        print("Loaded");
        return;

    def createQuit(self):
        self.QUIT = Button(self);
        self.QUIT["text"] = "Quit";
        self.QUIT["fg"] = "red";
        self.QUIT["command"] = self.quit;
        self.QUIT.pack({"side": "left"});
        return;

    def createHi(self):
        self.hiThere = Button(self);
        self.hiThere["text"] = "Hello",
        self.hiThere["command"] = self.sayHi;
        self.hiThere.pack({"side": "left"});
        return;

    def createLoadData(self):
        self.loadData = Button(self);
        self.loadData["text"] = "Load",
        self.loadData["fg"] = "green";
        self.loadData["command"] = self.loadIt;
        self.loadData.pack({"side": "left"});
        return;

    def createWidgits(self):
        self.createHi();
        self.createLoadData();
        self.createQuit();
        return;

        

    def __init__(self, master=None):
        Frame.__init__(self, master);
        self.pack();
        self.createWidgits();


#END

