inventory = []

def collect_item(item):
    inventory.append(item)
    print(item, "added to inventory")


def display_inventory():
    print("Inventory:")

    for item in inventory:
        print(item)


collect_item("Sword")
collect_item("Shield")
collect_item("Potion")

display_inventory()