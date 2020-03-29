"""
TeamZ0Plan.py Team data definition:
"""

import ArchEdenZ0Plan as aep

category = "TEAM";


teamThesarus = [aep.thesarus(aep.Uci.rowId,         ["rowId"]   ),
                aep.thesarus(aep.Uci.townName,      ["town", "city"]),
                aep.thesarus(aep.Uci.stateName,     ["state", "province"]),
                aep.thesarus(aep.Uci.countryName,   ["country", "nation"]),
                aep.thesarus(aep.Uci.townLongLat,   ["longLat"] )];


# Data is loaded here from any source (until we get the above working)
teamThesarusData = ["someKey", "Preston", "Idaho", "USA", "7522000000"];

# Full width report title and columns
hdrTllCSlist = ["TllCS", "Full Team information"]; 

rptTllCSlist = [aep.Uci.townName,    \
                aep.Uci.townLongLat, \
                aep.Uci.countryName, \
                aep.Uci.stateName];

# Narrow report title and columns
hdrLlTlist = ["llT", "TT info"];

rptLlTlist = [  aep.Uci.townLongLat,   \
                aep.Uci.townName];

#END
