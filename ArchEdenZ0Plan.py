"""
ArchEdenZ0Plan.py - Eden Architecture Data Plan,
    version Z (base for all versions),
    level '0' (basic service support)

"""
import enum

# The Eden thesarus list of field numbers and symbolic names
# (for now, imagine that these are Team fields for Eden
class Uci(enum.Enum):
    rowId = 0;
    townName = 1;
    stateName = 2;
    countryName = 3;
    townLongLat = 4;
    uciEOL = 99;

# A service can use this thesarus to see which fields go where by name
# For example:
# - a csv file with column headers
# - test data with column headers possiby separate
# - a sql result
# - an HTML result
# A service can use this thesarus to see which fields go to whicj uci
class thesarus():
    # allows for up to six fields
    thesViaInCol = [0,0,0,0,0,0]; # varies by file being imported
    thesViaUci = [0,0,0,0,0,0];
    
    def __init__(self, uci, names, value=''):
        self.uci = uci;
        self.names = names;
        self.value = "";
        return;

    def initThesarus(myThes):
        for tr in myThes: print("thesarusRow uci=", tr.uci);
        return;
    
    def initForCsvField(thesarus, csvColName, csvColNbr):
        return;
#END
