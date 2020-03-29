"""
TeamO0.py Team version "O" level "0" api definition:

"""
import ArchEdenZ0Plan   as aep
import TeamZ0Plan       as tZ0
import datetime
import enum

class TeamRpts(enum.Enum):
    townLongLatCntryState = 1;
    longLatTown = 2;
    
def rptOpenDate():
    gotIt = datetime.datetime.today();
    print("%02d" %gotIt.day, end='');
    print("/%02d" %gotIt.month, end='');
    print("/%04d" %gotIt.year, end='');
    print(" %02d" %gotIt.hour, end='');
    print(":%02d" %gotIt.minute, end='');
    print(end='\n');
    return;

def rptHdrTownLongLatCntryState():
    print("[%s/"             %tZ0.category, end='');
    print("%s]"              %tZ0.hdrTllCSlist[0], end='');
    print("     %s     "    %tZ0.hdrTllCSlist[1], end='');
    rptOpenDate();
    return;

def rptHdrLongLatTown():
    print("[%s/"         %tZ0.category, end='');
    print("%s]"         %tZ0.hdrLlTlist[0], end='');
    print("   %s   "    %tZ0.hdrLlTlist[1], end='');
    rptOpenDate();
    return;

def rptColHdr(teamEnum):
    print("Column headers are coming");
    return;

def rptRptHdr(teamEnum):
    if(teamEnum == TeamRpts.townLongLatCntryState):
        rptHdrTownLongLatCntryState();
    elif(teamEnum == TeamRpts.longLatTown):
        rptHdrLongLatTown();
    rptColHdr(teamEnum)
    return;



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


def rptLine(teamEnum):
    if(teamEnum == TeamRpts.townLongLatCntryState):
        reportFields(tZ0.rptTllCSlist);
    elif(teamEnum == TeamRpts.longLatTown):
        reportFields(tZ0.rptLlTlist);
    return

def rptFooterAll():
    print("End of report");
    return;


#END
