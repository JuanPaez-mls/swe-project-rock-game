import game_data


def show_greeting():
    """Print a welcome message."""
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Play as many rounds as you like against the computer.")


def show_menu():
    """Print the list of options."""
    print("\nMenu:")
    print("1. Play Round")
    print("2. View Stats")
    print("3. Exit")


def get_menu_choice():
    """Ask for a menu number until the user enters 1, 2, or 3."""
    while True:
        choice = input("\nChoose an Action (Enter 1-3): ").strip()

        if choice == "1" or choice == "2" or choice == "3":
            return choice

        print("\nWarning: Invalid choice. Please enter 1, 2, or 3.")


def get_player_move():
    """Ask for a move until the user enters rock, paper, or scissors."""
    while True:
        user_input = input("\nChoose a move (rock, paper, or scissors): ")
        player_move = game_data.clean_move(user_input)

        # clean_move() returns None when the input is not a valid move.
        if player_move is not None:
            return player_move

        print("\nWarning: Invalid move. Please type rock, paper, or scissors.")


def play_round():
    """Play one round against the computer."""
    player_move = get_player_move()
    computer_move = game_data.get_computer_move()
    result = game_data.determine_winner(player_move, computer_move)
    game_data.record_result(result)

    print(f"\nYou chose: {player_move}")
    print(f"Computer chose: {computer_move}")
    print(game_data.get_result_message(player_move, computer_move, result))


def show_stats(title):
    """Print the stats under the given title."""
    print(f"\n{title}:")
    print(f"Games Won: {game_data.stats['won']}")
    print(f"Games Lost: {game_data.stats['lost']}")
    print(f"Games Tied: {game_data.stats['tied']}")
    print(f"Total Games: {game_data.get_total_games()}")
    print(f"Win Rate: {game_data.get_win_rate()}%")


def run_menu():
    """Show the menu again and again until the user chooses to exit."""
    show_greeting()

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "1":
            play_round()
        elif choice == "2":
            show_stats("Current Statistics")
        else:
            show_stats("Final Statistics")
            print("\nThanks for playing. Goodbye!")
            break
