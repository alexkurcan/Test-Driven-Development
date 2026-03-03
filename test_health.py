def test_take_damage_reduces_health():
    assert take_damage(100, 30) == 70 

def test_heal_adds_health():
    assert heal(70, 30) == 100

def test_is_alive_true():
    assert is_alive(100) == True