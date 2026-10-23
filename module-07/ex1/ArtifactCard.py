from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ):
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int):
            raise TypeError("durability must be integer")
        if durability >= 0:
            self.durability = durability
        else:
            raise ValueError("durability must be positive integer")

        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": game_state.get("effect", "No effect specified"),
        }

    def activate_ability(self) -> dict:
        return {"name": self.name, "active_ability": self.activate_ability}
