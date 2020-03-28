# Module - MetroData management
# Load data from any source into the thesarus then use these services:
# - report the data as desired
# - blah blah blah
#
# The thesarus list field numbers and names
uciRowId = 0;
uciTownName = 1;
uciStateName = 2;
uciCountryName = 3;
uciTownLongLat = 4;
uciEOL = 99;
# Data is loaded here from any source
MetroThesarusData = ["someKey", "Preston", "Idaho", "USA", "7522000000"];

# 100% flexible report generator in two parts
# part 1 - output a formatted field
def reportMetroField(fldNbr):
    "Print MetroData field"
    if(fldNbr == uciTownName):
        print('%12s' %(MetroThesarusData[uciTownName]), end='');
    elif(fldNbr == uciStateName):
        print("%8s" %(MetroThesarusData[uciStateName]), end='');
    elif(fldNbr == uciCountryName):
        print("%6s" %(MetroThesarusData[uciCountryName]), end='');
    elif(fldNbr == uciTownLongLat):
        print("%12s" %(MetroThesarusData[uciTownLongLat]), end='');
    elif(fldNbr == uciEOL):
        print(end='\n');
    return;
# part 2 - output all of the fields for a desired row
# including appending a uciEOL.
def reportMetroFields(fldLst):
    "Print MetroData fields in the given order"
    # I can't get this to work?
    temp = fldLst + [uciEOL];
    for x in temp: reportMetroFields(x);
    return;

# Start program execution here
print("Start with Metro thesarus data for one line loaded");

#chosenFields = [uciStateName,uciTownName];
#reportMetroFields(chosenFields);

metroReportOne = [uciTownLongLat,uciTownName,uciEOL];  
for x in metroReportOne: reportMetroField(x);

metroReportTwo = [uciTownName,uciTownLongLat,uciCountryName,uciStateName,uciEOL];
for x in metroReportTwo: reportMetroField(x);

print("End");
