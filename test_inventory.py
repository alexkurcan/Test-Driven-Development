import pytest
from inventory import add_item, remove_item, get_item_count


# Test that add_item successfully adds an item to the inventory
def test_add_item_adds_item(empty_inventory):
    add_item(empty_inventory, "sword")
    assert "sword" in empty_inventory["items"]


# Test that adding an item to a full inventory raises an error
def test_add_item_full_inventory(full_inventory):
    with pytest.raises(ValueError):
        add_item(full_inventory, "shield")


# Test that a locked inventory cannot be modified
def test_add_item_locked_inventory(locked_inventory):
    result = add_item(locked_inventory, "shield")
    assert result == locked_inventory


# Test that remove_item correctly removes an item from the inventory
def test_remove_item_removes_item(partial_inventory):
    remove_item(partial_inventory, "sword")
    assert "sword" not in partial_inventory["items"]


# Test that removing an item not in the inventory raises an error
def test_remove_item_not_found(partial_inventory):
    with pytest.raises(ValueError):
        remove_item(partial_inventory, "potion")


# Test that get_item_count returns the correct number of items
def test_get_item_count(empty_inventory):
    assert get_item_count(empty_inventory) == 0