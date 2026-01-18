def set_achievements(achievements: str) -> set:
    split = achievements.split(",")
    return set(split)


def test_exercise() -> None:
    print("=== Achievement Tracker System ===")
    print()
    alice = set_achievements("first_kill,level_10,treasure_hunter,\
    speed_demon")
    print(f"Player alice achievements: {alice}")
    bob = set_achievements("first_kill,level_10,boss_slayer,collector")
    print(f"Player bob achievements: {bob}")
    charlie = set_achievements("level_10,treasure_hunter,boss_slayer,\
    speed_demon,perfectionist")
    print(f"Player charlie achievements: {charlie}")
    print()
    print("=== Achievement Analytics ===")
    union = set.union(alice, bob, charlie)
    print(f"All unique achievements: {union}")
    print(f"Total unique achievements: {len(union)}")
    print()
    intersection = set.intersection(alice, bob, charlie)
    print(f"Common to all players: {intersection}")
    intersection_ab = set.intersection(alice, bob)
    intersection_ac = set.intersection(alice, charlie)
    intersection_bc = set.intersection(bob, charlie)
    unique_to_players = set.difference(union, intersection_ab,
                                       intersection_ac, intersection_bc)
    print(f"Rare achievements (1 player): {unique_to_players}")
    print()
    print(f"Alice vs Bob common: {set.intersection(alice, bob)}")
    print(f"Alice unique: {set.difference(alice, bob)}")
    print(f"Bob unique: {set.difference(bob, alice)}")


if __name__ == "__main__":
    test_exercise()
