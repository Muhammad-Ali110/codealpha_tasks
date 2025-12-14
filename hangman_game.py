import random
import sys

WORD_LIST = ["PYTHON", "CODING", "ALPHA", "INTERN", "GITHUB", "HANGMAN", "COMPUTER", "PROGRAMMING", "TECHNOLOGY", "CODE", "PROJECT", "INOVATION"]
MAX_INCORRECT_GUESSES = 6  

STAGES = [
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========
    """, 
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    ========
    """, 
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    ========
    """, 
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    ========
    """, 
    """
      +---+
      |   |
      O   |
          |
          |
          |
    ========
    """, 
    """
      +---+
      |   |
          |
          |
          |
          |
    ========
    """, 
    """
      +---+
      |   |
          |
          |
          |
          |
    ========
    """ 
]

def choose_word(words):
    """Selects a random word from the provided list."""
    return random.choice(words)

def display_game_state(incorrect_guesses_set, correct_guesses_set, word):
    """
    Displays the current hangman stage, the hidden word, and letters already guessed.
    """
    incorrect_guesses = len(incorrect_guesses_set)
    remaining_guesses = MAX_INCORRECT_GUESSES - incorrect_guesses
    print(STAGES[MAX_INCORRECT_GUESSES - incorrect_guesses])

    display_word = ""
    for letter in word:
        if letter in correct_guesses_set:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord: " + display_word)
    print(f"Incorrect Guesses Remaining: {remaining_guesses}")
    print(f"Guessed Letters: {', '.join(sorted(correct_guesses_set | incorrect_guesses_set))}")
    print("-" * 30)

def get_guess(already_guessed):
    """
    Takes and validates a single letter guess from the user.
    """
    while True:
        guess = input("Guess a letter: ").upper()
        
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not 'A' <= guess <= 'Z':
            print("Please enter a letter of the alphabet.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Try again.")
        else:
            return guess

def hangman():
    """Main function to run the Hangman game."""
    print("WELCOME TO HANGMAN!")
    print("-" * 30)

    secret_word = choose_word(WORD_LIST).upper()
    
    incorrect_guesses_set = set()
    correct_guesses_set = set()
    
    all_guesses = set() 
    
    while True:
        display_game_state(incorrect_guesses_set, correct_guesses_set, secret_word)
        
        if all(letter in correct_guesses_set for letter in secret_word):
            print(f"\n🥳 CONGRATULATIONS! You guessed the word: {secret_word}")
            break

        if len(incorrect_guesses_set) >= MAX_INCORRECT_GUESSES:
            print(STAGES[0]) # Display the final, full hangman stage
            print("\nGAME OVER! You ran out of guesses.")
            print(f"The word was: {secret_word}")
            break

        guess = get_guess(all_guesses)
        all_guesses.add(guess)

        if guess in secret_word:
            print("✅ Good guess!")
            correct_guesses_set.add(guess)
        else:
            print("❌ Incorrect guess.")
            incorrect_guesses_set.add(guess)

if __name__ == "__main__":
    hangman()