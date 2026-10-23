"""Exercise 1: Score Analytics.

Parse numeric scores from the command line and print summary statistics.
"""

import sys


def parse_scores(args):
    """Convert a list of strings to integers, skipping invalid entries."""
    scores = []
    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            continue
    return scores


def main(argv):
    """Entry point for command-line score analytics."""
    print("=== Player Score Analytics ===")

    scores = parse_scores(argv[1:])
    if scores:
        total_score = sum(scores)
        score_count = len(scores)
        high_score = max(scores)
        low_score = min(scores)

        print(f"Scores processed:{scores}")
        print(f"Total players: {score_count}")
        print(f"Total score: {total_score}")
        print(f"Average score: {total_score / score_count}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {high_score - low_score}")
        return

    print("No scores provided. Usage: python3 ft_score_analytics.py "
          "<score1> <score2> ...")


if __name__ == "__main__":
    main(sys.argv)
