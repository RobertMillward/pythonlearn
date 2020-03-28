# Module - MetroData management
# Load data from any source into the thesarus then use these services:
# - report the data as desired
# - blah blah blah
#
import ArchEdenZ0Plan as aep




# Start program execution here
print("Start with Metro thesarus data for one line pre loaded");
 
for x in aep.metroReportLlTlist: aep.reportMetroField(x);

for x in aep.metroReportTllCSlist: aep.reportMetroField(x);

print("End");
