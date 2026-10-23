from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity

print("=== DataDeck Card Foundation ===\n")
print("Testing Abstract Base Class Design:\n")

card = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
print("CreatureCard Info:")
print(card.get_card_info())

available_mana = 6
print(f"\nPlaying Fire Dragon with {available_mana} mana available:")
print(f"Playable: {card.is_playable(available_mana)}")
play_result = card.play({"effect": "Creature summoned to battlefield"})
print(f"Play result: {play_result}")

print("\nFire Dragon attacks Goblin Warrior:")
print(f"Attack result: {card.attack_target('Goblin Warrior')}")

available_mana = 3
print(f"\nTesting insufficient mana ({available_mana} available):")
print(f"Playable: {card.is_playable(available_mana)}")

print("\nAbstract pattern successfully demonstrated!")
