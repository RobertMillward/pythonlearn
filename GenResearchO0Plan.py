"""
GenResearchO0Plan.py

Copyright (c) 2020 by Robert Russell Millward. All rights reserved.
"""

from tkinter import *

class GenResearch(Frame):

#       Doers
#       - sayHi
#       - loadIt
#       - printOnLog
#
    def myDoSayHi(self):
        print("hi Bob");
        return;

    def myDoLoadIt(self):
        print("Loaded");
        return;
        
    def myDoPrintOnLog(self, event):
        print("Log->", self.contents.get());
        #self.contents.set("So there");
        return;

#       Creators
#       - Buttons
#       - Texts
#
# * Buttons (Create)
# ** quit
# ** hi
# ** load
    def myCreateQuit(self):
        self.QUIT = Button(self);
        self.QUIT["text"] = "Quit";
        self.QUIT["fg"] = "red";
        self.QUIT["command"] = self.quit; # probably class
        self.QUIT.pack({"side": "left"});
        return;

    def myCreateSayHi(self):
        self.hiThere = Button(self);
        self.hiThere["text"] = "Hello",
        self.hiThere["command"] = self.myDoSayHi;
        self.hiThere.pack({"side": "left"});
        return;

    def myCreateLoadData(self):
        self.loadData = Button(self);
        self.loadData["text"] = "Load",
        self.loadData["fg"] = "green";
        self.loadData["command"] = self.myDoLoadIt;
        self.loadData.pack({"side": "left"});
        return;
# * Entrys (Create)
# ** SeeEm
    def myCreateEntrySeeEm(self):
        self.contents = StringVar(); # this will go into the GUI fields
        self.contents.set("Greyed out");
        #self.maxsize(1000, 400);
        self.seeEm = Entry();
        self.seeEm.pack();
        self.seeEm["textvariable"] = self.contents;
        self.seeEm.bind('<Key-Return>', self.myDoPrintOnLog)
        return;

#       * Menues
#       ** Buttons
#       ** Texts
    def myCreateButtons(self):
        self.myCreateSayHi();
        self.myCreateLoadData();
        self.myCreateQuit();
        return;

    def myCreateEntrys(self):
        self.myCreateEntrySeeEm();
        return;

        
#       * Master creator
    def __init__(self, master=None):
        Frame.__init__(self, master);
        self.pack();
        self.myCreateEntrys();
        self.myCreateButtons();
        #for stuff in self: print(stuff);
        #master.title = "Master title";
        #self.title = "Self title";
        return;


#END

