#!/usr/bin/python3
'''
A script that reads stdin line by line
'''
import sys

# Define status codes
STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize metrics
total_file_size = 0
num_lines_by_status_code = {status_code: 0 for status_code in STATUS_CODES}

# Read lines from stdin
for line in sys.stdin:
    # Split line into fields
    fields = line.split()

    # Check if line is in the expected format
    if len(fields) != 6 or not fields[4].isdigit() or not fields[5].isdigit():
        continue

    # Update metrics
    total_file_size += int(fields[5])
    num_lines_by_status_code[int(fields[4])] += 1

    # Print metrics if every 10 lines or keyboard interruption
    if line_number % 10 == 0 or sys.stdin.isatty():
        print("Total file size: {}".format(total_file_size))
        for status_code in sorted(num_lines_by_status_code.keys()):
            num_lines = num_lines_by_status_code[status_code]
            if num_lines > 0:
                print("{}: {}".format(status_code, num_lines))
