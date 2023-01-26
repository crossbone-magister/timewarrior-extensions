#!/usr/bin/env python3
from extensioncore import *
import datetime

PRINCIPAL_TAG='principale'

if __name__ == "__main__":
    _, timeEntries = parse_from_stdin()
    timePerDay = {}
    timePerPrincipal = {}
    for entry in timeEntries:
        startDate = datetime.datetime.fromisoformat(entry['start'])
        endDate = datetime.datetime.fromisoformat(entry['end'])
        spentTime = endDate - startDate
        dateKey = str(startDate)[:10]
        if dateKey in timePerDay:
            timePerDay[dateKey] = timePerDay[dateKey] + spentTime.seconds
        else:
            timePerDay[dateKey] = spentTime.seconds
        if PRINCIPAL_TAG in entry['tags']:
            if dateKey in timePerPrincipal:
                timePerPrincipal[dateKey] = timePerPrincipal[dateKey] + spentTime.seconds
            else:
                timePerPrincipal[dateKey] = spentTime.seconds
    for date in timePerDay.keys():
        totalTime = timePerDay[date]
        principalTime = timePerPrincipal[date]
        principalPercent = (principalTime / totalTime) * 100
        totalTimeConverted = seconds_to_hms(totalTime)
        principalTimeConverted = seconds_to_hms(principalTime)
        print(f'{date} - {PRINCIPAL_TAG}: {principalPercent:.2f}%')
