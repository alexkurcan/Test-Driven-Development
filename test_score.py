import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score


def test_add_points(game):
    # Adding 10 points to a new game should result in a score of 10
    assert add_points(game, 10)["score"] == 10


def test_add_points_invalid(game):
    # Adding a negative amount should raise a ValueError
    with pytest.raises(ValueError):
        add_points(game, -5)


def test_apply_multiplier(game):
    # Applying a multiplier of 3 should update the game's multiplier to 3
    assert apply_multiplier(game, 3)["multiplier"] == 3


def test_apply_multiplier_invalid(game):
    # Applying a multiplier less than 1 should raise a ValueError
    with pytest.raises(ValueError):
        apply_multiplier(game, 0)


def test_reset_score(game):
    # Set score to a non-zero value
    game["score"] = 500
    assert reset_score(game)["score"] == 0     # Resetting the score should set it back to 0


def test_is_high_score(game):
    # Set the score to 100
    game["score"] = 100
    assert is_high_score(game, 50) == True    # Score of 100 should be considered higher than threshold 50


def test_is_high_score_invalid(game):
    # Negative threshold should raise a ValueError
    with pytest.raises(ValueError):
        is_high_score(game, -1)