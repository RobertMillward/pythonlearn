"""
TeamZ0Plan.py Team data definition:
"""
import ArchEdenZ0Plan as aep
import ArchTrexZ0Plan as trex
import enum

class teamTrex(trex.trexThesarus):
    
    thrsViaInCol = [-1,-1,-1,-1,-1]; # varies by file being imported
    thrsViaUci = [-1,-1,-1,-1,-1];

    thrsCtrl = trex.thrsCtrl("TEAM", aep.Uci.metroRowId, thrsViaInCol, thrsViaUci);
    
    thrsFields = [
        trex.thrsField(aep.Uci.metroRowId,  ["rowId"]   ),
        trex.thrsField(aep.Uci.townLongLat, ["longLat"] ),
        trex.thrsField(aep.Uci.townName,    ["town", "city"]),
        trex.thrsField(aep.Uci.stateName,   ["state", "province"]),
        trex.thrsField(aep.Uci.countryName, ["country", "nation"])]

    def initAtStart():
        "Initialize this thesarus using tools in the master."
        trex.trexThesarus.initYourAtStart(teamTrex.thrsFields, teamTrex.thrsCtrl);
        #trex.trexThesarus.initYourAtStart(teamTrex.thrsFields, teamTrex.thrsViaUci)'
        return;

    def initForCvsHeader(csvColName, csvColNbr):
        "Initialize one column Ix by locating its matching synonym."
        initYourForCvsHeader(csvColName, csvColNbr, teamTrex.thrsFields,teamTrex.thrsViaInCol); 
        return;

    def importCsvValue(csvColVal, csvColNbr):
        "Import one column value to its designated thesarus field."
        importYourForCvsValue(csvColValue, csvColNbr, teamTrex.thrsFields, teamTrex.thrsViaInCol); 
        return;

    def explain(csvColVal, csvColNbr):
        "Explain the thesarus in its current state."
        explainYour(teamTrex.thrsFields, teamTrex.thrsViaInCol, teamTrex.thrsViaUci); 
        return;
        


class teamThesarus():
    # one reverse index each per field
    thrsViaInCol = [-1,-1,-1,-1,-1]; # varies by file being imported
    thrsViaUci = [-1,-1,-1,-1,-1];
    
    thrsFields = [
        trex.thrsField(aep.Uci.metroRowId,  ["rowId"]   ),
        trex.thrsField(aep.Uci.townLongLat, ["longLat"] ),
        trex.thrsField(aep.Uci.townName,    ["town", "city"]),
        trex.thrsField(aep.Uci.stateName,   ["state", "province"]),
        trex.thrsField(aep.Uci.countryName, ["country", "nation"])]
    
    def explain():
        "Explain the thesarus in its current state."
        print("Begin explanation:");
        trIx = -1;
        for tr in teamThesarus.thrsFields:
            trIx = trIx + 1;
            print("thesarusColumn[", trIx, "] uci=", tr.uci, ", value=", tr.ievalue);
            for tfn in tr.names:
                print("   Synonym=", tfn);

        trIx = -1;
        for uciIx in teamThesarus.thrsViaUci:
            trIx = trIx + 1;
            print("Reverse uci[", trIx, "]=", uciIx);

        trIx = -1;
        for csvIx in teamThesarus.thrsViaInCol:
            trIx = trIx + 1;
            print("Reverse csv[", trIx, "]=", csvIx);
        print("End of explanation");
        return;

    
    def initAtStart():
        "Initialize the thesarus."
        trIx = -1;
        for tr in teamThesarus.thrsFields:
            trIx = trIx + 1;
            teamThesarus.thrsViaUci[tr.uci.value - aep.Uci.metroRowId.value] = trIx;
        return;
    
    def initForCsvHeader(csvColName, csvColNbr):
        "Initialize one column Ix by locating its matching synonym."
        trIx = -1;
        for tr in teamThesarus.thrsFields:
            trIx = trIx + 1;
            for tfn in tr.names:
                if(tfn == csvColName):
                    #print("csvColName", csvColName, trIx, csvColNbr);
                    teamThesarus.thrsViaInCol[csvColNbr] = trIx;
                    break;        
        return;

    def importCsvValue(csvColVal, csvColNbr):
        "Import one column value to its designated thesarus field."
        thrsNbr = teamThesarus.thrsViaInCol[csvColNbr];
        teamThesarus.thrsFields[thrsNbr].ievalue = csvColVal;
        #print("import1", csvColNbr, csvColVal, thrsNbr);
        #print("import2", teamThesarus.thrsFields[thrsNbr].ievalue);
        return




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
