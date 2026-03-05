# adds an item to the inventory
def add_item(inventory, item):
    if inventory["locked"]:                                  # if the inventory is locked, return it unchanged
        return inventory
    
    if not isinstance(item, str) or item == "":              # item must be a non-empty string
        raise ValueError("item must be a non-empty string")

    if len(inventory["items"]) >= inventory["capacity"]:     # check if inventory is already at capacity
        raise ValueError("inventory is full")
    inventory["items"].append(item)
    return inventory


# removes the first occurrence of an item from the inventory
def remove_item(inventory, item):
    if inventory["locked"]:                           # same purpose as line 3
        return inventory
    if item not in inventory["items"]:
        raise ValueError("item not in inventory")     # if the item is not in the inventory, raise an error
    inventory["items"].remove(item)
    return inventory


# returns the number of items currently in the inventory
def get_item_count(inventory):
    return len(inventory["items"])           # returns the length of the items list