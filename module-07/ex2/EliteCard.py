from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self, name: str, cost: int, rarity: str, damage: int, health: int
    ):
        super().__init__(name, cost, rarity)
        if not isinstance(damage, int) or not isinstance(health, int):
            raise TypeError("Attack and health must be integers")

        if damage >= 0 and health >= 0:
            self.damage = damage
            self.health = health
        else:
            raise ValueError("attack and health must be positive integers")

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": game_state.get(
                "effect", "Elite deployed to battlefield"
            ),
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.damage,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = self.health - incoming_damage
        self.health -= incoming_damage
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.damage, "health": self.health}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost,
        }

    def channel_mana(self, amount: int) -> dict:
        self.cost += amount
        return {"channeled": amount, "total_mana": self.cost}

    def get_magic_stats(self) -> dict:
        return {"mana": self.cost}
