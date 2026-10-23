from typing import Union
from ex3.CardFactory import CardFactory
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

CREATURES = {
    "dragon": ("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5),
    "goblin": ("Goblin Warrior", 2, Rarity.COMMON.value, 2, 2),
    "elf": ("Forest Elf", 3, Rarity.RARE.value, 3, 4),
}

SPELLS = {
    "fireball": ("Fireball", 4, Rarity.RARE.value, "damage"),
    "ice_bolt": ("Ice Bolt", 2, Rarity.COMMON.value, "debuff"),
    "lightning": ("Lightning Bolt", 3, Rarity.RARE.value, "damage"),
}

ARTIFACTS = {
    "mana_ring": (
        "Mana Ring",
        2,
        Rarity.ARTIFACT.value,
        5,
        "Permanent: +1 mana per turn",
    ),
    "staff": (
        "Arcane Staff",
        3,
        Rarity.RARE.value,
        4,
        "Boost spell damage by 2",
    ),
    "crystal": (
        "Mana Crystal",
        4,
        Rarity.ARTIFACT.value,
        6,
        "Double mana on first turn",
    ),
}


class FantasyCardFactory(CardFactory):

    def create_creature(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        if isinstance(name_or_power, str):
            data = CREATURES.get(name_or_power.lower(), CREATURES["goblin"])
        elif isinstance(name_or_power, int):
            if name_or_power >= 5:
                data = CREATURES["dragon"]
            else:
                data = CREATURES["goblin"]
        else:
            data = CREATURES["goblin"]
        return CreatureCard(*data)

    def create_spell(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        if isinstance(name_or_power, str):
            data = SPELLS.get(name_or_power.lower(), SPELLS["fireball"])
        elif isinstance(name_or_power, int):
            data = (
                SPELLS["ice_bolt"]
                if name_or_power < 3
                else SPELLS["fireball"]
            )
        else:
            data = SPELLS["fireball"]
        return SpellCard(*data)

    def create_artifact(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        if isinstance(name_or_power, str):
            data = ARTIFACTS.get(name_or_power.lower(), ARTIFACTS["mana_ring"])
        elif isinstance(name_or_power, int):
            data = (
                ARTIFACTS["staff"]
                if name_or_power >= 3
                else ARTIFACTS["mana_ring"]
            )
        else:
            data = ARTIFACTS["mana_ring"]
        return ArtifactCard(*data)

    def create_themed_deck(self, size: int) -> dict:
        cards = []
        per_type = size // 3
        remainder = size % 3

        for i in range(per_type):
            creature_name = "dragon" if i % 2 == 0 else "goblin"
            cards.append(self.create_creature(creature_name))
        for i in range(per_type):
            spell_name = "fireball" if i % 2 == 0 else "lightning"
            cards.append(self.create_spell(spell_name))
        for i in range(per_type + remainder):
            artifact_name = "mana_ring" if i % 2 == 0 else "staff"
            cards.append(self.create_artifact(artifact_name))

        return {"theme": "Fantasy", "size": len(cards), "cards": cards}

    def get_supported_types(self) -> dict:
        return {
            "creatures": list(CREATURES.keys()),
            "spells": list(SPELLS.keys()),
            "artifacts": list(ARTIFACTS.keys()),
        }
