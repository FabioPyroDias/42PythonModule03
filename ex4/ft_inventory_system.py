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
    print("=== Current Inventory ===")
    inventory_copy = {}
    for item in inventory.items():
        inventory_copy.update({item[0]: item[1]})
    inventory_sorted = {}
    current_items_in_inventory = 0
    sorted_max_items = len(inventory.keys())
    while current_items_in_inventory < sorted_max_items:
        item_to_be_transfered = None
        max_value = -1
        for item in inventory_copy.items():
            key, value = item
            if (value > max_value):
                item_to_be_transfered = item
                max_value = value
        inventory_sorted.update({
            item_to_be_transfered[0]: item_to_be_transfered[1]})
        inventory_copy[item_to_be_transfered[0]] = -1
        current_items_in_inventory += 1
    for item in inventory_sorted.items():
        key, value = item
        print(f"{key}: {value} units "
              f"({(value/number_of_occorrunces)*100:.1f}%)")
    print()
    print("=== Inventory Statistics ===")
    max_occorrunces_item = list(inventory_sorted.items())[0]
    max_occorrunces_str = ""
    if max_occorrunces_item[1] == 1:
        max_occorrunces_str = (f"{max_occorrunces_item[0]} ("
                               f"{max_occorrunces_item[1]} unit)")
    else:
        max_occorrunces_str = (f"{max_occorrunces_item[0]} ("
                               f"{max_occorrunces_item[1]} units)")
    min_value = max_occorrunces_item[1]
    min_occorrunces_str = ""
    for item in inventory_sorted.items():
        if item[1] < min_value:
            if item[1] == 1:
                min_occorrunces_str = (f"{item[0]} ("
                                       f"{item[1]} unit)")
            else:
                min_occorrunces_str = (f"{item[0]} ("
                                       f"{item[1]} units)")
            min_value = item[1]
    print(f"Most abundant: {max_occorrunces_str}")
    print(f"Least abundant: {min_occorrunces_str}")
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
    print(f"Sample lookup - 'sword' in inventory: "
          f"{bool(inventory.get('sword'))}")
