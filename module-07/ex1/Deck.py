from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck:
    def __init__(self) -> None:
        self.deck: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck:
            if card_name == card.name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        if self.deck:
            return self.deck.pop()

    def get_deck_stats(self) -> dict:

        total_cost = 0
        creatures = 0
        spells = 0
        artifacts = 0
        total_cards = len(self.deck)

        for card in self.deck:
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1
            elif isinstance(card, SpellCard):
                spells += 1
            total_cost += card.cost
        avg_cost = 0.0
        if total_cards > 0:
            avg_cost = total_cost / total_cards

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost,
        }
