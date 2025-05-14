import random
from typing import List, Set
import httpx
import asyncio

class WordManager:
    def __init__(self, word_file: str = "words.txt"):
        self.word_file = word_file
        self.words: Set[str] = set()
        self.load_words()

    def load_words(self) -> None:
        """Load words from the word file."""
        try:
            with open(self.word_file, 'r') as f:
                # Convert all words to uppercase and filter for 5-letter words
                self.words = {word.strip().upper() for word in f.readlines() if len(word.strip()) == 5}
        except FileNotFoundError:
            print(f"Warning: {self.word_file} not found. Using empty word list.")
            self.words = set()

    def get_random_word(self) -> str:
        """Get a random word from the word list."""
        if not self.words:
            raise ValueError("No words available in the word list")
        word = random.choice(list(self.words))
        print(word)
        print("cddcdcdccdcdcdcdcdcdcdcdcdc")
        return word

    async def is_valid_word(self, word: str) -> bool:
        """Check if a word is valid using the dictionary API."""
        # Convert to uppercase and check length
        word = word.strip().upper()
        if len(word) != 5:
            return False

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}")
                return response.status_code == 200
        except Exception as e:
            print(f"Error checking word validity: {e}")
            return False

    def get_word_length(self) -> int:
        """Get the length of words in the word list."""
        return 5  # Wordle uses 5-letter words 