from alchemy.grimoire import validate_ingredients, record_spell

print("=== Circular Curse Breaking ===\n")

print("Testing ingredient validation:")
result1 = validate_ingredients("fire air")
print(f"validate_ingredients(\"fire air\"): {result1}")
result2 = validate_ingredients("dragon scales")
print(f"validate_ingredients(\"dragon scales\"): {result2}\n")

print("Testing spell recording with validation:")
result3 = record_spell("Fireball", "fire air")
print(f"record_spell(\"Fireball\", \"fire air\"): {result3}")
result4 = record_spell("Dark Magic", "shadow")
print(f"record_spell(\"Dark Magic\", \"shadow\"): {result4}\n")

print("Testing late import technique:")
result5 = record_spell("Lightning", "air")
print(f"record_spell(\"Lightning\", \"air\"): {result5}\n")

print("Circular dependency curse avoided using late imports!")
print("All spells processed safely!")
