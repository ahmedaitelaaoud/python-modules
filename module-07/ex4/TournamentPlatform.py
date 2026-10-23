from ex4.TournamentCard import TournamentCard
import random


class TournamentPlatform:

    def __init__(self) -> None:

        self.registered_cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:

        self.registered_cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:

        card1 = self.registered_cards[card1_id]
        card2 = self.registered_cards[card2_id]

        winner = random.choice([card1, card2])
        if winner == card1:
            loser = card2
        else:
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list:

        cards_list = list(self.registered_cards.values())

        cards_list.sort(key=lambda card: card.rating, reverse=True)

        leaderboard = []

        for card in cards_list:
            leaderboard.append(card.get_tournament_stats())

        return leaderboard

    def generate_tournament_report(self) -> dict:

        total_cards = len(self.registered_cards)

        total_rating = 0
        for card in self.registered_cards.values():
            total_rating += card.rating

        if total_cards > 0:
            avg_rating = int(total_rating / total_cards)
        else:
            avg_rating = 0

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
