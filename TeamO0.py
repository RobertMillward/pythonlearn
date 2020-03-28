"""
TeamO0.py Team version "O" level "0" api definition:

"""
import ArchEdenZ0Plan   as aep
import TeamZ0Plan       as tZ0

# 100% flexible report generator in two parts
# part 1 - output one formatted field
def reportField(fldNbr):
    "Print one TeamData field"
    if(fldNbr == aep.Uci.townName):
        print('%12s' %(tZ0.teamThesarusData[1]), end='');
    elif(fldNbr == aep.Uci.stateName):
        print("%8s" %(tZ0.teamThesarusData[2]), end='');
    elif(fldNbr == aep.Uci.countryName):
        print("%6s" %(tZ0.teamThesarusData[3]), end='');
    elif(fldNbr == aep.Uci.townLongLat):
        print("%12s" %(tZ0.teamThesarusData[4]), end='');
    elif(fldNbr == aep.Uci.uciEOL):
        print(end='\n');
    return;

# part 2 - output all of the desired fields for a desired row
# including appending a uciEOL.
def reportFields(fldLst):
    "Print TeamData fields in the given order"
    for x in fldLst: reportField(x);
    reportField(aep.Uci.uciEOL);
    return;

#END
