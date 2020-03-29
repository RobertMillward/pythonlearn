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

# Thesarus
# A service can use this thesarus to locate a field:
# For example by name:
# - a csv file with column headers
# - test data with column headers possiby separate
# - a sql result
# - an HTML result
# For example by uci
# - wanting data for a report
# -
#
class thesField():
    def __init__(self, uci, names, value=''):
        self.uci = uci;
        self.names = names;
        self.ievalue = "";
        return;
    

    


#END
