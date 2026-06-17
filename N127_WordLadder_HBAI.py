import re
from typing import List


class Solution:
    def generate_substitution_regex(self, word):
        patterns = []
        for i in range(len(word)):
            pattern = word[:i] + "." + word[i + 1 :]
            patterns.append(pattern)
        return r"^(" + "|".join(patterns) + r")$"

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Base check: If endWord isn't in the list, it's impossible
        if endWord not in wordList:
            return 0

        # Convert wordList to a set for O(1) ultra-fast lookups and removals
        words_remaining = set(wordList)

        # We store our active search paths here dynamically.
        # Format: (current_word, current_sequence_length)
        # We start at beginWord with a length of 1
        paths = [(beginWord, 1)]

        # Dynamically loop through the paths as we discover them
        for current_word, steps in paths:
            # If we reached the endWord, return the steps immediately!
            if current_word == endWord:
                return steps

            # Generate the regex pattern for the word we are currently standing on
            pattern = self.generate_substitution_regex(current_word)

            # Find all words in our remaining list that match this regex
            matches = [w for w in words_remaining if re.match(pattern, w)]

            for next_word in matches:
                # Add the new step to our paths list to be evaluated next
                paths.append((next_word, steps + 1))
                # Remove it so we don't accidentally walk in circles
                words_remaining.remove(next_word)

        # If the loop finishes and we never hit endWord, no path exists
        return 0
