#!/usr/bin/python3
"""
log_parser_module.py

This module provides an implementation of the Observer design pattern, where
the StreamLogParser class serves as the subject that notifies observers
about log parsing events. It includes a SignalHandler to
manage system signals and an Observer interface for concrete observer
implementations.

Classes:
    - SignalHandler: Manages system signals and invokes callbacks.
    - Observer: Abstract base class for observers that need to
                implement the update method.
    - StreamLogParser: Abstract base class for parsing logs and
                        notifying observers.
    - ConcreteLogParser: A concrete implementation of StreamLogParser
                        for processing specific log formats.
    - ConsoleObserver: A concrete observer that outputs
                    log summaries to the console.
"""

import signal
import sys
import re
from abc import ABC, abstractmethod
from collections import defaultdict


class SignalHandler:
    """
    Handles system signals and executes a callback when a
    signal is received.
    """

    def __init__(self, sig: signal.Signals, callback=None):
        """Initialize with a specific signal and an optional callback."""
        self._callback = callback
        self._sig = sig
        signal.signal(self._sig, self._handle_signal)

    @property
    def callback(self):
        """Get the current callback function."""
        return self._callback

    @callback.setter
    def callback(self, callback: callable):
        """Set or update the callback function for the signal."""
        self._callback = callback

    def _handle_signal(self, sig: int, frame):
        """Handle the signal and execute the callback if set."""
        if self._callback:
            self._callback()
        else:
            print("No callback set for handling the signal.")
        sys.exit(0)


class Observer(ABC):
    """Abstract base class for observers to receive updates from subjects."""

    @abstractmethod
    def update(self, data: dict[any, any]):
        """Receive updates from the subject."""
        pass


class StreamLogParser(ABC):
    """Abstract base class for parsing logs and notifying observers."""

    def __init__(self, stream):
        """Initialize the StreamLogParser with a stream for log input."""
        self._observers = []
        self.stream = stream  # Store the stream to read from

    def attach(self, observer: Observer):
        """Attach an observer to the subject."""
        self._observers.append(observer)

    def detach(self, observer: Observer):
        """Detach an observer from the subject."""
        self._observers.remove(observer)

    def notify(self):
        """Notify all observers about changes in log parsing data."""
        summary = self.get_summary()
        for observer in self._observers:
            observer.update(summary)

    @abstractmethod
    def get_summary(self) -> dict[str, any]:
        """Get summary data from the log parsing."""
        pass

    @abstractmethod
    def start(self):
        """Start the log parsing."""
        pass


class ConcreteLogParser(StreamLogParser):
    """Concrete implementation of StreamLogParser that processes log data."""

    _pattern = r'(?P<ip_address>\d{1,3}(?:\.\d{1,3}){3}) - ' \
               r'\[(?P<date>\d{4}-\d{2}-\d{2} ' \
               r'\d{2}:\d{2}:\d{2}(?:\.\d{,12})?)\] ' \
               r'\"GET /projects/260 HTTP/1\.1\" ' \
               r'(?P<status_code>\d{3}) (?P<file_size>\d+)'

    def __init__(self, stream):
        """Initialize ConcreteLogParser, setting up necessary attributes."""
        super().__init__(stream)
        self._files_size = 0
        self._status_code_count = defaultdict(int)
        self._line_count = 0
        self.signal_handler = SignalHandler(signal.SIGINT)
        self.signal_handler.callback = self.notify  # Set callback for signal

    def start(self):
        """Starts the log parser, reading from the provided stream."""
        for log in self.stream:
            log = log.strip()  # Strip whitespace/newlines
            if not log:
                continue  # Skip empty lines

            try:
                log_info = self.parse_log(log)

                if not log_info:
                    continue

                file_size = int(log_info["file_size"])
                status_code = log_info["status_code"]

                # Log the file size and status code
                self.log(file_size, status_code)
                self._line_count += 1

                # Notify observers every 10 lines parsed
                if self._line_count % 10 == 0:
                    self.notify()

            except ValueError as e:
                print(f"Error parsing log: {e}")

    @classmethod
    def parse_log(cls, log) -> dict[str, str]:
        """Parses a single log entry and returns its components."""
        match = re.match(cls._pattern, log)
        if not match:
            print(
                "Log doesn't match the expected pattern. "
                "Check your logs, log skipped!"
            )
            return {}

        return {
            "ip_address": match.group("ip_address"),
            "date": match.group("date"),
            "status_code": match.group("status_code"),
            "file_size": match.group("file_size")
        }

    def log(self, file_size, status_code):
        """Log file size and status code for analysis."""
        self._files_size += file_size
        self._status_code_count[status_code] += 1

    def get_summary(self) -> dict[str, any]:
        """Return the summary of parsed logs."""
        return {
            "files_size": self._files_size,
            "status_code_count": self._status_code_count
        }


class ConsoleObserver(Observer):
    """Concrete observer that prints the log summary to the console."""

    def update(self, data):
        """Receive and process log summary data."""
        print(f"File Size: {data['files_size']}")
        for code, count in sorted(data['status_code_count'].items()):
            print(f"{code}: {count}")


# Example usage
def main():
    """Main entry point for the log parser."""
    # You can pass any iterable as a stream, for example, a file or a list
    log_stream = sys.stdin  # Replace with an actual stream if needed
    parser = ConcreteLogParser(log_stream)
    console_observer = ConsoleObserver()

    # Attach observer to StreamLogParser
    parser.attach(console_observer)

    # Handle Ctrl-C signal
    signal_handler = SignalHandler(signal.SIGINT)
    signal_handler.callback = parser.notify

    parser.start()  # Start parsing logs


if __name__ == "__main__":
    main()
