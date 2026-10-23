from enum import Enum
from pydantic import model_validator, BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_contact_rules(self):
        if not self.contact_id.startswith('AC'):
            raise ValueError("Contact ID must start with "
                             "\"AC\" (Alien Contact)")
        if (self.contact_type == ContactType.PHYSICAL
                and not self.is_verified):
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include "
                             "received messages")
        return self


def main():
    print("Alien Contact Log Validation")
    print("="*40)
    try:
        contact_51 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contact_type="radio",
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(f"ID: {contact_51.contact_id}")
        print(f"Type: {contact_51.contact_type.value}")
        print(f"Location: {contact_51.location}")
        print(f"Signal: {contact_51.signal_strength}/10")
        print(f"Duration: {contact_51.duration_minutes} minutes")
        print(f"Witnesses: {contact_51.witness_count}")
        msg = (contact_51.message_received if contact_51.message_received
               else "No message")
        print(f"Message: '{msg}'")
        print()
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])

    print("="*40)
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            contact_type="telepathic",
            location="Namic",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli"
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
