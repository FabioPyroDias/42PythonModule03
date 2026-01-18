import time


def generator(number_of_events: int):
    name = ""
    level = 0
    action = ""
    for event in range(number_of_events):
        if event == 0:
            name = "alice"
        elif event % 2 == 0:
            name = "charlie"
        elif event % 3 == 0:
            name = "dahlia"
        elif event % 4 == 0:
            name = "erik"
        elif event % 5 == 0:
            name = "friedrich"
        elif event % 7 == 0:
            name = "gemma"
        elif event % 11 == 0:
            name = "harper"
        elif event % 13 == 0:
            name = "iris"
        elif event % 17 == 0:
            name = "jade"
        elif event % 19 == 0:
            name = "kane"
        elif event % 23 == 0:
            name = "lua"
        elif event % 29 == 0:
            name = "maya"
        elif event % 31 == 0:
            name = "noah"
        elif event % 37 == 0:
            name = "orion"
        elif event % 41 == 0:
            name = "phoenix"
        elif event % 43 == 0:
            name = "quin"
        elif event % 47 == 0:
            name = "raphael"
        elif event % 53 == 0:
            name = "sonny"
        elif event % 59 == 0:
            name = "tate"
        elif event % 61 == 0:
            name = "ulises"
        elif event % 67 == 0:
            name = "violet"
        elif event % 71 == 0:
            name = "winter"
        elif event % 73 == 0:
            name = "xena"
        elif event % 79 == 0:
            name = "yoshiro"
        elif event % 83 == 0:
            name = "zelda"
        else:
            name = "bob"
        if event == 0:
            level = 5
        elif event % 2 == 0:
            level = 8
        elif event % 3 == 0:
            level = 15
        elif event % 4 == 0:
            level = 2
        elif event % 5 == 0:
            level = 19
        elif event % 7 == 0:
            level = 21
        elif event % 11 == 0:
            level = 24
        elif event % 13 == 0:
            level = 25
        elif event % 17 == 0:
            level = 28
        elif event % 19 == 0:
            level = 30
        elif event % 23 == 0:
            level = 33
        elif event % 29 == 0:
            level = 38
        elif event % 31 == 0:
            level = 42
        elif event % 37 == 0:
            level = 48
        elif event % 41 == 0:
            level = 52
        elif event % 43 == 0:
            level = 59
        elif event % 47 == 0:
            level = 63
        elif event % 53 == 0:
            level = 70
        elif event % 59 == 0:
            level = 77
        elif event % 61 == 0:
            level = 82
        elif event % 67 == 0:
            level = 86
        elif event % 71 == 0:
            level = 90
        elif event % 73 == 0:
            level = 93
        elif event % 79 == 0:
            level = 96
        elif event % 83 == 0:
            level = 99
        else:
            level = 12
        if event == 0:
            action = "killed monster"
        elif event % 2 == 0:
            action = "leveled up"
        elif event % 3 == 0:
            action = "found clue"
        elif event % 5 == 0:
            action = "sold treasure"
        elif event % 7 == 0:
            action = "found cave"
        elif event % 11 == 0:
            action = "searched ruins"
        elif event % 13 == 0:
            action = "upgraded equipment"
        elif event % 17 == 0:
            action = "fast traveled"
        elif event % 19 == 0:
            action = "jumped to their death"
        elif event % 23 == 0:
            action = "took the easy way out"
        elif event % 29 == 0:
            action = "discovered dungeon"
        elif event % 31 == 0:
            action = "caught a pokemon"
        else:
            action = "found treasure"
        yield name, level, action


def fibonacci(element: int):
    result = 0
    previous = 0
    next = 1
    number = 0
    while number < element:
        yield result
        previous = result
        result = next
        next = previous + result
        number += 1


def prime(element: int):
    result = 0
    max = 2
    while result < element:
        is_prime = True
        current = 2
        while current <= max / 2:
            if max % current == 0:
                is_prime = False
            current += 1
        if is_prime:
            yield max
            result += 1
        max += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print()
    number_of_events = 1000
    print(f"Processing {number_of_events} game events...")
    print()
    iterator = iter(generator(number_of_events))
    event_index = 0
    high_level_players = 0
    treasure_related_events = 0
    level_related_events = 0
    duration = time.time()
    while event_index < number_of_events:
        name, level, action = next(iterator)
        print(f"Event {event_index + 1}: Player {name} "
              f"(level {level}) {action}")
        if level >= 10:
            high_level_players += 1
        if action == "leveled up":
            level_related_events += 1
        elif action == "found treasure" or action == "sold treasure":
            treasure_related_events += 1
        event_index += 1
    duration = time.time() - duration
    print("...")
    print("")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {number_of_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_related_events}")
    print(f"Level-up events: {level_related_events}")
    print("")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {duration} seconds")
    print("")
    print("=== Generator Demonstration ===")
    max_elements = 10
    iterator_fibonacci = iter(fibonacci(max_elements))
    element = 0
    result = ""
    while element < max_elements:
        result += f"{next(iterator_fibonacci)}"
        element += 1
        if element != max_elements:
            result += ", "
    print(f"Fibonacci sequence (first {max_elements}): {result}")
    max_elements = 5
    iterator_prime = iter(prime(max_elements))
    element = 0
    result = ""
    while element < max_elements:
        result += f"{next(iterator_prime)}"
        element += 1
        if element != max_elements:
            result += ", "
    print(f"Prime numbers (first {max_elements}): {result}")
