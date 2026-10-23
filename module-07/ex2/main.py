from ex2.EliteCard import EliteCard
from ex0.Card import Rarity

print("=== DataDeck Ability System ===\n")
print("EliteCard capabilities:")
print("""- Card: ['play', 'get_card_info', 'is_playable']
- Combatable: ['attack', 'defend', 'get_combat_stats']
- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n""")


card = EliteCard("Arcane Warrior", 4, Rarity.LEGENDARY.value, 5, 5)
print("Playing Arcane Warrior (Elite Card):\n")

print("Combat phase:")
print(f"Attack result: {card.attack('Enemy')}")
print(f"Defense result: {card.defend(2)}\n")

print("Magic phase:")
print(f"Spell cast: {card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
print(f"Mana channel: {card.channel_mana(3)}\n")

print("Multiple interface implementation successful!")
