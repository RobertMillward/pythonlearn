"""
TeamZ0Plan.py Team data definition:
"""

import ArchEdenZ0Plan as aep

category = "TEAM";


class teamThesarus():
    # one reverse index each per field
    thesViaInCol = [-1,-1,-1,-1,-1]; # varies by file being imported
    thesViaUci = [-1,-1,-1,-1,-1];
    
    thesFields = [
        aep.thesField(aep.Uci.rowId,         ["rowId"]   ),
        aep.thesField(aep.Uci.townLongLat,   ["longLat"] ),
        aep.thesField(aep.Uci.townName,      ["town", "city"]),
        aep.thesField(aep.Uci.stateName,     ["state", "province"]),
        aep.thesField(aep.Uci.countryName,   ["country", "nation"])]
    
    def explain():
        print("Begin explanation:");
        trIx = -1;
        for tr in teamThesarus.thesFields:
            trIx = trIx + 1;
            print("thesarusColumn[", trIx, "] uci=", tr.uci, ", value=", tr.ievalue);
            for tfn in tr.names:
                print("   Synonym=", tfn);

        trIx = -1;
        for uciIx in teamThesarus.thesViaUci:
            trIx = trIx + 1;
            print("Reverse uci[", trIx, "]=", uciIx);

        trIx = -1;
        for csvIx in teamThesarus.thesViaInCol:
            trIx = trIx + 1;
            print("Reverse csv[", trIx, "]=", csvIx);
        print("End of explanation");
        return;

    
    def initAtStart():
        trIx = -1;
        for tr in teamThesarus.thesFields:
            trIx = trIx + 1;
            teamThesarus.thesViaUci[tr.uci.value - aep.Uci.rowId.value] = trIx;
        return;
    
    def initForCsvHeader(csvColName, csvColNbr):
        trIx = -1;
        for tr in teamThesarus.thesFields:
            trIx = trIx + 1;
            #teamThesarus.thesViaInCol[csvColNbr] = -1; in caller
            for tfn in tr.names:
                if(tfn == csvColName):
                    teamThesarus.thesViaInCol[csvColNbr] = trIx;
                    break;        
        return;

    def importCsvValue(csvColVal, csvColNbr):
        thsNbr = teamThesarus.thesViaInCol[csvColNbr];
        teamThesarus.thesFields[thsNbr].ievalue = csvColVal;
        return


# Data is loaded here from any source (until we get the above working)
teamThesarusData = ["someKey", "Preston", "Idaho", "USA", "7522000000"];

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
