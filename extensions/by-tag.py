#!/usr/bin/env python3

"""
 This extension produces a report that indicates the total time tracked for each tag present in tracked intervals. Tags are sorted in descending order based on total time.
"""

from extensioncore import parse_from_stdin, seconds_to_hms, entry_to_seconds_diff

if __name__ == "__main__":
    _, time_entries = parse_from_stdin()
    time_per_tag = {}
    for entry in time_entries:
        time_spent = entry_to_seconds_diff(entry).seconds
        for tag in entry['tags']:
            if tag in time_per_tag:
                time_per_tag[tag] = time_per_tag[tag] + time_spent
            else:
                time_per_tag[tag] = time_spent

    length_longest_tag = 0
    for tag in time_per_tag:
        if len(tag) >= length_longest_tag:
            length_longest_tag = len(tag)
    time_per_tag = dict(reversed(sorted(time_per_tag.items(), key=lambda item: item[1])))
    for tag, time_spent in time_per_tag.items():
        time_spent_converted = seconds_to_hms(time_spent)
        print(f'{tag: <{length_longest_tag}} - {time_spent_converted[0]:03}h {time_spent_converted[1]:02}m {time_spent_converted[2]:02}s')
