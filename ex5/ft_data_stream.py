import time


def generator(number_of_events: int):
    current_event = 1
    while current_event <= number_of_events:
        player = ""
        level = 0
        event = ""
        if current_event % 2 == 0:
            player = "bob"
            level = 12
            event = "found treasure"
        elif current_event % 3 == 0:
            player = "charlie"
            level = 8
            event = "leveled up"
        else:
            player = "alice"
            level = 5
            event = "killed monster"
        current_event += 1
        yield player, level, event


def fibonacci(number_of_elements: int):
    result = 0
    previous = 0
    current = 1
    number = 0
    while number < number_of_elements:
        yield result
        previous = result
        result = current
        current += previous
        number += 1


def prime(number_of_elements: int):
    current_prime = 2
    current_element = 0
    while current_element < number_of_elements:
        number = 2
        while number < current_prime:
            if current_prime % number == 0:
                current_prime += 1
                number = 2
            number += 1
        yield current_prime
        current_prime += 1
        current_element += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    current_event = 1
    max_event = 3
    print(f"Processing {max_event} game events...")
    iterator = iter(generator(max_event))
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0
    processing_time = time.time()
    while current_event <= max_event:
        player, level, event = next(iterator)
        print(f"Event {current_event}: Player {player} (level {level}) {event}")
        current_event += 1
        if level >= 10:
            high_level_players += 1
        if event == "found treasure":
            treasure_events += 1
        elif event == "leveled up":
            level_up_events += 1
    processing_time = time.time() - processing_time
    print("...")
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {max_event}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {processing_time} seconds")
    print()
    print("=== Generator Demonstration ===")
    fibonacci_elements = 10
    fibonacci_current_element = 0
    fibonacci_str = ""
    fibonacci_iterator = iter(fibonacci(fibonacci_elements))
    while fibonacci_current_element < fibonacci_elements:
        fibonacci_str += f"{next(fibonacci_iterator)}"
        fibonacci_current_element += 1
        if fibonacci_current_element != fibonacci_elements:
            fibonacci_str += ", "
    print(f"Fibonacci sequence (first 10): {fibonacci_str}")
    prime_elements = 5
    prime_current_element = 0
    prime_str = ""
    prime_iterator = iter(prime(prime_elements))
    while prime_current_element < prime_elements:
        prime_str += f"{next(prime_iterator)}"
        prime_current_element += 1
        if prime_current_element != prime_elements:
            prime_str += ", "
    print(f"Prime numbers (first {prime_elements}): {prime_str}")