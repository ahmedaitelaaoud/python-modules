from ex0.Card import Card


class SpellCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(effect_type, str):
            raise TypeError(f"{effect_type} must be a string")
        self.effect_type = effect_type
        self.spell_type = "Spell"

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": game_state.get("effect", "No effect specified"),
        }

    def resolve_effect(self, targets: list) -> dict:
        return {"effect": self.resolve_effect, "targets": targets}
