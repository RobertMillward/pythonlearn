"""
TeamZ0Plan.py Team data definition:
"""

import ArchEdenZ0Plan as aep

# Data is loaded here from any source
teamThesarusData = ["someKey", "Preston", "Idaho", "USA", "7522000000"];
# A service can use this thesarus to see which fields go where by name
# For example a csv file with column headers.
teamThesarus = [["key", "id"], \
                ["town", "city"], \
                ["state", "province"], \
                ["country", "nation"], \
                ["longLat"]];
# A service can use this thesarus to see which fields 

rptTllCSlist = [aep.Uci.townName,    \
                aep.Uci.townLongLat, \
                aep.Uci.countryName, \
                aep.Uci.stateName];

rptLlTlist = [  aep.Uci.townLongLat,   \
                aep.Uci.townName];

#END
