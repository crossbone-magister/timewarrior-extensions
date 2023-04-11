# Timewarrior Extensions
This repository contains a collection of useful (at least for me) timewarrior extensions written in Python.

## Requirements
* Python 3

## Dependencies
No dependency required!

## Installation
Download or clone the repository.
Copy or create a symlink of all the files in the `extensions/` folder to your timewarrior extensions folder.
To find where the extension folder is, you can either run `timew extensions` or get more info on the [timewarrior doc](https://timewarrior.net/docs/api/).
Make sure the files are executable.

## Usage
To run an extension, simply execute `timew report <extension-name>` where `<extension-name>` is the name of the file of one of the extensions.

### extensioncore
This file contains a series of constants and utility functions used by other extensions.
> This file should not be run as an extension, as it won't process any input or produce any output.

### hours-day
This extension produces a report that indicates:
* For each day
    * Total hours tracked
    * Total hours over or under the `WORK_HOURS` threshold (defaults to 8)
    * If the day is a day off
* Total of days tracked
* Total time tracked
* Total overtime tracked, based on `WORK_HOURS` threshold
    * Hours tracked during a day off are considered overtime
* Total undertime tracked, based on `WORK_HOURS` threshold
* Actual overtime, as difference between total overtime and total undertime

> Since timewarrior doesn't allow custom parameters to be passed to extensions, in order to specify which days are off, it is necessary to open the extension file and modify the variable `DAYS_OFF`. Days range from zero (monday) to six (sunday) as specified in the python [documentation](https://docs.python.org/3/library/datetime.html#datetime.date.weekday)

### principal-hours-day
This extension produces a report that indicates the time tracked for a specific tag as percentage of total time tracked for each day. It also outputs an average percentage based on days tracked.
> Since timewarrior doesn't allow custom parameters to be passed to extensions, in order to select the tag used for elaboration, it is necessary to open the file extension and modify the variable `PRINCIPAL_TAG`

### by-tag
This extension produces a report that indicates the total time tracked for each tag present in tracked intervals. Tags are sorted in descending order based on total time.

## Timewarrior utils
Along side the extensions, this repository contains some useful (al least for me) utility scripts.

## csv-to-timew
This script takes a csv file and inserts each line into timewarrior as a closed interval.

### File name
The file **must** be named after the day the trackings have to be recorded to. File name **must** adhere to the following date format `YYYYMMDD.csv`
> For example, if you wish to register time trackings from January the First 2023, the file should be named `20230101.csv`

### Line format
Each line **must** be composed as follows:
```csv
#startTime in HHMM format,endTime in HHMM format,tags separated by spaces
0900,1000,coding python
```

## TODO
- [ ] Maybe find a better name for principal-hours-day report
- [X] Proper metadata parsing
- [X] Proper metadata honoring
- [X] Always consider days off (like weekend days) as overtime
- [ ] Always consider holy days as overtime
