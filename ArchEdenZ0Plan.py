"""
Architecture Plan file for version Z (base for all),
level '0' (basics)

"""
import enum
print("ArchEden");
# The thesarus list field numbers and names
class Uci(enum.Enum):
    rowId = 0;
    townName = 1;
    stateName = 2;
    countryName = 3;
    townLongLat = 4;
    uciEOL = 99;

# Data is loaded here from any source
MetroThesarusData = ["someKey", "Preston", "Idaho", "USA", "7522000000"];

# 100% flexible report generator in two parts
# part 1 - output one formatted field
def reportMetroField(fldNbr):
    "Print MetroData field"
    if(fldNbr == Uci.townName):
        print('%12s' %(MetroThesarusData[1]), end='');
    elif(fldNbr == Uci.stateName):
        print("%8s" %(MetroThesarusData[2]), end='');
    elif(fldNbr == Uci.countryName):
        print("%6s" %(MetroThesarusData[3]), end='');
    elif(fldNbr == Uci.townLongLat):
        print("%12s" %(MetroThesarusData[4]), end='');
    elif(fldNbr == Uci.uciEOL):
        print(end='\n');
    return;
# part 2 - output all of the fields for a desired row
# including appending a uciEOL.
def reportMetroFields(fldLst):
    "Print MetroData fields in the given order"
    # I can't get this to work?
    temp = fldLst + [uciEOL];
    for x in temp: reportMetroField(x);
    return;

metroReportTllCSlist = [Uci.townName,Uci.townLongLat,Uci.countryName,Uci.stateName,Uci.uciEOL];
metroReportLlTlist = [Uci.townLongLat,Uci.townName,Uci.uciEOL];


#END
