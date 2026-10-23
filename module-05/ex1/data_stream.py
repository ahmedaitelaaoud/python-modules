from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0
        self.error_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [
            item for item in data_batch
            if criteria.lower() in str(item).lower()
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed": self.processed_count,
            "errors": self.error_count
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        temps: List[float] = []
        alerts: int = 0

        for item in data_batch:
            try:
                if isinstance(item, dict):
                    if "temp" in item:
                        temp_val: float = float(item["temp"])
                        temps.append(temp_val)
                        self.processed_count += 1
                        if temp_val > 35.0 or temp_val < 0.0:
                            alerts += 1
                    elif "humidity" in item:
                        self.processed_count += 1
                    elif "pressure" in item:
                        self.processed_count += 1
                    else:
                        self.error_count += 1
                else:
                    self.error_count += 1
            except (TypeError, KeyError, ValueError):
                self.error_count += 1

        avg_temp: float = sum(temps) / len(temps) if temps else 0.0
        alert_str: str = f", {alerts} extreme alerts" if alerts else ""
        count: int = self.processed_count
        return (
            f"Sensor analysis: {count} readings processed, "
            f"avg temp: {avg_temp}°C{alert_str}"
        )


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        net_flow: int = 0

        for item in data_batch:
            try:
                if isinstance(item, dict):
                    if "buy" in item:
                        net_flow += int(item["buy"])
                        self.processed_count += 1
                    elif "sell" in item:
                        net_flow -= int(item["sell"])
                        self.processed_count += 1
                    else:
                        self.error_count += 1
                else:
                    self.error_count += 1
            except (ValueError, TypeError):
                self.error_count += 1

        count: int = self.processed_count
        return (
            f"Transaction analysis: {count} operations, "
            f"net flow: {net_flow:+} units"
        )


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        batch_error: int = 0
        for item in data_batch:
            if isinstance(item, str):
                self.processed_count += 1
                if item.lower() == "error":
                    batch_error += 1
            else:
                self.error_count += 1

        count: int = self.processed_count
        return (
            f"Event analysis: {count} events, "
            f"{batch_error} error detected"
        )


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def register_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_mixed_batch(self, data_batch: List[Any]) -> None:
        for stream in self.streams:
            old_count: int = stream.processed_count
            stream.process_batch(data_batch)
            batch_processed: int = stream.processed_count - old_count

            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {batch_processed} readings processed")
            elif isinstance(stream, TransactionStream):
                print(
                    f"- Transaction data: "
                    f"{batch_processed} operations processed"
                )
            elif isinstance(stream, EventStream):
                print(f"- Event data: {batch_processed} events processed")


if __name__ == "__main__":

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    sensor_data: List[Dict[str, float]] = [
        {"temp": 22.5},
        {"humidity": 65},
        {"pressure": 1013}
    ]
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch(sensor_data))

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")
    trans_data: List[Dict[str, int]] = [
        {"buy": 100},
        {"sell": 150},
        {"buy": 75}
    ]
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(transaction.process_batch(trans_data))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    event_data: List[str] = ["login", "error", "logout"]
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(event_data))

    print("=== Polymorphic Stream Processing ===")
    processor = StreamProcessor()
    processor.register_stream(sensor)
    processor.register_stream(transaction)
    processor.register_stream(event)

    mixed_batch: List[Any] = [
        {"temp": 20.0}, {"temp": 21.0},
        {"buy": 10}, {"sell": 10}, {"buy": 10}, {"sell": 10},
        "login", "update", "logout"
    ]
    print("Processing mixed stream types through unified interface...")
    print("\nBatch 1 Results:")
    processor.process_mixed_batch(mixed_batch)

    print("\nStream filtering active: High-priority data only")

    filter_test_batch: List[str] = [
        "critical sensor alert 1",
        "critical sensor alert 2",
        "normal sensor reading",
        "large transaction",
        "small transaction"
    ]

    critical_sensors: List[Any] = sensor.filter_data(
        filter_test_batch, criteria="critical"
    )
    large_trans: List[Any] = transaction.filter_data(
        filter_test_batch, criteria="large"
    )

    n_crit: int = len(critical_sensors)
    n_large: int = len(large_trans)
    print(
        f"Filtered results: {n_crit} critical sensor alerts, "
        f"{n_large} large transaction"
    )
    print("\nAll streams processed successfully. Nexus throughput optimal.")
