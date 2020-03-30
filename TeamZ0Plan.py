"""
TeamZ0Plan.py Team data definition:
"""
import ArchEdenZ0Plan as aep
import ArchTrexZ0Plan as trex
import enum

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
        trex.trexThesarus.initYourAtStart(teamTrex.thrsCtrl);
        return;

    def initForCsvHeader(csvColName, csvColNbr):
        "Initialize one column Ix by locating its matching synonym."
        #print("Initializing2 teamTrex", teamTrex.thrsCtrl.refFields[2].uci);
        #print("Initializing3 teamTrex", teamTrex.thrsCtrl.refViaUci[2])
        trex.trexThesarus.initYourForCvsHeader(csvColName, csvColNbr, teamTrex.thrsCtrl); 
        return;

    def importCsvValue(csvColVal, csvColNbr):
        "Import one column value to its designated thesarus field."
        trex.trexThesarus.importYourCvsValue(csvColVal, csvColNbr, teamTrex.thrsCtrl); 
        return;

    def explain():
        "Explain the thesarus in its current state."
        trex.trexThesarus.explainYour(teamTrex.thrsCtrl); 
        return;
        



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

#END
