from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    ARTIFACT = "Artifact"
    LEGENDARY = "Legendary"
    RARE = "Rare"
    COMMON = "Common"
    EPIC = "Epic"


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict: ...

    def get_card_info(self) -> dict:
        return self.__dict__

    def is_playable(self, available_mana: int):
        return available_mana >= self.cost
