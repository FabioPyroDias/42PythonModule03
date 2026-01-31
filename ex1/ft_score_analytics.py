import sys


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        try:
            scores = []
            index = 1
            processed = "Scores processed: ["
            while index < len(sys.argv):
                scores.append(int(sys.argv[index]))
                processed += f"{scores[index - 1]}"
                index += 1
                if index < len(sys.argv):
                    processed += ", "
            processed += "]"
            print(processed)
            total_players = len(sys.argv) - 1
            print(f"Total players: {total_players}")
            total_score = sum(scores)
            print(f"Total score: {total_score}")
            average_score = total_score / total_players
            print(f"Average score: {average_score}")
            max_score = max(scores)
            print(f"High score: {max_score}")
            min_score = min(scores)
            print(f"Low score: {min_score}")
            range_score = max_score - min_score
            print(f"Score range: {range_score}")
        except ValueError:
            print("Invalid input")
