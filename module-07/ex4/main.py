from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex0.Card import Rarity

platform = TournamentPlatform()

print("\n== DataDeck Tournament Platform ===\n")
print("Registering Tournament Cards...")

dragon = TournamentCard(
    "Fire Dragon",
    cost=5,
    rarity=Rarity.EPIC.value,
    attack=80,
    health=500,
    starting_rating=1200,
)
wizard = TournamentCard(
    "Ice Wizard",
    cost=4,
    rarity=Rarity.RARE.value,
    attack=60,
    health=400,
    starting_rating=1150,
)

platform.register_card(dragon)
platform.register_card(wizard)

for card in [dragon, wizard]:
    stats = card.get_tournament_stats()

    interfaces_str = ", ".join(stats["interfaces"])

    print(f"\n{stats['name']} (ID: {stats['card_id']}):")
    print(f"- Interfaces: [{interfaces_str}]")
    print(f"- Rating: {stats['rating']}")
    print(f"- Record: {stats['record']}")

print("\nCreating tournament match...")
match_result = platform.create_match(dragon.card_id, wizard.card_id)
print(f"Match result: {match_result}")


print("\nTournament Leaderboard:")
leaderboard = platform.get_leaderboard()


for i, stats in enumerate(leaderboard, 1):
    print(
        f"{i}. {stats['name']} - Rating: {stats['rating']} ({stats['record']})"
    )

print("\nPlatform Report:")
report = platform.generate_tournament_report()
print(report)

print("\n=== Tournament Platform Successfully Deployed! ===")
print(
    "All abstract patterns working together harmoniously!"
)
