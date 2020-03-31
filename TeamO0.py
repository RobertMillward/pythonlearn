"""
TeamO0.py Team version "O" level "0" api definition:

"""
import ArchEdenZ0Plan   as aep
import TeamZ0Plan       as tZ0
#import ArchTrexZ0Plan   as trex
import enum





def doOneLine(dataRow, rptCols):
    "Import into the thesarus this data row then report it."
    selColIx = -1;
    for selColVal in dataRow:
        #print("Working on column ", selColVal);
        selColIx = selColIx + 1;
        #print(selRowIx, selColIx, selColVal);
        tZ0.teamTrex.importCsvValue(selColVal, selColIx);
    tZ0.teamTrex.rptLine(rptCols);


#END
