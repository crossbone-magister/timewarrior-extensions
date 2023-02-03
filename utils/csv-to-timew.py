import sys
import csv
import os

if len(sys.argv) < 2:
    raise ValueError('No file name specified')

fileToImport = sys.argv[1]
fileToImportName = os.path.basename(fileToImport)
trackingDate = os.path.splitext(fileToImportName)[0]
print(f'Importing {fileToImport}')

with open(fileToImport, newline='') as csvFile:
    timeTrackReader = csv.reader(csvFile)
    for timeTrack in timeTrackReader:
        command = f'timew track {trackingDate}T{timeTrack[0]} - {trackingDate}T{timeTrack[1]} {timeTrack[2]}'
        os.system(command)
