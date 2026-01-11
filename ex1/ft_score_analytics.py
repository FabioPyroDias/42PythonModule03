import sys


def score_analysis():
    """"""
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3.10 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    scores = [0] * (len(sys.argv) - 1)
    try:
        for index in range(1, len(sys.argv)):
            scores[index - 1] = int(sys.argv[index])
    except ValueError:
        print("Invalid score passed")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
