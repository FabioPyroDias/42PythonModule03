class Item():
    """"""
    def __init__(self, name: str, type: str, rarity: str, value: int):
        """"""
        self.name = name
        self.type = type
        self.rarity = rarity
        self.value = value


def add_item(inventory: dict, item: Item, count: int) -> None:
    result = inventory.get(item, 0)
    inventory.update({item: count + result})


def update_inventory(inventory: dict, item: Item, count: int) -> None:
    inventory.update({item: count})


def get_inventory_info(inventory: dict) -> str:
    info = ""
    index = 0
    for slot in inventory.items():
        item, count = slot
        info += (f"{item.name} ({item.type}, {item.rarity}): {count}x @ "
                 f"{item.value} gold each = {item.value * count}")
        index += 1
        if index < len(inventory.items()):
            info += "\n"
    return info


def get_item_count(inventory: dict) -> int:
    total = 0
    for count in inventory.values():
        total += count
    return total


def get_inventory_value(inventory: dict) -> int:
    value = 0
    for slot in inventory.items():
        item, count = slot
        value += item.value * count
    return value


def get_type_occurrences(inventory: dict) -> str:
    type_ocrr = {}
    result = ""
    for slot in inventory.items():
        item, count = slot
        occr = type_ocrr.get(item.type, 0)
        type_ocrr.update({item.type: occr + count})
    index = 0
    size = len(type_ocrr.keys())
    for slot in type_ocrr.items():
        item, count = slot
        result += f"{item}({count})"
        index += 1
        if (index < size):
            result += ", "
    return result


def transfer_items(src: dict, dst: dict, item: Item, count: int) -> bool:
    initial_count = src.get(item, 0)
    if count <= 0 or initial_count <= 0 or initial_count < count:
        return False
    result = dst.get(item, 0)
    dst.update({item: count + result})
    src.update({item: initial_count - count})
    return True


def get_rarest_items(dict1: dict, dict2: dict) -> str:
    all_items = {}
    result = ""
    for slot in dict1.items():
        item, count = slot
        all_items.update({item: dict1.get(item, 0) + count})
    for slot in dict2.items():
        item, count = slot
        all_items.update({item: all_items.get(item, 0) + count})
    rarest = "rare"
    index = 0
    rarest_count = 0
    for item in all_items.keys():
        if item.rarity == rarest:
            rarest_count += 1
    for item in all_items.keys():
        if item.rarity == rarest:
            result += item.name
            index += 1
            if index < rarest_count:
                result += ", "
    return result


def test_example():
    print("=== Player Inventory System ===")
    print()
    sword = Item("sword", "weapon", "rare", 500)
    potion = Item("potion", "consumable", "common", 50)
    shield = Item("shield", "armor", "uncommon", 200)
    alice = {}
    add_item(alice, sword, 1)
    add_item(alice, potion, 5)
    add_item(alice, shield, 1)
    print("=== Alice's Inventory ===")
    print(get_inventory_info(alice))
    print()
    print(f"Inventory value: {get_inventory_value(alice)} gold")
    print(f"Item count: {get_item_count(alice)} items")
    print(f"Categories: {get_type_occurrences(alice)}")
    print()
    bob = {}
    print("=== Transaction: Alice gives Bob 2 potions ===")
    if transfer_items(alice, bob, potion, 2):
        print("Transaction successful!")
    else:
        print("Transaction unsuccessful...")
    print()
    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice.get(potion, 0)}")
    print(f"Bob potions: {bob.get(potion, 0)}")
    print()
    print("=== Inventory Analytics ===")
    value_alice = get_inventory_value(alice)
    value_bob = get_inventory_value(bob)
    if value_alice > value_bob:
        print(f"Most valuable player: Alice ({value_alice} gold)")
    elif value_alice < value_bob:
        print(f"Most valuable player: Bob ({value_bob} gold)")
    else:
        print(f"Both players have the same value ({value_alice} gold)")
    items_alice = get_item_count(alice)
    items_bob = get_item_count(bob)
    if items_alice > items_bob:
        print(f"Most items: Alice ({items_alice} items)")
    elif items_alice < items_bob:
        print(f"Most items: Bob ({items_bob} items)")
    else:
        print(f"Both players have the same number of items "
              f"({items_alice} items)")
    add_item(bob, Item("magic_ring", "armor", "rare", 150), 1)
    print(f"Rarest items: {get_rarest_items(alice, bob)}")
