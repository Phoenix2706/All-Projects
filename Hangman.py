import random

def hangman(): #the hangman game
    word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'childhood', 'plane', "apple", "book", "desk", "pen", "cat", "dog", "tree", "house", "car", "phone",
    "laptop", "keyboard", "mouse", "chair", "table", "door", "window", "wall", "floor", "water", "movie", "love", "letters"]  # List of words to choose from
    word = random.choice(word_list)  # Select a random word from the list
    guessed_letters = []  # A list to store the letters guessed by the player
    tries = 10  # Number of tries the player has

    while tries > 0:
        guess = input("Enter a letter: ").lower()  # Ask the player to guess a letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.") # Prevent player from entering wrong values
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
            continue

        guessed_letters.append(guess)  # Add the guessed letter to the list

        if guess not in word:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")

        # Display the current state of the word with blanks for unguessed letters
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print(display_word)

        if "_" not in display_word:
            print("Congratulations! You won!")
            break

    if tries == 0:
        print(f"Sorry, you lost! The word was '{word}'.")

print("Good day! Welcome to the hangman game, glad you could join us here today!")
input("What's your name?")
print("Amazing! Remember to only type in lowercase, let's start! ")
hangman()