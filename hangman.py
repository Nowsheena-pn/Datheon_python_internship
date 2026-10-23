import random


# Load English words from words.txt
def load_words():
    try:
        with open("words.txt", "r") as file:
            words = [
                word.strip().lower()
                for word in file
                if word.strip().isalpha()
            ]

        # Use words with at least 4 letters
        words = [word for word in words if len(word) >= 4]

        return words

    except FileNotFoundError:
        print("Error: words.txt file not found!")
        return []


# ASCII Hangman drawings for each wrong guess
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
           |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
      =======
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
      =======
    """
]


# Main Hangman game
def play_hangman():

    words = load_words()

    if not words:
        print("No valid words available. Please check words.txt.")
        return

    # Select a random secret word
    secret_word = random.choice(words)

    # Store guessed letters
    guessed_letters = set()

    # Maximum incorrect guesses
    max_attempts = 6
    wrong_guesses = 0

    print("\n================================")
    print("     HANGMAN WORD GUESSING GAME")
    print("================================")
    print("Guess the hidden word letter by letter.")
    print("You have 6 incorrect guesses allowed.")

    # Game loop
    while wrong_guesses < max_attempts:

        # Display Hangman drawing
        print(HANGMAN_STAGES[wrong_guesses])

        # Display hidden word
        displayed_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print("Hidden Word:", displayed_word)
        print("Wrong Guesses:", wrong_guesses, "/", max_attempts)

        # Check if the player has won
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            print("The word was:", secret_word)
            print("You WIN!")
            return

        # Get user input
        guess = input("\nEnter a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter only one alphabet letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print("You already guessed this letter!")
            print("Try a different letter.")
            continue

        # Add guessed letter
        guessed_letters.add(guess)

        # Check whether the letter is correct
        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess! One attempt lost.")

    # Display final Hangman drawing
    print(HANGMAN_STAGES[max_attempts])

    # Game over
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)


# Start the game
if __name__ == "__main__":
    play_hangman()
