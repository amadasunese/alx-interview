#!/usr/bin/python3
"""Log parsing"""


import sys
import re

# Define regular expression patterns for extracting information
log_pattern = r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)'

# Initialize variables to store metrics
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()

        # Use regular expression to extract relevant information from the line
        match = re.match(log_pattern, line)
        if match:
            ip, status_code, file_size = match.groups()

            # Convert status_code and file_size to integers
            status_code = int(status_code)
            file_size = int(file_size)

            # Update metrics
            total_file_size += file_size
            status_codes[status_code] += 1
            line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print(f'Total file size: {total_file_size}')
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f'{code}: {status_codes[code]}')

except KeyboardInterrupt:
    print('Keyboard interruption detected. Printing current statistics:')
    print(f'Total file size: {total_file_size}')
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f'{code}: {status_codes[code]}')

