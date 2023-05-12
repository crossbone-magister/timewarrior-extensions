#!/usr/bin/env python3
import fileinput
import json
import datetime

SECONDS_TO_HOURS = 60 * 60

def parse_from_stdin():
    configurationParsing = True
    configurationData = {}
    jsonData = ""
    for line in fileinput.input():
        parseLine = line.rstrip()
        if parseLine == "":
            configurationParsing = False
        if configurationParsing:
            configurationPair = parseLine.split(':')
            configurationData[configurationPair[0]] = configurationPair[1].strip()
        else:
            jsonData = jsonData + parseLine
    timeEntries = json.loads(jsonData)
    return configurationData, timeEntries

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

def print_no_data_message(configuration):
    start = datetime.datetime.fromisoformat(configuration['temp.report.start']).astimezone()
    end = datetime.datetime.fromisoformat(configuration['temp.report.end']).astimezone()
    #TODO: print with correct format
    print(f'No filtered data found in the range {start} - {end}')
