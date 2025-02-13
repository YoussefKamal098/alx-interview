#!/usr/bin/python3
"""
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

    def __init__(self, sig: signal.Signals, callback: callable = None):
        """
        Initialize with a specific signal and an optional callback.

        Parameters:
            sig (signal.Signals): The signal to handle.
            callback (Callable): The function to call when the
                                signal is received.
        """
        self._callback = callback
        self._sig = sig
        signal.signal(self._sig, self._handle_signal)

    @property
    def callback(self) -> callable:
        """Get the current callback function."""
        return self._callback

    @callback.setter
    def callback(self, callback: callable):
        """
        Set or update the callback function for the signal.

        Parameters:
            callback (Callable): The function to call when the
                                signal is received.
        """
        self._callback = callback

    def _handle_signal(self, sig: int, frame):
        """
        Handle the signal and execute the callback if set.

        Parameters:
            sig (int): The received signal.
            frame (Any): The current stack frame.
        """
        if self._callback:
            self._callback()
        else:
            print("No callback set for handling the signal.")
        sys.exit(0)


class Observer(ABC):
    """Abstract base class for observers to receive updates from subjects."""

    @abstractmethod
    def update(self, data: dict[str, any]):
        """
        Receive updates from the subject.

        Parameters:
            data (Dict[str, Any]): The data passed from
                                    the subject to observers.
        """
        pass


class StreamLogParser(ABC):
    """Abstract base class for parsing logs and notifying observers."""

    def __init__(self, stream):
        """
        Initialize the StreamLogParser with a stream for log input.

        Parameters:
            stream (TextIO): A text-based input/output stream used for
                            log parsing.
        """
        self.stream = stream  # Store the stream to read from
        self._observers = []

    def attach(self, observer: Observer):
        """
        Attach an observer to the subject.

        Parameters:
            observer (Observer): The observer to attach.
        """
        self._observers.append(observer)

    def detach(self, observer: Observer):
        """
        Detach an observer from the subject.

        Parameters:
            observer (Observer): The observer to detach.
        """
        self._observers.remove(observer)

    def notify(self):
        """Notify all observers about changes in log parsing data."""
        summary = self.get_summary()
        for observer in self._observers:
            observer.update(summary)

    @abstractmethod
    def get_summary(self) -> dict[str, any]:
        """
        Get summary data from the log parsing.

        Returns:
            Dict[str, Any]: A dictionary containing the summary of parsed data.
        """
        pass

    @abstractmethod
    def start(self):
        """Start the log parsing process."""
        pass


class ConcreteLogParser(StreamLogParser):
    """Concrete implementation of StreamLogParser that processes log data."""

    _pattern = re.compile(
        r'(?P<ip_address>\d{1,3}(?:\.\d{1,3}){3}) - '
        r'\[(?P<date>\d{4}-\d{2}-\d{2} '
        r'\d{2}:\d{2}:\d{2}(?:\.\d{,12})?)\] '
        r'\"GET /projects/260 HTTP/1\.1\" '
        r'(?P<status_code>(200|301|400|401|403|404|405|500)) '
        r'(?P<file_size>\d{,12})'
    )

    def __init__(self, stream):
        """
        Initialize ConcreteLogParser, setting up necessary attributes.

        Parameters:
            stream (TextIO): A text-based input/output stream used
                            for log parsing.
        """
        super().__init__(stream)
        self._files_size = 0
        self._status_code_count = defaultdict(int)
        self._line_count = 0
        self.signal_handler = SignalHandler(signal.SIGINT)
        self.signal_handler.callback = self.notify  # Set callback for signal

    def start(self):
        """Start the log parser, reading from the provided stream."""
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
                print(f"Error parsing the log '{log}': {e}")

        self.notify()   # Notify observers with the final summary

    @classmethod
    def parse_log(cls, log: str) -> dict[str, any]:
        """
        Parse a single log entry and return its components.

        Parameters:
            log (str): A single log entry string.

        Returns:
            Dict[str, Any]: A dictionary with parsed log components if
                            matched, else empty.
        """
        match = re.fullmatch(cls._pattern, log)
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

    def log(self, file_size: int, status_code: int):
        """
        Log file size and status code for analysis.

        Parameters:
            file_size (int): Size of the file accessed.
            status_code (int): HTTP status code of the response.
        """
        self._files_size += file_size
        self._status_code_count[status_code] += 1

    def get_summary(self) -> dict[str, any]:
        """
        Return the summary of parsed logs.

        Returns:
            Dict[str, Any]: A summary including file size and
                            status code counts.
        """
        return {
            "files_size": self._files_size,
            "status_code_count": self._status_code_count
        }


class ConsoleObserver(Observer):
    """Concrete observer that prints the log summary to the console."""

    def update(self, data: dict[str, any]):
        """
        Receive and process log summary data.

        Parameters:
            data (Dict[str, Any]): A dictionary containing the log summary.
        """
        print(f"File Size: {data['files_size']}")
        for code, count in sorted(data['status_code_count'].items()):
            print(f"{code}: {count}")


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
