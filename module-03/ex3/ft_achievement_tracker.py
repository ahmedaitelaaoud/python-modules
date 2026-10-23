"""Exercise 3: Achievement Tracker.

Demonstrates set operations for unique and shared achievements.
"""




def get_data_set():
    """Return the sample achievement data for all players."""
    return {
        'alice': ['first_blood', 'pixel_perfect', 'speed_runner',
                  'first_blood', 'first_blood'],
        'bob': ['level_master', 'boss_hunter', 'treasure_seeker',
                'level_master', 'level_master', 'first_blood'],
        'charlie': ['treasure_seeker', 'boss_hunter', 'combo_king',
                    'first_blood', 'boss_hunter', 'first_blood',
                    'boss_hunter', 'first_blood'],
        'diana': ['first_blood', 'combo_king', 'level_master',
                  'treasure_seeker', 'speed_runner', 'combo_king',
                  'combo_king', 'level_master'],
        'eve': ['level_master', 'treasure_seeker', 'first_blood',
                'treasure_seeker', 'first_blood', 'treasure_seeker'],
        'frank': ['explorer', 'boss_hunter', 'first_blood', 'explorer',
                  'first_blood', 'boss_hunter']
    }


def main():
    """Run the achievement tracker demo."""
    data_set = get_data_set()

    print("=== Achievement Tracker System ===")

    player_sets = {
        name: set(achievements)
        for name, achievements in data_set.items()
    }

    for name, achievements in player_sets.items():
        print(f"Player {name} achievements: {achievements}")

    print("\n=== Achievement Analytics ===")

    all_achievements = set().union(*player_sets.values())

    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_achievements = set.intersection(*player_sets.values())

    print(f"Common to all players: {common_achievements}")

    rare_achievements = set.difference(*player_sets.values())

    print(f"Rare achievements (1 player): {rare_achievements}")

    print("\n=== Specific Comparison (Alice vs Bob) ===")

    alice = player_sets['alice']
    bob = player_sets['bob']
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
