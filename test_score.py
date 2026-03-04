import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score


def test_add_points(game):
    assert add_points(game, 10)["score"] == 10

def test_add_points_invalid(game):
    with pytest.raises(ValueError):
        add_points(game, -5)

def test_apply_multiplier(game):
    assert apply_multiplier(game, 3)["multiplier"] == 3

def test_apply_multiplier_invalid(game):
    with pytest.raises(ValueError):
        apply_multiplier(game, 0)

def test_reset_score(game):
    game["score"] = 500
    assert reset_score(game)["score"] == 0

def test_is_high_score(game):
    game["score"] = 100
    assert is_high_score(game, 50) == True

def test_is_high_score_invalid(game):
    with pytest.raises(ValueError):
        is_high_score(game, -1)