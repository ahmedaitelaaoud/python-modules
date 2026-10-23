from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ):
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or not isinstance(health, int):
            raise TypeError("Attack and health must be integers")

        if attack >= 0 and health >= 0:
            self.attack = attack
            self.health = health
        else:
            raise ValueError("attack and health must be positive integers")

        self.creature = "Creature"

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": game_state.get("effect", "No effect specified"),
        }

    def attack_target(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
