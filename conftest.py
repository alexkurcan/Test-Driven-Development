import pytest

@pytest.fixture
def player():
    return {'health': 100, 'max_health': 100, 'alive': True}

@pytest.fixture
def dead_player():
    return {'health': 0, 'max_health': 100, 'alive': False}

@pytest.fixture
def game():
    return {"score": 0, "multiplier": 1, "active": True}    # score starts at 0, multiplier starts at 1, and game is active (added day 3)

@pytest.fixture
def locked_inventory():
    return {"items": ["sword"], "capacity": 10, "locked": True} # used in tests where the inventory should not allow changes (added day 4)