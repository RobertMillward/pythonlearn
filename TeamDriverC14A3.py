"""
TeamDriverC14A3.py - Demo Application TeamC14 level 3.
Load data from any source into the thesarus then use these services:
- report the data using a stock or custom field list.
- blah blah blah

"""
import ArchEdenZ0Plan   as aep # the Application definitions
import TeamZ0Plan       as tZ0 # the Team Data Plan
import TeamO0           as tO0 # the Team version 'O', level '0' api

# As though a query had been run for all towns named Preston
demoDataWhereTown = ["town",
                     "Preston"];
demoDataSelected = [
    ["longLat", "province", "nation"],
    ["7500000", "Idaho",    "USA"   ],
    ["6400000", "Iowa",     "USA"   ],
    ["5800000", "Maine",    "USA"   ],
    ["0500000", "England",  "UK"   ]]
    

whrRowIx = 0;
whrColIx = 0;
selRowIx = 0;
selColIx = 0;

def startImport():
    whrRowIx = 0;
    whrColIx = 0;
    tZ0.teamThesarus.initForCsvHeader(demoDataWhereTown[whrRowIx][whrRowIx], whrColIx);
    whrRowIx = whrRowIx + 1;
    tZ0.teamThesarus.importCsvValue(demoDataWhereTown[whrRowIx][whrRowIx], whrColIx);
    selRowIx = 0;
    selColIx = -1;
    for selColNm in demoDataSelected[selRowIx]:
        selColIx = selColIx + 1;
        tZ0.teamThesarus.initForCsvHeader(selColNm, selColIx);
    
    tZ0.teamThesarus.explain();
    return;

# demonstrate that any report can be run from the team thesarus.
# (imagine that this is Team data)
def doReport(rptCols):
    startImport();
    tO0.rptRptHdr(rptCols);
    for dataRow in demoDataSelected:
        selRowIx = selRowIx + 1;
        selColIx = -1;
        for selColVal in demoDataSelected[selRowIx]:
            selColIx = selColIx + 1;
            tZ0.teamThesarus.importCsvValue(selColVal, selColIx);
            tO0.rptLine(rptCols);
    
        tO0.rptFooterAll();
        return

# Start program execution here
print("Start demo of Team thesarus data.");

tZ0.teamThesarus.initAtStart();

# this is a report of longitude/latitude and town.
doReport(tO0.TeamRpts.longLatTown);

# this is a report of town, longitude/latitude, country, and state.
doReport(tO0.TeamRpts.townLongLatCntryState);

print("End");
