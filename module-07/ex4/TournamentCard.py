from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        starting_rating: int,
    ):
        super().__init__(name, cost, rarity)

        self.attack_damage = attack
        self.health = health

        self.wins = 0
        self.losses = 0
        self.base_rating = starting_rating
        self.rating = starting_rating
        self.card_id = f"{name.lower().replace(' ', '_')}_001"

    def play(self, game_state: dict) -> dict:

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "tournament_id": self.card_id,
        }

    def attack(self, target) -> dict:

        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.attack_damage,
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage

        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "new_health": self.health,
            "still_alive": self.health > 0,
        }

    def calculate_rating(self) -> int:

        self.rating = self.base_rating + (self.wins * 16) - (self.losses * 16)
        return self.rating

    def update_wins(self, wins: int) -> None:

        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.calculate_rating()

    def get_tournament_stats(self) -> dict:

        return {
            "card_id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}",
            "interfaces": ["Card", "Combatable", "Rankable"],
        }

    def get_rank_info(self) -> dict:

        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
            "record": f"{self.wins}-{self.losses}",
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_damage, "health": self.health}
