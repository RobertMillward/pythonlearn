"""
TeamZ0Plan.py Team data definition:
"""
import ArchEdenZ0Plan as aep

category = "TEAM";


class teamThesarus():
    # one reverse index each per field
    thrsViaInCol = [-1,-1,-1,-1,-1]; # varies by file being imported
    thrsViaUci = [-1,-1,-1,-1,-1];
    
    thrsFields = [
        aep.thrsField(aep.Uci.rowId,         ["rowId"]   ),
        aep.thrsField(aep.Uci.townLongLat,   ["longLat"] ),
        aep.thrsField(aep.Uci.townName,      ["town", "city"]),
        aep.thrsField(aep.Uci.stateName,     ["state", "province"]),
        aep.thrsField(aep.Uci.countryName,   ["country", "nation"])]
    
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
            teamThesarus.thrsViaUci[tr.uci.value - aep.Uci.rowId.value] = trIx;
        return;
    
    def initForCsvHeader(csvColName, csvColNbr):
        "Initialize one column Ix by locating its matching synonym."
        trIx = -1;
        for tr in teamThesarus.thrsFields:
            trIx = trIx + 1;
            for tfn in tr.names:
                if(tfn == csvColName):
                    teamThesarus.thrsViaInCol[csvColNbr] = trIx;
                    break;        
        return;

    def importCsvValue(csvColVal, csvColNbr):
        "Import one column value to its designated thesarus field."
        thrsNbr = teamThesarus.thrsViaInCol[csvColNbr];
        teamThesarus.thrsFields[thrsNbr].ievalue = csvColVal;
        #print("inIt1", csvColNbr, csvColVal, thrsNbr);
        #print("inIt2", teamThesarus.thrsFields[thrsNbr].ievalue);
        return


        
# Data is loaded here from any source (until we get the above working)
#teamThesarusData = ["someKey", "Preston", "Idaho", "USA", "7522000000"];

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
