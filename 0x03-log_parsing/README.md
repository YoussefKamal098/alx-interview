# Log Parsing

## Overview

The `0-stats.py` script is a Python implementation of the Observer design pattern, designed for real-time log data parsing. It reads log entries from standard input (stdin), processes them to compute various metrics, and notifies observers about significant parsing events. The script is structured to handle log data in a specified format and is equipped to aggregate and summarize information efficiently.

## Project Description

For the **“0x03. Log Parsing”** project, you will apply your knowledge of Python programming, focusing on parsing and processing data streams in real time. This project involves:

- Reading from standard input (stdin)
- Handling data in a specific format
- Performing calculations based on the input data

### Concepts Needed

To successfully implement this project, you should be familiar with the following concepts:

- **File I/O in Python**: Understanding how to read from `sys.stdin` line by line.
  - [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

- **Signal Handling in Python**: Handling keyboard interruptions (CTRL + C) using signal handling in Python.
  - [Python Signal Handling](https://docs.python.org/3/library/signal.html)

- **Data Processing**: Parsing strings to extract specific data points and aggregating data to compute summaries.

- **Regular Expressions**: Using regular expressions to validate the format of each line.
  - [Python Regular Expressions](https://docs.python.org/3/library/re.html)

- **Dictionaries in Python**: Using dictionaries to count occurrences of status codes and accumulate file sizes.
  - [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

- **Exception Handling**: Handling possible exceptions that may arise during file reading and data processing.
  - [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

By studying these concepts and utilizing the resources provided, you will be well-prepared to tackle the log parsing project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.

### Additional Resources

- [Mock Technical Interview](https://www.youtube.com/watch?feature=shared&v=5dRTK-_Bzd0)

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A README.md file, at the root of the folder of the project, is mandatory.
- Your code should use the PEP 8 style (version 1.7.x).
- All your files must be executable.
- The length of your files will be tested using `wc`.

## Tasks

### 0. Log Parsing (Mandatory)

Write a script that reads stdin line by line and computes metrics:

- **Input format**: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
  - **Total file size**: `File size: <total size>` (where `<total size>` is the sum of all previous `<file size>`).
  - **Number of lines by status code**:
    - Possible status codes: `200, 301, 400, 401, 403, 404, 405, 500`
    - If a status code doesn’t appear or is not an integer, don’t print anything for this status code.
    - Format: `<status code>: <number>`
    - Status codes should be printed in ascending order.

#### Example

```bash
alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./0-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
alexa@ubuntu:~/0x03-log_parsing$ 
```

## [Solution Here](0-stats.py)

### Components

#### Classes

- **SignalHandler**: 
  - Manages system signals and executes a callback function when a specific signal is received.

- **Observer**: 
  - An abstract base class for observers that implement the `update` method to receive log updates.

- **StreamLogParser**: 
  - An abstract base class that defines the interface for log parsers, including methods to attach/detach observers and notify them of changes.

- **ConcreteLogParser**: 
  - A specific implementation of `StreamLogParser` that processes logs matching a predefined pattern and tracks file sizes and status codes.

- **ConsoleObserver**: 
  - A concrete observer that outputs log summary information to the console.

