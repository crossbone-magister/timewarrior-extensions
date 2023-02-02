# Timewarrior Extensions
This repository contains a collection of useful (at least for me) timewarrior extensions written in Python.

## Requirements
* Python 3

## Dependencies
No dependency required!

## Installation
Copy or create a symlink of all the files in the `extensions/` folder to your timewarrior extensions forder. 
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
    * Total hours over or under the `WORK_HOURS` threshold (default to 8)
* Total of days registered
* Total time registered
* Total overtime registered, based on `WORK_HOURS` threshold
* Total undertime registered, based on `WORK_HOURS` threshold
* Actual overtime, as difference between total overtime and total undertime

### principal-hours-day
This extension produces a report that indicates the time tracked for a specific tag as percentage of total time tracked for each day.
> Since timewarrior doesn't allow custom parameters to be passed to extensions, in order to select the tag used for elaboration, it is necessary to open the file extension and modifiy the variable `PRINCIPAL_TAG`

### by-tag

## Timewarrior utils
TODO

## TODO
TODO
