from typing import List, Dict, Optional
from word_manager import WordManager

class Game:
    def __init__(self, word_manager: WordManager):
        self.word_manager = word_manager
        self.max_attempts = 6
        self.current_word = word_manager.get_random_word()
        self.attempts: List[str] = []
        self.evaluations: List[List[Dict[str, str]]] = []
        self.game_over = False
        self.won = False

    def evaluate_guess(self, guess: str) -> List[Dict[str, str]]:
        """Evaluate a guess against the current word."""
        if len(guess) != len(self.current_word):
            raise ValueError("Guess length must match word length")

        # Create a copy of the current word to track used letters
        remaining_letters = list(self.current_word)
        result = []

        # First pass: mark correct letters and remove them from remaining letters
        for i, letter in enumerate(guess):
            if letter == self.current_word[i]:
                result.append({"letter": letter, "status": "correct"})
                remaining_letters.remove(letter)
            else:
                result.append({"letter": letter, "status": "absent"})

        # Second pass: mark present letters that weren't marked as correct
        for i, letter in enumerate(guess):
            if result[i]["status"] != "correct":
                if letter in remaining_letters:
                    result[i]["status"] = "present"
                    remaining_letters.remove(letter)

        return result

    async def make_guess(self, guess: str) -> List[Dict[str, str]]:
        """Make a guess and return the evaluation."""
        # Convert guess to uppercase and strip whitespace
        guess = guess.strip().upper()

        # Check if game is already over
        if self.game_over:
            raise ValueError("Game is over")

        # Validate word length
        if len(guess) != 5:
            raise ValueError("Word must be exactly 5 letters long")

        # Validate word exists in dictionary
        if not await self.word_manager.is_valid_word(guess):
            raise ValueError("Not a valid word")

        # Check if we've reached max attempts
        if len(self.attempts) >= self.max_attempts:
            self.game_over = True
            self.won = False
            raise ValueError("Maximum attempts reached")

        evaluation = self.evaluate_guess(guess)
        self.attempts.append(guess)
        self.evaluations.append(evaluation)

        # Check if won
        if guess == self.current_word:
            self.game_over = True
            self.won = True
        # Check if lost (after adding the current attempt)
        elif len(self.attempts) >= self.max_attempts:
            self.game_over = True
            self.won = False

        return evaluation

    def get_game_state(self) -> Dict:
        """Get the current game state."""
        return {
            "attempts": self.attempts,
            "evaluations": self.evaluations,
            "game_over": self.game_over,
            "won": self.won,
            "max_attempts": self.max_attempts,
            "current_attempt": len(self.attempts),
            "current_word": self.current_word
        }

    def reset(self) -> None:
        """Reset the game with a new word."""
        self.current_word = self.word_manager.get_random_word()
        self.attempts = []
        self.evaluations = []
        self.game_over = False
        self.won = False 