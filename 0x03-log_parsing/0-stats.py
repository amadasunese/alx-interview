#!/usr/bin/python3
'''Log parsing'''


import re
import sys
from collections import defaultdict

# Initialize variables to store metrics
total_file_size = 0
status_code_count = defaultdict(int)

try:
    line_number = 0

    # Regular expression to match the expected input format
    log_format = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)')

    for line in sys.stdin:
        line_number += 1

        # Try to match the line with the expected format
        match = log_format.match(line)
        if match:
            ip, status_code, file_size = match.groups()

            # Update total file size
            total_file_size += int(file_size)

            # Update status code count
            if status_code in {'200', '301', '400', '401', '403', '404', '405', '500'}:
                status_code_count[status_code] += 1

        # Print statistics after every 10 lines
        if line_number % 10 == 0:
            print(f'Total file size: {total_file_size}')
            for code in sorted(status_code_count.keys()):
                print(f'{code}: {status_code_count[code]}')

except KeyboardInterrupt:
    # Handle keyboard interruption
    print(f'Total file size: {total_file_size}')
    for code in sorted(status_code_count.keys()):
        print(f'{code}: {status_code_count[code]}')