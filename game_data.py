import random

# The moves a player is allowed to choose.
VALID_MOVES = ["rock", "paper", "scissors"]

# Each key beats its value. For example, rock beats scissors.
WHAT_BEATS_WHAT = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

# This dictionary keeps track of the score across all rounds.
stats = {"won": 0, "lost": 0, "tied": 0}


def clean_move(user_input):
    """Turn the user's text into a valid move, or return None if it is not valid."""
    # .strip() removes extra spaces and .lower() makes the text lowercase,
    # so "  ROCK " becomes "rock".
    move = user_input.strip().lower()

    if move in VALID_MOVES:
        return move
    return None


def get_computer_move():
    """Pick rock, paper, or scissors at random."""
    return random.choice(VALID_MOVES)


def determine_winner(player_move, computer_move):
    """Return "win", "loss", or "tie" from the player's point of view."""
    if player_move == computer_move:
        return "tie"
    elif WHAT_BEATS_WHAT[player_move] == computer_move:
        return "win"
    else:
        return "loss"


def get_result_message(player_move, computer_move, result):
    """Return the sentence that explains who won the round."""
    if result == "win":
        return f"{player_move.capitalize()} beats {computer_move}! You win!"
    elif result == "loss":
        return f"{computer_move.capitalize()} beats {player_move}! You lose!"
    else:
        return "It's a tie!"


def record_result(result):
    """Add one to the correct stat after a round."""
    if result == "win":
        stats["won"] += 1
    elif result == "loss":
        stats["lost"] += 1
    else:
        stats["tied"] += 1


def get_total_games():
    """Return how many rounds have been played."""
    # sum() adds up all the numbers in the dictionary: won + lost + tied.
    return sum(stats.values())


def get_win_rate():
    """Return the percentage of games won, rounded to a whole number."""
    total_games = get_total_games()

    # Avoid dividing by zero when no games have been played.
    if total_games == 0:
        return 0

    win_percentage = stats["won"] / total_games * 100
    # Adding 0.5 before int() rounds to the nearest whole number.
    return int(win_percentage + 0.5)


def reset_stats():
    """Set the score back to zero."""
    stats["won"] = 0
    stats["lost"] = 0
    stats["tied"] = 0
