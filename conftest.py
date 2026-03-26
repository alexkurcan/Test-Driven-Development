import pytest


@pytest.fixture
def player():
    return {'health': 100, 'max_health': 100, 'alive': True}


@pytest.fixture
def dead_player():
    return {'health': 0, 'max_health': 100, 'alive': False}


@pytest.fixture
def game():
    # score starts at 0, multiplier starts at 1, game is active (added day 3)
    return {"score": 0, "multiplier": 1, "active": True}


@pytest.fixture
def inventory():
    # unlocked inventory
    return {"items": ["sword"], "capacity": 10, "locked": False}


@pytest.fixture
def locked_inventory():
    # locked inventory (both added on day 4)
    return {"items": ["sword"], "capacity": 10, "locked": True}
