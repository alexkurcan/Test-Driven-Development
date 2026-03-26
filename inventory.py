# adds an item to the inventory
def add_item(inventory, item):
    if inventory["locked"]:  # if inventory is locked, return it unchanged
        return inventory
    # item must be a non-empty string
    if not isinstance(item, str) or item == "":
        raise ValueError
    # cannot add item if inventory is at capacity
    if len(inventory["items"]) >= inventory["capacity"]:
        raise ValueError
    inventory["items"].append(item)

    return inventory


# removes the first occurrence of an item
def remove_item(inventory, item):
    if inventory["locked"]:  # same as line 3
        return inventory
    if item not in inventory["items"]:  # item must exist in inventory
        raise ValueError
    inventory["items"].remove(item)  # removes the item
    return inventory


# returns the number of items currently in inventory
def get_item_count(inventory):
    return len(inventory["items"])
