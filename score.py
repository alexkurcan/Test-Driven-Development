def add_points(game, amount):
    # doesn't allow zero or negative point additions
    if amount <= 0:
        raise ValueError
    if not game["active"]:                          # if the game is not active, do not modify anything
        return game
    game["score"] += amount * game["multiplier"]    # add points multiplied by the current multiplier
    return game

def apply_multiplier(game, multiplier):
    # multiplier must be at least 1
    if multiplier < 1:
        raise ValueError
    if not game["active"]:               # if the game is not active, do not modify anything
        return game
    game["multiplier"] = multiplier      # set the new multiplier
    return game


def reset_score(game):
    # reset score back to 0
    game["score"] = 0
    game["multiplier"] = 1     # reset multiplier back to default value of 1
    return game


def is_high_score(game, threshold):
    # threshold must not be negative
    if threshold < 0:
        raise ValueError
    return game["score"] > threshold