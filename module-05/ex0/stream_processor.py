from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if self.validate(data):
            if isinstance(data, int):
                data = [data]
            count = len(data)
            l_sum = sum(data)
            avg = l_sum / count
            return f"Processed {count} numeric values, sum={l_sum}, avg={avg}"
        return "Error: invalid numeric data"

    def validate(self, data: Any) -> bool:
        if not data:
            return False
        if isinstance(data, (list)):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        elif isinstance(data, int):
            return True
        return False


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if self.validate(data):
            count = len(data)
            words = len(data.split())
            return f"Processed text: {count} characters, {words} words"
        return "Error: invalid text data"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if self.validate(data):
            parts = data.split(":", 1)
            level = parts[0].strip()
            message = parts[1].strip()
            severity = "ALERT" if level == "ERROR" else "INFO"
            return f"[{severity}] {level} level detected: {message}"
        return "Error: invalid log data"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        known_levels = ("ERROR", "INFO")
        return any(data.startswith(level) for level in known_levels)


if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    numeric = NumericProcessor()
    print("Initializing Numeric Processor...")
    data_num = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_num}")
    is_valid = numeric.validate(data_num)
    print(f"Validation: {'Numeric data verified' if is_valid else 'Failed'}")
    print(numeric.format_output(numeric.process(data_num)))

    print()

    text = TextProcessor()
    print("Initializing Text Processor...")
    data_text = "Hello Nexus World"
    print(f'Processing data: "{data_text}"')
    is_valid = text.validate(data_text)
    print(f"Validation: {'Text data verified' if is_valid else 'Failed'}")
    print(text.format_output(text.process(data_text)))

    print()

    log = LogProcessor()
    print("Initializing Log Processor...")
    data_log = "ERROR: Connection timeout"
    print(f'Processing data: "{data_log}"')
    is_valid = log.validate(data_log)
    print(f"Validation: {'Log entry verified' if is_valid else 'Failed'}")
    print(log.format_output(log.process(data_log)))

    print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data_samples: List[Any] = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready",
    ]

    for i in range(len(processors)):
        processor = processors[i]
        sample = data_samples[i]
        print(f"Result {i + 1}: {processor.process(sample)}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
