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
    


def startDemoImportA3():
    "Set up the columns and load the where clause data."
    selRowIx = 0;
    selColIx = -1;
    for selColNm in demoDataSelected[selRowIx]:
        selColIx = selColIx + 1;
        tZ0.teamThesarus.initForCsvHeader(selColNm, selColIx);
        
    whrRowIx = 0;
    whrColIx = 0;
    selColIx = selColIx + 1;
    tZ0.teamThesarus.initForCsvHeader(demoDataWhereTown[whrRowIx][whrColIx], selColIx);
    whrRowIx = whrRowIx + 1;
    tZ0.teamThesarus.importCsvValue(demoDataWhereTown[whrRowIx][whrColIx], selColIx);

    
    #tZ0.teamThesarus.explain();
    return;

# demonstrate that any report can be run from the team thesarus.
# (imagine that this is Team data)
def doDemoReportA3(rptCols):
    startDemoImportA3();
    
    tO0.rptRptHdr(rptCols);

    selRowIx = -1;
    for dataRow in demoDataSelected:
        #print("Working on row ", dataRow);
        selRowIx = selRowIx + 1;
        if(selRowIx > 0): # skip header
            tO0.doOneLine(dataRow, rptCols);
            
    tO0.rptFooterAll();
    return

# Start program execution here
print("Start demo of Team thesarus data.");

tZ0.teamThesarus.initAtStart();

# this is a report of longitude/latitude and town
# using demo data in a list.
doDemoReportA3(tO0.TeamRpts.longLatTown);

# this is a report of town, longitude/latitude, country, and state
# using the same demo data.
doDemoReportA3(tO0.TeamRpts.townLongLatCntryState);

print("End");
