#!/usr/bin/env python3
import fileinput
import json
import datetime

SECONDS_TO_HOURS = 60 * 60

def parse_from_stdin():
    frontMatterParsing = True
    frontMatterData = ""
    jsonData = ""
    for line in fileinput.input():
        parseLine = line.rstrip()
        #print(parseLine)
        if parseLine == "":
            frontMatterParsing = False 
        if frontMatterParsing:
            frontMatterData = frontMatterData + parseLine
        else:
            jsonData = jsonData + parseLine
    timeEntries = json.loads(jsonData)
    return frontMatterData, timeEntries

def seconds_to_hms(seconds):
    h = int(seconds / SECONDS_TO_HOURS)
    m = int(seconds / 60 - h * 60)
    s = int(seconds - h * SECONDS_TO_HOURS - m * 60)
    return h, m, s

def entry_to_seconds_diff(entry):
    startDate = datetime.datetime.fromisoformat(entry['start'])
    endDate = datetime.datetime.fromisoformat(entry['end'])
    spentTime = endDate - startDate
    return spentTime

if __name__ == "__main__":
    print(parse_from_stdin())
