class Player():
    def __init__(self, name: str, score: int, status: bool,
                 achievements: list, region: str) -> None:
        try:
            self.__name = None
            self.__score = 0
            self.__status = False
            self.__achievements = []
            self.__region = None
            self.set_name(name)
            self.set_score(score)
            self.set_status(status)
            self.set_achievements(achievements)
            self.set_region(region)
        except ValueError as error:
            print(f"Player Creation Failed: {error}")

    def set_name(self, name: str) -> None:
        if name is None or len(name) == 0:
            raise ValueError("Player name cannot be empty")
        self.__name = name

    def set_score(self, score: int) -> None:
        if score < 0:
            raise ValueError("Player score cannot be negative")
        self.__score = score

    def set_status(self, status: bool) -> None:
        self.__status = status

    def set_achievements(self, achievements: list) -> None:
        achievement_index = 0
        if achievements is None:
            raise ValueError("Player achievement cannot be None")
        while achievement_index < len(achievements):
            if achievements[achievement_index] is None:
                raise ValueError("Player achievement cannot be empty")
            achievement_index += 1
        self.__achievements = achievements

    def set_region(self, region: str) -> None:
        if region is None or len(region) == 0:
            raise ValueError("Player region cannot be None")
        self.__region = region

    def get_name(self) -> str:
        return self.__name

    def get_score(self) -> int:
        return self.__score

    def get_status(self) -> bool:
        return self.__status

    def get_achievements(self) -> set:
        return self.__achievements

    def get_region(self) -> str:
        return self.__region


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    print()
    print("=== List Comprehension Examples ===")
    players = [
        Player("alice", 2300, True,
               ["first_kill", "treasure_hunter", "speed_demon"], "north"),
        Player("bob", 1800, True,
               ["perfectionist", "collector", "treasure_hunter"], "east"),
        Player("charlie", 2150, True,
               ["collector", "level_10", "speed_demon"], "central"),
        Player("diana", 2050, False, [], "west")
    ]
    list_high_scorers = [player.get_name() for player in players
                         if player.get_score() > 2000]
    list_scores_double = [player.get_score() * 2 for player in players]
    list_active_players = [player.get_name() for player in players
                           if player.get_status()]
    print(f"High scorers (>2000): {list_high_scorers}")
    print(f"Scores doubled: {list_scores_double}")
    print(f"Active players: {list_active_players}")
    print()
    print("=== Dict Comprehension Examples ===")
    dict_player_scores = {player.get_name(): player.get_score()
                          for player in players}
    dict_score_categories = {
        "high": len([player.get_score() for player in players
                     if player.get_score() > 2000]),
        "medium": len([player.get_score() for player in players
                       if player.get_score() >= 1000
                       and player.get_score() <= 2000]),
        "low": len([player.get_score() for player in players
                    if player.get_score() < 1000])
    }
    dict_achievements_count = {player.get_name():
                               len(player.get_achievements())
                               for player in players}
    print(f"Player scores: {dict_player_scores}")
    print(f"Score categories: {dict_score_categories}")
    print(f"Achievement counts: {dict_achievements_count}")
    print()
    print("=== Set Comprehension Examples ===")
    set_players = set([player.get_name() for player in players])
    set_achievements = set(achievement for player in players for achievement
                           in player.get_achievements())
    set_regions = set([player.get_region() for player in players])
    print(f"Unique players: {set_players}")
    print(f"Unique achievements: {set_achievements}")
    print(f"Active regions: {set_regions}")
    print()
    print("=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    unique_number_achievements = len(
            {
                achievement
                for player in players
                for achievement in player.get_achievements()
            })
    print(f"Total unique achievements: {unique_number_achievements}")
    average_score = sum(
        [player.get_score() for player in players]) / len(players)
    print(f"Average score: {average_score}")
    top_performer = players[0]
    for player in players:
        if player.get_score() > top_performer.get_score():
            top_performer = player
    print(f"Top performer: {top_performer.get_name()} "
          f"({top_performer.get_score()} points, "
          f"{len(top_performer.get_achievements())} achievements)")
