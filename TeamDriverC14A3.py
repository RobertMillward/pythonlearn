"""
TeamDriverC14A3.py - Application TeamC14 level 3.
Load data from any source into the thesarus then use these services:
- report the data using a stock or custom field list.
- blah blah blah

"""
import ArchEdenZ0Plan   as aep
import TeamZ0Plan       as tZ0
import TeamO0           as tO0



# Start program execution here
print("Start with Team thesarus data for one line pre loaded");
 
# demonstrate that any report can be run from the appropriate data.
# (imagine that this is Team data)
# this is a report of longitude/latitude and town.
tO0.rptRptHdr(tO0.TeamRpts.longLatTown);
tO0.rptLine(tO0.TeamRpts.longLatTown);
tO0.rptFooterAll();
# this is a report of town, longitude/latitude, country, and state.
tO0.rptRptHdr(tO0.TeamRpts.townLongLatCntryState);
tO0.rptLine(tO0.TeamRpts.townLongLatCntryState);
tO0.rptFooterAll();

print("End");
