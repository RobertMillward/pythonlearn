"""
GenResearchGUIZ0Plan

The GUI interface to the Genealogy Research project.
"""
#from TrexGUIZ0Plan import *
import TrexGUIZ0Plan as trex;
import ArchEdenZ0Plan as anyEnv;

class GenResearchGUI(trex.TrexGUIThesarus):
    # the reverse indices
    thrsViaInCol =  [-1, -1, -1, -1, -1];
    thrsViaUci =    [-1, -1, -1, -1, -1];

    thrsFields = [
        trex.trexguiField(anyEnv.Uci.metroRowId,  "%-8s", ["rowId"]   ),
        trex.trexguiField(anyEnv.Uci.countryName, "%-8s", ["country", "nation"]),
        trex.trexguiField(anyEnv.Uci.stateName,   "%-8s", ["state", "province"]   ),
        trex.trexguiField(anyEnv.Uci.townName,    "%-8s", ["town", "city"]),
        trex.trexguiField(anyEnv.Uci.townLongLat, "%-8s", ["longLat"])
        ];
        
    thrsCtrl = trex.trexxCtrl("GenRsrch", thrsFields, anyEnv.Uci.metroRowId, thrsViaInCol, thrsViaUci);

    def initAtStart():
        "Initialize the thesarus."
        GenResearchGUI.initYourAtStart(GenResearchGUI.thrsCtrl);
        return;

    def initForCsvHeader(csvColName, csvColNbr):
        "Initialize one column Ix by locating its matching synonym."
        GenResearchGUI.initYourForCvsHeader(csvColName, csvColNbr, trexThesarus.thrsCtrl);
        return;
    
    def importCsvValue(csvColVal, csvColNbr):
        "Import one column value to its designated thesarus field."
        GenResearchGUI.importYourForCvsValue(csvColValue, csvColNbr, trexThesarus.thrsCtrl);
        return;
    
    def doOneLine(dataRow, rptColsEnum):
        "Import one row then report it."
        GenResearchGUI.importYourLine(thrsCtrl, dataRow, rptColsEnum);
        rptYourLine(thrsCtrl, rptColsEnum);
        return;

    
    def explain():
        "Explain this thesarus in its current state."
        GenResearchGUI.explainYour(trexThesarus.thrsCtrl);
        return;

#END
