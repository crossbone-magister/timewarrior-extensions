"""
This script takes a csv file and inserts each line into timewarrior as a closed interval.
"""

import sys
import csv
import os

if __name__ == "__main__":
  if len(sys.argv) < 2:
      raise ValueError('No file name specified')

  file_to_import = sys.argv[1]
  file_to_importName = os.path.basename(file_to_import)
  tracking_date = os.path.splitext(file_to_importName)[0]
  print(f'Importing {file_to_import}')

  with open(file_to_import, newline='', encoding='UTF-8') as csvFile:
      time_track_reader = csv.reader(csvFile)
      for time_track in time_track_reader:
          command = f'timew track {tracking_date}T{time_track[0]} - {tracking_date}T{time_track[1]} {time_track[2]}'
          os.system(command)
