"""
ArchTrexZ0Plan.py - Coming
"""
import ArchEdenZ0Plan as aep
import datetime
import enum

# Thesarus
# A service can use this thesarus to locate a field:
# For example by name:
# - a csv file with column headers
# - test data with column headers possiby separate
# - a sql result
# - an HTML result
# For example by uci
# - wanting data for a report
# -
#
class thrsField():
    def __init__(self, uci, names, value=''):
        self.uci = uci;
        self.names = names;
        self.ievalue = "";
        return;

class thrsCtrl():
    def __init__(self, category, baseUci, viaInCol, viaUci):
        self.category       = category;
        self.baseUci        = baseUci;
        self.refViaInCol    = viaInCol;
        self.refViaUci      = viaUci;
        return;
    
    
class trexThesarus():
    # one reverse index each per field
    thrsViaInCol = [-1,-1]; # varies by file being imported
    thrsViaUci = [-1,-1];

    thrsCtrl = thrsCtrl("TREX", aep.Uci.metroRowId, thrsViaInCol, thrsViaUci);
    # the data fields
    thrsFields = [
        thrsField(aep.Uci.metroRowId,  ["rowId"]   ),
        thrsField(aep.Uci.countryName, ["country", "nation"])]

    def initYourAtStart(yourFields, yourCtrl):
        "Initialize your thesarus."
        yourViaUci = yourCtrl.refViaUci;
        trIx = -1;
        for tr in yourFields:
            trIx = trIx + 1;
            yourViaUci[tr.uci.value - yourCtrl.baseUci.value] = trIx;
        return;
        
    def initAtStart():
        "Initialize the thesarus."
        initYourAtStart(trexThesarus.thrsFields, trexThesarus.thrsCtrl);
        return;

    def initYourForCvsHeader(csvColName, csvColNbr, yourFields, yourViaInCol):
        "Initialize your one column Ix by locating its matching synonym."
        trIx = -1;
        for tr in yourFields:
            trIx = trIx + 1;
            for tfn in tr.names:
                if(tfn == csvColName):
                    #print("csvColName", csvColName, trIx, csvColNbr);
                    yourViaInCol[csvColNbr] = trIx;
                    break;         
        return; 

    def initForCsvHeader(csvColName, csvColNbr):
        "Initialize one column Ix by locating its matching synonym."
        initYourForCvsHeader(csvColName, csvColNbr, trexThesarus.thrsFields,trexThesarus.thrsViaInCol); 
        return;

    def importYourCvsValue(csvColVal, csvColNbr, yourFields, yourViaInCol):
        "Import your column value to its designated thesarus field."
        thrsNbr = yourViaInCol[csvColNbr];
        yourFields[thrsNbr].ievalue = csvColVal;
        #print("import1", csvColNbr, csvColVal, thrsNbr);
        #print("import2", trexThesarus.thrsFields[thrsNbr].ievalue);
        return;
    
    def importCsvValue(csvColVal, csvColNbr):
        "Import one column value to its designated thesarus field."
        importYourForCvsValue(csvColValue, csvColNbr, trexThesarus.thrsFields, trexThesarus.thrsViaInCol); 
        return;

    def explainYour(yourFields, yourViaInCol, yourViaUci):
        "Explain your thesarus in its current state."
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
    
    def explain(csvColVal, csvColNbr):
        "Explain the thesarus in its current state."
        explainYour(trexThesarus.thrsFields,trexThesarus.thrsViaInCol, trexThesarus.thrsViaUci); 
        return;


def rptOpenDate():
    "Print a common look and feel date at the end of the line."
    gotIt = datetime.datetime.today();
    print("%02d" %gotIt.day, end='');
    print("/%02d" %gotIt.month, end='');
    print("/%04d" %gotIt.year, end='');
    print(" %02d" %gotIt.hour, end='');
    print(":%02d" %gotIt.minute, end='');
    print(end='\n');
    return;



def rptFooterAll():
    print("End of report");
    return;

#END
