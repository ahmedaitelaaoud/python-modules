from typing import Optional
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    good_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now()
    )
    print("Space Station Data Validation")
    print("="*40)
    print("Valid station created:")
    print(f"ID: {good_station.station_id}")
    print(f"Name: {good_station.name}")
    print(f"Crew: {good_station.crew_size}")
    print(f"Power: {good_station.power_level}")
    print(f"Oxygen: {good_station.oxygen_level}")
    print("Status: Operational")
    print()

    try:
        bad_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=999,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
        bad_station.crew_size
    except ValidationError as e:
        print("="*40)
        print("Expected validation error:")
        clean_msg = e.errors()[0]['msg']
        print(clean_msg)


if __name__ == "__main__":
    main()
