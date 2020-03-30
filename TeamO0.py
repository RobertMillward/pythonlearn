"""
TeamO0.py Team version "O" level "0" api definition:

"""
import ArchEdenZ0Plan   as aep
import ArchTrexZ0Plan   as trex
import TeamZ0Plan       as tZ0
import enum

class TeamRpts(enum.Enum):
    townLongLatCntryState = 1;
    longLatTown = 2;
    


def rptHdrTownLongLatCntryState():
    print("[%s/"             %tZ0.teamTrex.thrsCtrl.category, end='');
    print("%s]"              %tZ0.hdrTllCSlist[0], end='');
    print("     %s     "     %tZ0.hdrTllCSlist[1], end='');
    trex.rptOpenDate();
    return;

def rptHdrLongLatTown():
    print("[%s/"        %tZ0.teamTrex.thrsCtrl.category, end='');
    print("%s]"         %tZ0.hdrLlTlist[0], end='');
    print("   %s   "    %tZ0.hdrLlTlist[1], end='');
    trex.rptOpenDate();
    return;

def rptColHdr():
    print("Column headers are coming");
    return;

def rptRptHdr(teamEnum):
    if(teamEnum == TeamRpts.townLongLatCntryState):
        rptHdrTownLongLatCntryState();
    elif(teamEnum == TeamRpts.longLatTown):
        rptHdrLongLatTown();
    rptColHdr()
    return;



# 100% flexible report generator in two parts
# part 1 - output one formatted field
def reportField(uci):
    "Print one teamThesarus Data field"
    if(uci == aep.Uci.townName):
        print('%-12s' %(tZ0.teamThesarus.thrsFields[2].ievalue), end='');
    elif(uci == aep.Uci.stateName):
        print("%-8s" %(tZ0.teamThesarus.thrsFields[3].ievalue), end='');
    elif(uci == aep.Uci.countryName):
        print("%-6s" %(tZ0.teamThesarus.thrsFields[4].ievalue), end='');
    elif(uci == aep.Uci.townLongLat):
        print("%-12s" %(tZ0.teamThesarus.thrsFields[1].ievalue), end='');
    elif(uci == aep.Uci.uciEOL):
        print(end='\n');
    return;

# part 2 - output all of the desired fields for a desired row
# including appending a uciEOL.
def reportFields(uciLst):
    "Print all identified TeamData fields in the given order"
    for uci in uciLst: reportField(uci);
    # Put the new-line.
    reportField(aep.Uci.uciEOL);
    return;


def rptLine(teamEnum):
    "Based on the report enum given print a row."
    if(teamEnum == TeamRpts.townLongLatCntryState):
        reportFields(tZ0.rptTllCSlist);
    elif(teamEnum == TeamRpts.longLatTown):
        reportFields(tZ0.rptLlTlist);
    return


def doOneLine(dataRow, rptCols):
    "Import into the thesarus this data row then report it."
    selColIx = -1;
    for selColVal in dataRow:
        #print("Working on column ", selColVal);
        selColIx = selColIx + 1;
        #print(selRowIx, selColIx, selColVal);
        tZ0.teamThesarus.importCsvValue(selColVal, selColIx);
    rptLine(rptCols);


#END
