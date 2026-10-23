#!/usr/bin/env python3
"""
Exercise 6: Data Alchemist
Demonstrates list, dictionary, and set comprehensions for
elegant data transformation and analysis.
"""




def get_game_data():
    """Return the game analytics dataset."""
    data = {
        'players': {
            'alice': {
                'level': 41,
                'total_score': 2824,
                'sessions_played': 13,
                'favorite_mode': 'ranked',
                'achievements_count': 5
            },
            'bob': {
                'level': 16,
                'total_score': 4657,
                'sessions_played': 27,
                'favorite_mode': 'ranked',
                'achievements_count': 2
            },
            'charlie': {
                'level': 44,
                'total_score': 9935,
                'sessions_played': 21,
                'favorite_mode': 'ranked',
                'achievements_count': 7
            },
            'diana': {
                'level': 3,
                'total_score': 1488,
                'sessions_played': 21,
                'favorite_mode': 'casual',
                'achievements_count': 4
            },
            'eve': {
                'level': 33,
                'total_score': 1434,
                'sessions_played': 81,
                'favorite_mode': 'casual',
                'achievements_count': 7
            },
            'frank': {
                'level': 15,
                'total_score': 8359,
                'sessions_played': 85,
                'favorite_mode': 'competitive',
                'achievements_count': 1
            }
        },
        'sessions': [
            {'player': 'bob', 'duration_minutes': 94, 'score': 1831,
             'mode': 'competitive', 'completed': False},
            {'player': 'bob', 'duration_minutes': 32, 'score': 1478,
             'mode': 'casual', 'completed': True},
            {'player': 'diana', 'duration_minutes': 17, 'score': 1570,
             'mode': 'competitive', 'completed': False},
            {'player': 'alice', 'duration_minutes': 98, 'score': 1981,
             'mode': 'ranked', 'completed': True},
            {'player': 'diana', 'duration_minutes': 15, 'score': 2361,
             'mode': 'competitive', 'completed': False},
            {'player': 'eve', 'duration_minutes': 29, 'score': 2985,
             'mode': 'casual', 'completed': True},
            {'player': 'frank', 'duration_minutes': 34, 'score': 1285,
             'mode': 'casual', 'completed': True},
            {'player': 'alice', 'duration_minutes': 53, 'score': 1238,
             'mode': 'competitive', 'completed': False},
            {'player': 'bob', 'duration_minutes': 52, 'score': 1555,
             'mode': 'casual', 'completed': False},
            {'player': 'frank', 'duration_minutes': 92, 'score': 2754,
             'mode': 'casual', 'completed': True},
            {'player': 'eve', 'duration_minutes': 98, 'score': 1102,
             'mode': 'casual', 'completed': False},
            {'player': 'diana', 'duration_minutes': 39, 'score': 2721,
             'mode': 'ranked', 'completed': True},
            {'player': 'frank', 'duration_minutes': 46, 'score': 329,
             'mode': 'casual', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 56, 'score': 1196,
             'mode': 'casual', 'completed': True},
            {'player': 'eve', 'duration_minutes': 117, 'score': 1388,
             'mode': 'casual', 'completed': False},
            {'player': 'diana', 'duration_minutes': 118, 'score': 2733,
             'mode': 'competitive', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 22, 'score': 1110,
             'mode': 'ranked', 'completed': False},
            {'player': 'frank', 'duration_minutes': 79, 'score': 1854,
             'mode': 'ranked', 'completed': False},
            {'player': 'charlie', 'duration_minutes': 33, 'score': 666,
             'mode': 'ranked', 'completed': False},
            {'player': 'alice', 'duration_minutes': 101, 'score': 292,
             'mode': 'casual', 'completed': True},
            {'player': 'frank', 'duration_minutes': 25, 'score': 2887,
             'mode': 'competitive', 'completed': True},
            {'player': 'diana', 'duration_minutes': 53, 'score': 2540,
             'mode': 'competitive', 'completed': False},
            {'player': 'eve', 'duration_minutes': 115, 'score': 147,
             'mode': 'ranked', 'completed': True},
            {'player': 'frank', 'duration_minutes': 118, 'score': 2299,
             'mode': 'competitive', 'completed': False},
            {'player': 'alice', 'duration_minutes': 42, 'score': 1880,
             'mode': 'casual', 'completed': False},
            {'player': 'alice', 'duration_minutes': 97, 'score': 1178,
             'mode': 'ranked', 'completed': True},
            {'player': 'eve', 'duration_minutes': 18, 'score': 2661,
             'mode': 'competitive', 'completed': True},
            {'player': 'bob', 'duration_minutes': 52, 'score': 761,
             'mode': 'ranked', 'completed': True},
            {'player': 'eve', 'duration_minutes': 46, 'score': 2101,
             'mode': 'casual', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 117, 'score': 1359,
             'mode': 'casual', 'completed': True}
        ],
        'game_modes': ['casual', 'competitive', 'ranked'],
        'achievements': [
            'first_blood', 'level_master', 'speed_runner',
            'treasure_seeker', 'boss_hunter', 'pixel_perfect',
            'combo_king', 'explorer'
        ]
    }
    return data


def list_comprehension_examples(data):
    """Demonstrate list comprehensions for filtering and transformation."""
    print("=== List Comprehension Examples ===")
    players = data['players']

    high_scorers = [name for name, info in players.items()
                    if info['total_score'] >= 5000]
    print(f"High scorers {high_scorers}")

    doubled_scores = [info['total_score'] * 2
                      for info in players.values()]
    print(f"Scores doubled {doubled_scores}")

    active_players = [name for name, info in players.items()
                      if info['sessions_played'] > 20]
    print(f"Active players: {active_players}")


def dict_comprehension_examples(data):
    """Demonstrate dictionary comprehensions for mappings and grouping."""
    print("=== Dict Comprehension Examples ===")
    players = data['players']

    player_scores = {name: info['total_score']
                     for name, info in players.items()}
    print(f"Player scores: {player_scores}")

    score_categories = {
        name: (
            'low' if info['total_score'] < 2000
            else 'mid' if info['total_score'] < 5000
            else 'high'
        )
        for name, info in players.items()
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {name: info['achievements_count']
                          for name, info in players.items()}
    print(f"Achievement counts: {achievement_counts}")


def set_comprehension_examples(data):
    """Demonstrate set comprehensions for unique data analysis."""
    print("=== Set Comprehension Examples ===")
    players = data['players']
    sessions = data['sessions']

    unique_players = {name for name in players.keys()}
    print(f"Unique players: {unique_players}")

    unique_achievements = {name for name in data['achievements']}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {session['mode'] for session in sessions}
    print(f"Active regions: {active_regions}")


def combined_analysis(data):
    """Demonstrate combined comprehensions for complex analytics."""
    print("=== Combined Analysis ===")
    players = data['players']

    total_players = len(players)
    print(f"Total players: {total_players}")

    total_unique_achievements = len({a for a in data['achievements']})
    print(f"Total unique achievements: {total_unique_achievements}")

    average_score = (
        sum(info['total_score'] for info in players.values()) / total_players
    )
    print(f"Average score: {average_score:.2f}")

    top_name, top_info = max(
        players.items(), key=lambda item: item[1]['total_score']
    )
    print(f"Top performer: {top_name}")


def main():
    """Main function demonstrating comprehensions."""
    # Get data
    data = get_game_data()

    print("=== Game Analytics Dashboard ===\n")
    # List comprehensions
    list_comprehension_examples(data)
    print()
    # Dictionary comprehensions
    dict_comprehension_examples(data)
    print()
    # Set comprehensions
    set_comprehension_examples(data)
    print()
    # Combined analysis
    combined_analysis(data)


if __name__ == "__main__":
    main()
