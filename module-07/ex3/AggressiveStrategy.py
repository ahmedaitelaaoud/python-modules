from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        priority = []
        others = []
        for target in available_targets:
            if "Player" in str(target):
                priority.append(target)
            else:
                others.append(target)
        return priority + others

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        available_mana = 10
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        sorted_hand = sorted(hand, key=lambda c: c.cost)

        for card in sorted_hand:
            if card.cost <= available_mana:
                cards_played.append(card.name)
                available_mana -= card.cost
                mana_used += card.cost
                damage_dealt += getattr(card, "attack", 0)
                damage_dealt += getattr(card, "damage", 0)

        targets = self.prioritize_targets(battlefield + ["Enemy Player"])
        targets_attacked = targets[:1] if targets else ["Enemy Player"]
        damage_dealt += 3 * len(cards_played)

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt,
        }
