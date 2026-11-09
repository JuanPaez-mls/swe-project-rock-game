import game_data


def test_determine_winner_when_player_wins():
    assert game_data.determine_winner("rock", "scissors") == "win"
    assert game_data.determine_winner("paper", "rock") == "win"
    assert game_data.determine_winner("scissors", "paper") == "win"


def test_determine_winner_when_player_loses():
    assert game_data.determine_winner("rock", "paper") == "loss"
    assert game_data.determine_winner("paper", "scissors") == "loss"
    assert game_data.determine_winner("scissors", "rock") == "loss"


def test_determine_winner_when_tied():
    assert game_data.determine_winner("rock", "rock") == "tie"
    assert game_data.determine_winner("paper", "paper") == "tie"
    assert game_data.determine_winner("scissors", "scissors") == "tie"


def test_clean_move_ignores_case_and_spaces():
    assert game_data.clean_move("rock") == "rock"
    assert game_data.clean_move("  PAPER  ") == "paper"
    assert game_data.clean_move("ScIsSoRs") == "scissors"


def test_clean_move_rejects_invalid_input():
    assert game_data.clean_move("lizard") is None
    assert game_data.clean_move("") is None


def test_get_computer_move_is_always_valid():
    for _ in range(20):
        assert game_data.get_computer_move() in game_data.VALID_MOVES


def test_get_result_message():
    assert (
        game_data.get_result_message("rock", "scissors", "win")
        == "Rock beats scissors! You win!"
    )
    assert (
        game_data.get_result_message("rock", "paper", "loss")
        == "Paper beats rock! You lose!"
    )
    assert game_data.get_result_message("rock", "rock", "tie") == "It's a tie!"


def test_record_result_updates_stats():
    game_data.reset_stats()

    game_data.record_result("win")
    game_data.record_result("win")
    game_data.record_result("loss")
    game_data.record_result("tie")

    assert game_data.stats == {"won": 2, "lost": 1, "tied": 1}
    assert game_data.get_total_games() == 4


def test_win_rate_is_rounded():
    game_data.reset_stats()

    game_data.record_result("win")
    game_data.record_result("win")
    game_data.record_result("loss")

    assert game_data.get_win_rate() == 67


def test_win_rate_is_zero_with_no_games():
    game_data.reset_stats()

    assert game_data.get_win_rate() == 0
