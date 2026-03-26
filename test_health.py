from health import is_alive, take_damage, heal


def test_take_damage_reduces_health():
    assert take_damage(100, 30) == 70


def test_heal_adds_health():
    assert heal(70, 30) == 100


def test_is_alive_true():
    assert is_alive(100) is True


def test_dead_player_is_not_alive():
    assert is_alive(0) is False


def test_dead_player_at_zero():
    assert take_damage(0, 50) == 0
