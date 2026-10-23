def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]
    items = ingredients.lower().split()
    invalid = [item for item in items if item not in valid]
    if invalid:
        return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
