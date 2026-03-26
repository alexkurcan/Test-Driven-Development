import pytest
from inventory import add_item, remove_item, get_item_count


# test that add_item adds an item to the inventory
def test_add_item(inventory):
    add_item(inventory, "shield")
    assert "shield" in inventory["items"]


# test that adding to a full inventory raises an error
def test_add_item_full(inventory):
    inventory["items"] = ["a"] * inventory["capacity"]

    with pytest.raises(ValueError):
        add_item(inventory, "potion")


# test that a locked inventory cannot be modified
def test_add_item_locked(locked_inventory):
    result = add_item(locked_inventory, "shield")
    assert result == locked_inventory


# test removing an item
def test_remove_item(inventory):
    remove_item(inventory, "sword")
    assert "sword" not in inventory["items"]


# test removing an item that does not exist
def test_remove_item_invalid(inventory):
    with pytest.raises(ValueError):
        remove_item(inventory, "potion")


# test getting the number of items
def test_get_item_count(inventory):
    assert get_item_count(inventory) == len(inventory["items"])
