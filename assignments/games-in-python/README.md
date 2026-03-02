
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and conditionals. You'll practice user input handling, string manipulation, and game logic by creating an interactive Hangman game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Set Up the Game Board

#### Description
Initialize the game state with a randomly selected word from a predefined list and create the display format for showing player progress.

#### Requirements
Completed program should:

- Randomly select a word from a list of words
- Initialize variables to track the hidden word and guessed letters
- Display the starting game board in the format `_ _ _ _` (with correct number of blanks)
- Initialize the number of incorrect guesses remaining


### 🛠️ Implement Guess Handling and Validation

#### Description
Process player letter guesses, validate input, and update the game board with revealed letters.

#### Requirements
Completed program should:

- Prompt the player to guess a letter
- Accept single letter input and validate it's a letter
- Check if the guessed letter is in the word
- Reveal all instances of correct guesses (update the display board)
- Track incorrect guesses and decrement the remaining attempts
- Prevent the same letter from being guessed twice


### 🛠️ Complete the Game Loop with Win/Lose Logic

#### Description
Create the main game loop that continues until the player wins or loses, with appropriate end-game messages.

#### Requirements
Completed program should:

- Loop continuously until the word is fully guessed or attempts run out
- Display the current board state and remaining attempts after each guess
- Determine when the player has won (all letters revealed)
- Determine when the player has lost (no attempts remaining)
- Display a clear win message showing the word when player wins
- Display a clear lose message revealing the word when player loses
- Offer to play again or exit the game
