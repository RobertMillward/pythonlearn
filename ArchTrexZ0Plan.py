"""
ArchTrexZ0Plan.py - Services for importing, exporting, and formatting data.
Using this thesarus a producer or consumer can locate a common field to process.

It knows about ArchEdenZ0Plan Uci so covers much of the processing.
"""
import ArchEdenZ0Plan as aep
import datetime



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


class trexxField():
    def __init__(self, uci, names, value=''):
        self.uci = uci;
        self.names = names;
        self.ievalue = "";
        return;

class trexxCtrl():
    def __init__(self, category, fields, baseUci, viaInCol, viaUci):
        self.category       = category;
        self.refFields      = fields;
        self.baseUci        = baseUci;
        self.refViaInCol    = viaInCol;
        self.refViaUci      = viaUci;
        return;
    
# The thesarus prototype
#
class trexThesarus():
    # These variables must be overridden in any instance.
    # one reverse index of each kind per field
    thrsViaInCol = [-1,-1]; # varies by file being imported
    thrsViaUci = [-1,-1];

    # the data fields
    thrsFields = [
        trexxField(aep.Uci.metroRowId,  ["rowId"]   ),
        trexxField(aep.Uci.countryName, ["country", "nation"])]

    thrsCtrl = trexxCtrl("TREX", thrsFields, aep.Uci.metroRowId, thrsViaInCol, thrsViaUci);

# The *Your* services serve any instance.
# They do not need to be overridden.
    def initYourAtStart(yourCtrl):
        "Initialize your thesarus."
        #print("InitializingZ Your", yourCtrl.refFields[2].uci);
        yourViaUci = yourCtrl.refViaUci;
        yourFields = yourCtrl.refFields;
        
        trIx = -1;
        for tr in yourFields:
            trIx = trIx + 1;
            yourViaUci[tr.uci.value - yourCtrl.baseUci.value] = trIx;
        return;

    def initYourForCvsHeader(csvColName, csvColNbr, yourCtrl):
        "Initialize your one column Ix by locating its matching synonym."
        #print("InitializingZ YourCvs", yourCtrl.refFields[2].uci);
        #print("InitializingZ YourCvs", yourCtrl.refViaUci[2]);
        #print("InitializingZ YourCvs", yourCtrl.refViaInCol[2]);
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

    def importYourCvsValue(csvColVal, csvColNbr, yourCtrl):
        "Import your column value to its designated thesarus field."
        yourViaInCol = yourCtrl.refViaInCol;
        yourFields = yourCtrl.refFields;
        
        thryNbr = yourViaInCol[csvColNbr];
        yourFields[thryNbr].ievalue = csvColVal;
        #print("import1", csvColNbr, csvColVal, thryNbr);
        #print("import2", yourFields[thryNbr].ievalue);
        return;


    def yourHdrLeftSubMidRight(yourCtrl, hdrSubAndMid):
        print("[%s/"             %yourCtrl.category, end='');
        print("%s]"              %hdrSubAndMid[0], end='');
        print("     %s     "     %hdrSubAndMid[1], end='');
        rptOpenDateRight();
        return;

    def yourRptColHdr(yourCtrl, uciList):
        "Print the headers for the desired columns."
        print("Column headers are coming");
        for uciIx in uciList:
            print(uciIx);
        return;

    # 100% flexible report generator in two parts
    # part 1 - output one formatted field
    def reportYourField(yourCtrl, uci):
        "Print one trex Data field"
        if(uci == aep.Uci.townName):
            print('%-12s' %(yourCtrl.refFields[2].ievalue), end='');
        elif(uci == aep.Uci.stateName):
            print("%-8s" %(yourCtrl.refFields[3].ievalue), end='');
        elif(uci == aep.Uci.countryName):
            print("%-6s" %(yourCtrl.refFields[4].ievalue), end='');
        elif(uci == aep.Uci.townLongLat):
            print("%-12s" %(yourCtrl.refFields[1].ievalue), end='');
        elif(uci == aep.Uci.uciEOL):
            print(end='\n');
        return;

    # part 2 - output all of the desired fields for a desired row
    # including appending a new-line.
    def reportYourFields(yourCtrl, uciLst):
        "Print all your identified trex fields in the given order"
        for uci in uciLst: trexThesarus.reportYourField(yourCtrl, uci);
        # Put the new-line.
        trexThesarus.reportYourField(yourCtrl, aep.Uci.uciEOL);
        return;

    def explainYour(yourCtrl):
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
        initYourAtStart(trexThesarus.thrsCtrl);
        return;

    def initForCsvHeader(csvColName, csvColNbr):
        "Initialize one column Ix by locating its matching synonym."
        trexThesarus.initYourForCvsHeader(csvColName, csvColNbr, trexThesarus.thrsCtrl); 
        return;
    
    def importCsvValue(csvColVal, csvColNbr):
        "Import one column value to its designated thesarus field."
        trexThesarus.importYourForCvsValue(csvColValue, csvColNbr, trexThesarus.thrsCtrl); 
        return;
    
    def explain():
        "Explain this thesarus in its current state."
        trexThesarus.explainYour(trexThesarus.thrsCtrl); 
        return;




def rptFooterAll():
    print("End of report");
    return;

#END
