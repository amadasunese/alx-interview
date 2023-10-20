#!/usr/bin/python3
'''
A script that reads stdin line by line
'''
import re
import random
import sys
from time import sleep
import datetime


# Initialize variables to store metrics
datetime.datetime.now(),
random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
random.randint(1, 1024)

try:
    for line in sys.stdin:
        """
        Parse the line using regular expressions
        """
        match = re.match(r'^(\d{1,3}\n.\d{1,3}\n.\d{1,3}\n.\d{1,3}) - \[([^\]]+)] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$', line)

        if match:
            ip_address, date, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            # Update metrics
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1

            # Check if it's time to print statistics
            if line_count % 10 == 0:
                print(f"Total file size: {total_file_size}")
                for code in sorted(status_code_counts.keys()):
                    if status_code_counts[code] > 0:
                        print(f"{code}: {status_code_counts[code]}")

except KeyboardInterrupt:
    # Handle CTRL+C interruption by printing statistics
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

except Exception as e:
    print(f"Error: {e}")
