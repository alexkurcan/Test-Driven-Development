def add_points(game, amount):
    # Do not allow zero or negative point additions
    if amount <= 0:
        raise ValueError
    if not game["active"]:     # If the game is not active, do not modify anything
        return game
    game["score"] += amount * game["multiplier"]     # Add points multiplied by the current multiplier
    return game

def apply_multiplier(game, multiplier):
    # Multiplier must be at least 1
    if multiplier < 1:
        raise ValueError
    if not game["active"]:     # If the game is not active, do not modify anything
        return game
    game["multiplier"] = multiplier      # Set the new multiplier
    return game


def reset_score(game):
    # Reset score back to 0
    game["score"] = 0
    game["multiplier"] = 1     # Reset multiplier back to default value of 1
    return game


def is_high_score(game, threshold):
    # Threshold must not be negative
    if threshold < 0:
        raise ValueError
    
    # Return True if score exceeds the threshold
    return game["score"] > threshold