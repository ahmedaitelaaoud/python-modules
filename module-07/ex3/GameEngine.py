from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            return {"error": "Engine not configured"}

        deck_data = self.factory.create_themed_deck(3)
        hand = deck_data["cards"]
        self.cards_created += len(hand)

        battlefield = []
        result = self.strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt", 0)

        hand_summary = [f"{c.name} ({c.cost})" for c in hand]

        return {
            "hand": hand_summary,
            "strategy": self.strategy.get_strategy_name(),
            "actions": result,
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": (
                self.strategy.get_strategy_name() if self.strategy else None
            ),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
