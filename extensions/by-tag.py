#!/usr/bin/env python3
from extensioncore import *

def calculate_by_tag(configuration,timeEntries):
    timePerTag = {}
    for entry in timeEntries:
        timeSpent = entry_to_seconds_diff(entry).seconds
        for tag in entry['tags']:
            if tag in timePerTag:
                timePerTag[tag] = timePerTag[tag] + timeSpent
            else:
                timePerTag[tag] = timeSpent

    lengthLongestTag = 0
    for tag in timePerTag.keys():
        if len(tag) >= lengthLongestTag:
            lengthLongestTag = len(tag)
    timePerTag = dict(reversed(sorted(timePerTag.items(), key=lambda item: item[1])))
    for tag, timeSpent in timePerTag.items():
        timeSpentConverted = seconds_to_hms(timeSpent)
        print(f'{tag: <{lengthLongestTag}} - {timeSpentConverted[0]:03}h {timeSpentConverted[1]:02}m {timeSpentConverted[2]:02}s')

if __name__ == "__main__":
    configuration, timeEntries = parse_from_stdin()
    if len(timeEntries) > 0:
        calculate_by_tag(configuration,timeEntries)
    else:
        print_no_data_message(configuration)
