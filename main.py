import game_data
import menu

# Set this to False when you want to hand in the project or just play the game.
# True = call every function once (a quick tour), then start the real game.
SHOW_DEMO = True


def call_all_functions():
    """Call every function in game_data.py and menu.py once, so you can see what each one does."""
    print("\n===== DEMO: calling every function =====")

    # --- game_data.py ---
    print("\n--- game_data.py ---")
    print("clean_move:", game_data.clean_move("  ROCK "))
    print("get_computer_move:", game_data.get_computer_move())
    print("determine_winner:", game_data.determine_winner("rock", "scissors"))
    print(
        "get_result_message:", game_data.get_result_message("rock", "scissors", "win")
    )
    game_data.record_result("win")
    print("record_result: stats are now", game_data.stats)
    print("get_total_games:", game_data.get_total_games())
    print("get_win_rate:", game_data.get_win_rate())
    game_data.reset_stats()
    print("reset_stats: stats are now", game_data.stats)

    # --- menu.py ---
    print("\n--- menu.py ---")
    menu.show_greeting()
    menu.show_menu()
    menu.show_stats("Demo Statistics")

    print("\nNext, three functions will ask you to type something.")
    print("get_menu_choice returned:", menu.get_menu_choice())
    print("get_player_move returned:", menu.get_player_move())
    menu.play_round()

    # The demo played a round, so clear the score before the real game starts.
    game_data.reset_stats()
    print("\n===== DEMO finished: now starting the real game (run_menu) =====")


def main():
    """Start the program."""

    menu.run_menu()


# This line makes sure the game only starts when you run this file directly,
# not when another file imports it.
if __name__ == "__main__":
    main()
