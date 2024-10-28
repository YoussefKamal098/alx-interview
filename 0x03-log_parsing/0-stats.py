#!/usr/bin/python3
"""
Log Parsing Module

This module provides functionality to parse log entries
from standard input, analyze them,
and compute metrics based on HTTP response codes and
file sizes. It reads log lines,
processes them based on a specific format, and outputs statistics after
every 10 lines or upon keyboard interruption (CTRL+C).

Log entry format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>

Attributes:
    total_file_size (int): Cumulative file size from all processed log lines.
    status_counts (dict): Dictionary that stores counts of each
    HTTP status code encountered (200, 301, 400, 401, 403, 404, 405, 500).

Functions:
    process_line(line: str) -> None:
        Processes a single line of log input. If the line
        matches the expected format,  it updates the
        `total_file_size` and `status_counts` attributes accordingly.

    print_metrics() -> None:
        Prints the current metrics, including total file size and counts
        of each HTTP status code in ascending order.
"""

import sys
import signal
import re

# Precompiled regex pattern to match the log line format
log_pattern = re.compile(
    r'(?P<ip_address>(?:\d{1,3}\.){3}\d{1,3}|[a-zA-Z0-9.-]+) - '
    r'\[(?P<date>\d{4}-\d{2}-\d{2} '
    r'\d{2}:\d{2}:\d{2}(?:\.\d{,12})?)\] '
    r'\"GET /projects/260 HTTP/1\.1\" '
    r'(?P<status_code>\d{3}|\w+) '
    r'(?P<file_size>\d{,12})'
)

# Dictionary to store the count of each status code
status_counts = {
    str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]
}
total_file_size = 0
line_count = 0


def print_metrics():
    """
    Print the metrics for total file size
    and status code counts.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def process_line(line: str):
    """
    Process a single line of log, updating metrics if
    the line is in the correct format.
    """
    global line_count
    global total_file_size

    match = re.fullmatch(log_pattern, line)
    if not match:
        return

    try:
        file_size = int(match.group("file_size"))
        status_code = match.group("status_code")

        # Update total file size and status code count
        total_file_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1

    except Exception as e:
        print("Error parsing line:", e)


def handle_interrupt(sig: int, frame):
    """
    Handle keyboard interrupt (CTRL + C) and print
    the metrics before exiting.
    """
    print_metrics()
    sys.exit(0)


if __name__ == "__main__":
    # Set up signal handler for CTRL + C
    signal.signal(signal.SIGINT, handle_interrupt)

    # Read lines from stdin and process them
    for line in sys.stdin:
        process_line(line.strip())

        line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0 and line_count > 0:
            print_metrics()

    # Print any remaining metrics after the loop
    print_metrics()
