#!/usr/bin/python3
"""
log parsing
"""
import sys
import re

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        # Parse the line using regular expressions
        match = re.match(r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$', line)
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
            print(f"{code}: {status_code_counts[code}")

except Exception as e:
    print(f"Error: {e}")