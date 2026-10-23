from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

print("=== DataDeck Game Engine ===\n")
print("Configuring Fantasy Card Game...")

factory = FantasyCardFactory()
strategy = AggressiveStrategy()
engine = GameEngine()

print(f"Factory: {factory.__class__.__name__}")
print(f"Strategy: {strategy.get_strategy_name()}")
print(f"Available types: {factory.get_supported_types()}\n")

engine.configure_engine(factory, strategy)

print("Simulating aggressive turn...")
turn_result = engine.simulate_turn()

print(f"Hand: {turn_result['hand']}")
print("\nTurn execution:")
print(f"Strategy: {turn_result['strategy']}")
print(f"Actions: {turn_result['actions']}\n")

report = engine.get_engine_status()
print("Game Report:")
print(report)

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
