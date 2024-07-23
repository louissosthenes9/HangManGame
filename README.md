# HangManGame

Welcome to HangManGame! This is a simple terminal-based Hangman game developed by louissosthenes9. Hangman is a classic word-guessing game where you must guess the word by suggesting letters within a limited number of attempts.

## Features

- Random word selection from a predefined list.
- Keeps track of the player's guesses.
- Displays the current state of the word with underscores for unguessed letters.
- Shows a hangman graphic that progresses with each incorrect guess.
- User-friendly command-line interface.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/louissosthenes9/HangManGame.git
   cd HangManGame
   ```

2. Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).

## Usage

1. Navigate to the project directory:
   ```bash
   cd HangManGame
   ```

2. Run the game:
   ```bash
   python hangman.py
   ```

3. Follow the on-screen instructions to play the game. Guess letters one at a time until you either guess the word or run out of attempts.

## Game Rules

1. The game selects a random word from the predefined list.
2. You have a limited number of attempts to guess the word.
3. Each time you guess a letter correctly, it will be revealed in the word.
4. Each incorrect guess brings you closer to completing the hangman drawing.
5. The game ends when you either guess the word correctly or run out of attempts.

## Example

```bash
$ python hangman.py
Welcome to HangManGame!
_ _ _ _ _ _

Guess a letter: e
_ _ e _ _ _

Guess a letter: a
_ _ e _ _ _

Guess a letter: t
_ _ e _ t _

Guess a letter: s
_ _ e s t _

Guess a letter: n
You guessed it! The word was 'nestle'.
```

## Contributing

Feel free to fork this repository, create a new branch, make improvements, and submit a pull request. Your contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, please open an issue on GitHub.

Enjoy playing HangManGame!

---

louissosthenes9

GitHub: [louissosthenes9](https://github.com/louissosthenes9)
