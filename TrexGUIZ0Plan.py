"""
TrexGUIZ0Plan.py - Services for importing data to the thesarus and GUI.
Using this thesarus a producer or consumer can locate a common field to process.

It can, with a few appropriate changes, connect to anyEnv Uci driven.
It knows about ArchEdenZ0Plan Uci so covers much of the processing.

*Trex is short for thesarus, right?!

Copyright (c) 2020, Robert Russell Millward, all rights reserved.
"""
#from ArchEdenZ0Plan import * #as anyEnv
import ArchEdenZ0Plan as anyEnv
from tkinter import *
from datetime import *

def rptOpenDateRight():
    "Print a common look and feel date at the end of the line."
    gotIt = datetime.datetime.today();
    print("%02d" %gotIt.day, end='');
    print("/%02d" %gotIt.month, end='');
    print("/%04d" %gotIt.year, end='');
    print(" %02d" %gotIt.hour, end='');
    print(":%02d" %gotIt.minute, end='');
    print(end='\n');
    return;


class trexguiField():
    def __init__(self, uci, hdrFmtQ, synonyms, value='X'):
        print("Field", synonyms, uci.value, self);
        
        self.uci = uci;
        self.names = synonyms;
        #self.hdrFmt = hdrFmt;
        self.contents = StringVar();
        self.contents.set(synonyms[0]); # column header
        
        self.ieCtl = Entry();
        self.ieCtl.pack();
        self.ieCtl["textvariable"] = self.contents;
        #self.ieCtl.bind('<Key-Return>', trexguiField.TODO);
        return;

# The trexxCtrl is a single argument to the functions that do the work.
# the baseUci is the lowest numbered Uci
# of the field group served by the child.
root = Tk();

class trexxCtrl():
    def __init__(self, category, fields, baseUci, viaInCol, viaUci):
        print("Control", baseUci.value, self);
        self.category       = category;
        self.subCategory    = "TBD";
        self.refFields      = fields;
        self.baseUci        = baseUci;
        self.refViaInCol    = viaInCol;
        self.refViaUci      = viaUci;
        return;
    
# This the humble thesarus prototype or parent.
# Children of this class are useful.
#
class TrexGUIThesarus():

    # These variables must be overridden in any child.
    # one reverse index of each kind per field
    thrsViaInCol = [-1,-1]; # varies by file being imported
    thrsViaUci = [-1,-1,-1];

    # the data fields
    thrsFields = [
        trexguiField(anyEnv.Uci.metroRowId, "%-8s", ["rowId"]   ),
        trexguiField(anyEnv.Uci.countryName, "%-8s", ["country", "nation"])];

    thrsCtrl = trexxCtrl("TREX", thrsFields, anyEnv.Uci.metroRowId, thrsViaInCol, thrsViaUci);

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


# The *Your* services serve any instance.
# They do not need to be overridden.
    def initYourAtStart(yourCtrl):
        "Initialize your thesarus."
        #print("Initializing Your", yourCtrl.refFields[2].uci);
        yourViaUci = yourCtrl.refViaUci;
        yourFields = yourCtrl.refFields;
        
        thrsIx = -1;
        for tr in yourFields:
            thrsIx = thrsIx + 1;
            yourViaUci[tr.uci.value - yourCtrl.baseUci.value] = thrsIx;
            #print("########", tr.uci, "=", thrsIx, "##");
        return;

    def initYourForCvsHeader(yourCtrl, csvColName, csvColNbr):
        "Initialize your one column Ix by locating its matching synonym."
        #print("InitializingZ YourCsv", yourCtrl.refFields[2].uci);
        #print("InitializingZ YourCsv", yourCtrl.refViaUci[2]);
        #print("InitializingZ YourCsv", yourCtrl.refViaInCol[2]);
        yourViaInCol = yourCtrl.refViaInCol;
        yourFields = yourCtrl.refFields;
        
        trIx = -1;
        for tr in yourFields:
            trIx = trIx + 1;
            for tfn in tr.names:
                #print(tfn);
                if(tfn == csvColName):
                    #print("YourCsvHeader", csvColName, csvColNbr, trIx);
                    yourViaInCol[csvColNbr] = trIx;
                    break;         
        return; 

    def importYourCsvValue(yourCtrl, csvColVal, csvColNbr):
        "Import your column value to its designated thesarus field."
        yourViaInCol = yourCtrl.refViaInCol;
        yourFields = yourCtrl.refFields;
        
        thryNbr = yourViaInCol[csvColNbr];
        yourFields[thryNbr].ievalue.set(csvColVal);
        #print("import1", csvColNbr, csvColVal, thryNbr);
        #print("import2", yourFields[thryNbr].ievalue);
        return;

    def importYourLine(yourCtrl, dataRow, rptCols):
        "Import into the thesarus this data row."
        selColIx = -1;
        for selColVal in dataRow:
            #print("Working on column ", selColVal);
            selColIx = selColIx + 1;
            #print(selRowIx, selColIx, selColVal);
            trexThesarus.importYourCsvValue(yourCtrl, selColVal, selColIx);

    def yourHdrLeftSubMidRight(yourCtrl, hdrSubAndMid):
        print("[%s/"             %yourCtrl.category, end='');
        print("%s]"              %hdrSubAndMid[0], end='');
        print("     %s     "     %hdrSubAndMid[1], end='');
        rptOpenDateRight();
        return;

    def yourRptColHdr(yourCtrl, uciList):
        "Print the headers for the desired columns."
        #print("Column headers are coming");
        for uciIx in uciList:
            thrsIx = yourCtrl.refViaUci[uciIx.value - yourCtrl.baseUci.value];
            #print("\n####", uciIx, thrsIx, );
            print(yourCtrl.refFields[thrsIx].hdrFmt %yourCtrl.refFields[thrsIx].names[0], end='');
        print();    
        return;

    # 100% flexible report generator in two parts
    # part 1 - output one formatted field
    def reportYourField(yourCtrl, uci):
        "Print one trex Data field"
        #print("\n********", uci, "##", end='');
        if(uci == anyEnv.Uci.uciEOL):
            print(end='\n');
        else:
            thrsIx = yourCtrl.refViaUci[uci.value - yourCtrl.baseUci.value];
            if(uci == anyEnv.Uci.townName):
                print('%-12s' %(yourCtrl.refFields[thrsIx].ievalue), end='');
            elif(uci == anyEnv.Uci.stateName):
                print("%-8s" %(yourCtrl.refFields[thrsIx].ievalue), end='');
            elif(uci == anyEnv.Uci.countryName):
                print("%-8s" %(yourCtrl.refFields[thrsIx].ievalue), end='');
            elif(uci == anyEnv.Uci.townLongLat):
                print("%-12s" %(yourCtrl.refFields[thrsIx].ievalue), end='');
        return;

    # part 2 - output all of the desired fields for a desired row
    # including appending a new-line.
    def reportYourFields(yourCtrl, uciLst):
        "Print all your identified trex fields in the given order"
        for uci in uciLst: trexThesarus.reportYourField(yourCtrl, uci);
        # Put the new-line.
        trexThesarus.reportYourField(yourCtrl, anyEnv.Uci.uciEOL);
        return;


    def explainYour(yourCtrl): # will revise to __str__(self):
        "Explain your thesarus in its current state."
        yourViaUci = yourCtrl.refViaUci;
        yourViaInCol = yourCtrl.refViaInCol;
        yourFields = yourCtrl.refFields;
        
        print("Begin explanation:");
        trIx = -1;
        for tr in yourFields:
            trIx = trIx + 1;
            print("thesarusColumn[", trIx, "] uci=", tr.uci, ", value=", tr.ievalue);
            for tfn in tr.names:
                print("   Synonym=", tfn);

        trIx = -1;
        for uciIx in yourViaUci:
            trIx = trIx + 1;
            print("Reverse uci[", trIx, "]=", uciIx);

        trIx = -1;
        for csvIx in yourViaInCol:
            trIx = trIx + 1;
            print("Reverse csv[", trIx, "]=", csvIx);
        print("End of explanation");
        return;

# These services are for this instance and must be
# overridden in other instances.
    def initAtStart():
        "Initialize the thesarus."
        trexGUIThesarus.initYourAtStart(trexGUIThesarus.thrsCtrl);
        return;

    def initForCsvHeader(csvColName, csvColNbr):
        "Initialize one column Ix by locating its matching synonym."
        trexThesarus.initYourForCvsHeader(csvColName, csvColNbr, thrsCtrl);
        return;
    
    def importCsvValue(csvColVal, csvColNbr):
        "Import one column value to its designated thesarus field."
        trexThesarus.importYourForCvsValue(csvColValue, csvColNbr, thrsCtrl);
        return;
    
    def doOneLine(dataRow, rptColsEnum):
        "Import one row then report it."
        trexThesarus.importYourLine(thrsCtrl, dataRow, rptColsEnum);
        trexThesarus.rptYourLine(thrsCtrl, rptColsEnum);
        return;

    
    def explain():
        "Explain this thesarus in its current state."
        trexThesarus.explainYour(thrsCtrl);
        return;




def rptFooterAll():
    print("End of report");
    return;

#END
