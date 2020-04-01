"""
TeamDriverC14A3.py - Demo Application TeamC14 level 3.
Load data from any source into the thesarus then use these services:
- report the data using a stock or custom field list.
- blah blah blah

Copyright (c) 2020, Robert Russell Millward, all rights reserved.

"""
import ArchEdenZ0Plan   as aep # the Application definitions
import TeamZ0Plan       as tZ0 # the Team Data Plan
import TeamO0           as tO0 # the Team version 'O', level '0' api

# As though a query had been run for all towns named Preston
demoDataWhereTown = [["town"],
                     ["Preston"]];
demoDataSelected = [
    ["longLat", "province", "nation"],
    ["7500000", "Idaho",    "USA"   ],
    ["6400000", "Iowa",     "USA"   ],
    ["5800000", "Maine",    "USA"   ],
    ["0500000", "England",  "UK"   ]]
    


def startDemoJoinInitA3():
    "Set up the columns and load the where clause data."
    selRowIx = 0;
    selColIx = -1;
    for selColNm in demoDataSelected[selRowIx]:
        selColIx = selColIx + 1;
        tZ0.teamTrex.initForCsvHeader(selColNm, selColIx);
        
    whrRowIx = 0;
    whrColIx = 0;
    selColIx = selColIx + 1;
    tZ0.teamTrex.initForCsvHeader(demoDataWhereTown[whrRowIx][whrColIx], selColIx);
    # The where city = 'Preston' clause data (which is not in the selected data).
    whrRowIx = whrRowIx + 1;
    tZ0.teamTrex.importCsvValue(demoDataWhereTown[whrRowIx][whrColIx], selColIx);

    
    #tZ0.teamTrex.explain();
    return;

# demonstrate that any report can be run from the team thesarus.
# (imagine that this is Team data)
def doDemoReportA3(rptColsEnum):
    "Run the desired report per rptCols."
    
    startDemoJoinInitA3();
    tZ0.teamTrex.doOneReport(demoDataSelected, rptColsEnum, 0); 

    return

# Start program execution here
print("Start demo of Team thesarus data.");

tZ0.teamTrex.initAtStart();

# this is a report of longitude/latitude and town
# using demo data in a list.
doDemoReportA3(tZ0.TeamRptsEnum.longLatTown);

# this is a report of town, longitude/latitude, country, and state
# using the same demo data.
doDemoReportA3(tZ0.TeamRptsEnum.townLongLatCntryState);

print("End Demo");
