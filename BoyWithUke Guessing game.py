import random

# Dictionary with Alec Benjamin's latest songs and their clues
boy_with_uke_recent_songs = {
    "The Book of You & I": "A song about memories and looking back on a past relationship.",
    "The Way You Felt": "Reflects on the emotions and nostalgia associated with a past love.",
    "Oh My God": "Addresses the struggles and challenges of pursuing dreams and aspirations.",
    "Mind is a Prison": "Explores the internal struggles of mental health and feeling trapped within one's thoughts.",
    "Must Have Been the Wind": "Touches on themes of loneliness and the feeling of being haunted by unseen forces.",
    "Demons": "Reflects on battling inner demons and the challenges of self-acceptance.",
    "Alamo": "A reflective song that delves into regrets and the complexities of life.",
    "Boy in the Bubble": "Addresses societal issues and the challenges faced by individuals who feel disconnected from society.",
    "1994": "A nostalgic look back at the past and the memories associated with that time.",
    "Let Me Down Slowly": "A song about the pain of a breakup and the desire for a gentle, gradual separation."
}

def generate_options(correct_answer, all_songs):
    """Generate multiple choice options including the correct answer."""
    options = [correct_answer]
    while len(options) < 4:
        option = random.choice(all_songs)
        if option not in options:
            options.append(option)
    random.shuffle(options)
    return options

def play_game():
    print("Welcome to the Alec Benjamin Songs Guessing Game!")
    print("You have 3 chances to guess each song.")
    print("Let's begin!\n")

    score = 0
    num_rounds = 7  # Number of rounds to play

    # Convert song titles to a list for easier manipulation
    all_songs = list(boy_with_uke_recent_songs.keys())

    for round_num in range(1, num_rounds + 1):
        print(f"\nRound {round_num}:")
        song_title = random.choice(all_songs)
        clue = boy_with_uke_recent_songs[song_title]
        options = generate_options(song_title, all_songs)
        guessed = False
        chances = 2

        print(f"Clue: {clue}\n")
        print("Options:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        while chances > 0:
            guess = input("\nGuess the song title (enter the number of your choice): ").strip().lower()

            if guess.isdigit() and 1 <= int(guess) <= 4:
                guessed_song = options[int(guess) - 1]
                if guessed_song == song_title:
                    print("Congratulations! You guessed the song title correctly.")
                    score += 10
                    guessed = True
                    break
                else:
                    print("Incorrect guess.")
                    chances -= 1
            else:
                print("Invalid input. Please enter the number corresponding to your choice.")

            print(f"Chances left: {chances}")

        if not guessed:
            print("\nOut of chances. The correct song title was:", song_title)

    print(f"\nGame over! Your total score is: {score}")

# Start the game
play_game()
