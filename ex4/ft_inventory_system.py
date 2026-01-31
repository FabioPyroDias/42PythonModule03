import sys


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    if len(sys.argv) == 1:
        print("No items received")
        sys.exit()
    inventory = {}
    try:
        argument = 1
        while argument < len(sys.argv):
            if sys.argv[argument].find(":") == -1:
                raise ValueError()
            item = sys.argv[argument].split(":")
            inventory.update({item[0]: int(item[1])})
            argument += 1
    except ValueError:
        print("Invalid input")
        sys.exit()
    number_of_items = len(inventory.values())
    number_of_occorrunces = 0
    for occorrunces in inventory.values():
        number_of_occorrunces += occorrunces
    print(f"Total items in inventory: {number_of_occorrunces}")
    print(f"Unique item types: {number_of_items}")
    print()
    print(f"=== Current Inventory ===")
    for item in inventory.items():
        key, value = item
        print(f"{key}: {value} units ({(value/number_of_occorrunces)*100:.1f}%)")
    print()
    print("=== Inventory Statistics ===")
    item_index = 0
    min_occorrunces = 0
    min_occorrunces_str = ""
    max_occorrunces = 0
    max_occorrunces_str = ""
    for item in inventory.items():
        key, value = item
        if item_index == 0:
            min_occorrunces = value
            max_occorrunces = value
            if value == 1:
                min_occorrunces_str = f"{key} ({value} unit)"
                max_occorrunces_str = f"{key} ({value} unit)"
            else:
                min_occorrunces_str = f"{key} ({value} units)"
                max_occorrunces_str = f"{key} ({value} unit)"
        else:
            if min_occorrunces > value:
                min_occorrunces = value
                if value == 1:
                    min_occorrunces_str = f"{key} ({value} unit)"
                else:
                    min_occorrunces_str = f"{key} ({value} units)"
            if max_occorrunces < value:
                max_occorrunces = value
                if value == 1:
                    max_occorrunces_str = f"{key} ({value} unit)"
                else:
                    max_occorrunces_str = f"{key} ({value} units)"
        item_index += 1
    print(f"Most abundant: {max_occorrunces_str}")
    print(f"Least abundant:{min_occorrunces_str}")
    print()
    print("=== Item Categories ===")
    scarce_inventory = {}
    moderate_inventory = {}
    for item in inventory.items():
        key, value = item
        if value <= 3:
            scarce_inventory.update({key: value})
        else:
            moderate_inventory.update({key: value})
    print(f"Moderate: {moderate_inventory}")
    print(f"Scarce: {scarce_inventory}")
    print()
    print("=== Management Suggestions ===")
    suggestions = []
    for item in scarce_inventory.items():
        key, value = item
        if value < 2:
            suggestions.append(key)
    print(f"Restock needed: {suggestions}")
    print()
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {inventory.keys()}")
    print(f"Dictionary values: {inventory.values()}")
    print(f"Sample lookup - 'sword' in inventory: {bool(inventory.get('sword'))}")
