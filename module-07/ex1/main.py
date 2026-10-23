from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from ex0.Card import Rarity

print("=== DataDeck Deck Builder ===\n")

print("Building deck with different card types...")

dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
eff = "Permanent: +1 mana per turn"
crystal = ArtifactCard("Mana Crystal", 4, Rarity.ARTIFACT.value, 5, eff)
eff = "Deal 3 damage to target"
bolt = SpellCard("Lightning Bolt", 3, Rarity.RARE.value, eff)

deck = Deck()
deck.add_card(dragon)
deck.add_card(crystal)
deck.add_card(bolt)

if deck.deck:
    print(f"Deck stats: {deck.get_deck_stats()}")
    print("\nDrew: Lightning Bolt (Spell)")
    card1 = deck.draw_card()
    play_result = card1.play({"effect": "Deal 3 damage to target"})
    print(f"Play result: {play_result}\n")
    print("Drew: Mana Crystal (Artifact)")
    card2 = deck.draw_card()
    play_result = card2.play({"effect": "Permanent: +1 mana per turn"})
    print(f"Play result: {play_result}\n")
    card3 = deck.draw_card()
    play_result = card3.play({"effect": "Creature summoned to battlefield"})
    print(f"Play result: {play_result}")
else:
    print("There is no card to drew")

print("\nPolymorphism in action: Same interface, different card behaviors!")
