"""
TeamZ0Plan.py Team data definition:
"""
import ArchEdenZ0Plan as aep
import ArchTrexZ0Plan as trex
import enum

# Data plan for reports
class TeamRptsEnum(enum.Enum):
    townLongLatCntryState = 1;
    longLatTown = 2;

# Full width report title and columns
hdrTllCSlist = ["TllCS", "Full Team information"]; 

rptTllCSlist = [aep.Uci.townName,    \
                aep.Uci.townLongLat, \
                aep.Uci.countryName, \
                aep.Uci.stateName];

# Narrow report title and columns
hdrLlTlist = ["llT", "Tiny info"];

rptLlTlist = [  aep.Uci.townLongLat,   \
                aep.Uci.townName];

# The central control.
#
class teamTrex(trex.trexThesarus):
    
    thrsViaInCol = [-1,-1,-1,-1,-1]; # varies by file being imported
    thrsViaUci = [-1,-1,-1,-1,-1];

    
    thrsFields = [
        trex.trexxField(aep.Uci.metroRowId,  ["rowId"]   ),
        trex.trexxField(aep.Uci.townLongLat, ["longLat"] ),
        trex.trexxField(aep.Uci.townName,    ["town", "city"]),
        trex.trexxField(aep.Uci.stateName,   ["state", "province"]),
        trex.trexxField(aep.Uci.countryName, ["country", "nation"])];

    
    thrsCtrl = trex.trexxCtrl("TEAM", thrsFields, aep.Uci.metroRowId, thrsViaInCol, thrsViaUci);

    def initAtStart():
        "Initialize this thesarus using tools in the master."
        teamTrex.initYourAtStart(teamTrex.thrsCtrl);
        return;

    def initForCsvHeader(csvColName, csvColNbr):
        "Initialize one column Ix by locating its matching synonym."
        #print("Initializing2 teamTrex", teamTrex.thrsCtrl.refFields[2].uci);
        #print("Initializing3 teamTrex", teamTrex.thrsCtrl.refViaUci[2])
        teamTrex.initYourForCvsHeader(teamTrex.thrsCtrl, csvColName, csvColNbr); 
        return;

    def importCsvValue(csvColVal, csvColNbr):
        "Import one column value to its designated thesarus field."
        teamTrex.importYourCsvValue(teamTrex.thrsCtrl, csvColVal, csvColNbr); 
        return;

    def rptRptHdr(teamRptEnum):
        if(teamRptEnum == TeamRptsEnum.townLongLatCntryState):
            teamTrex.yourHdrLeftSubMidRight(teamTrex.thrsCtrl, hdrTllCSlist);
            teamTrex.yourRptColHdr(teamTrex.thrsCtrl, rptTllCSlist);
        elif(teamRptEnum == TeamRptsEnum.longLatTown):
            teamTrex.yourHdrLeftSubMidRight(teamTrex.thrsCtrl, hdrLlTlist);
            teamTrex.yourRptColHdr(teamTrex.thrsCtrl, rptLlTlist);
        return;
    
    def rptLine(teamRptEnum):
        "Based on the report enum given print a row."
        if(teamRptEnum == TeamRptsEnum.townLongLatCntryState):
            teamTrex.reportYourFields(teamTrex.thrsCtrl, rptTllCSlist);
        elif(teamRptEnum == TeamRptsEnum.longLatTown):
            teamTrex.reportYourFields(teamTrex.thrsCtrl, rptLlTlist);
        return
    
    def doOneLine(dataRow, rptColsEnum):
        "Import one row then report it."
        teamTrex.importYourLine(teamTrex.thrsCtrl, dataRow, rptColsEnum);
        teamTrex.rptLine(rptColsEnum);
        return;
    
    def doOneReport(dataRows, rptColsEnum):
        "Import and report one data set."
        teamTrex.rptRptHdr(rptColsEnum);
        selRowIx = -1;
        for dataRow in dataRows:
            #print("Working on row ", dataRow);
            selRowIx = selRowIx + 1;
            if(selRowIx > 0): # skip header
                teamTrex.doOneLine(dataRow, rptColsEnum);
        trex.rptFooterAll();
        return;

    def explain():
        "Explain the thesarus in its current state."
        trex.trexThesarus.explainYour(teamTrex.thrsCtrl); 
        return;
        





#END
